from __future__ import annotations

import re
from pathlib import Path

import pylopdf

_ROOT = Path(__file__).resolve().parents[1]
_WORKFLOW = _ROOT / ".github" / "workflows" / "release.yml"
_FONTS_WORKFLOW = _ROOT / ".github" / "workflows" / "release-fonts.yml"
_DOC_CONFIGS = (
    _ROOT / "mkdocs.yml",
    _ROOT / "mkdocs.ja.yml",
    _ROOT / "mkdocs.zh-cn.yml",
    _ROOT / "mkdocs.ko.yml",
)
_NATIVE_PLATFORMS = [
    ("ubuntu-latest", "x86_64-unknown-linux-gnu"),
    ("ubuntu-24.04-arm", "aarch64-unknown-linux-gnu"),
    ("macos-latest", "aarch64-apple-darwin"),
    ("macos-15-intel", "x86_64-apple-darwin"),
    ("windows-latest", "x86_64-pc-windows-msvc"),
]
_MATRIX_ENTRY = re.compile(r"^\s+- \{ runner: ([^,]+), target: ([^ }]+) \}$", re.MULTILINE)


def _job(workflow: str, name: str) -> str:
    start = workflow.index(f"  {name}:")
    match = re.search(r"^  [a-z][a-z0-9-]*:$", workflow[start + 1 :], re.MULTILINE)
    if match is None:
        return workflow[start:]
    return workflow[start : start + 1 + match.start()]


def test_every_native_release_wheel_runs_on_its_own_architecture() -> None:
    workflow = _WORKFLOW.read_text(encoding="utf-8")

    for job_name in ("build-wheels", "build-free-threaded-wheels"):
        job = _job(workflow, job_name)
        assert _MATRIX_ENTRY.findall(job) == _NATIVE_PLATFORMS
        assert "matrix.platform.smoke" not in job
        assert "python tools/smoke_artifact.py dist" in job


def test_documentation_announcement_tracks_package_version() -> None:
    version = pylopdf.__version__
    expected_prefix = f'announcement: "pylopdf {version} ·'
    expected_url = f'announcement_url: "https://github.com/yhay81/pylopdf/releases/tag/v{version}"'

    for config_path in _DOC_CONFIGS:
        config = config_path.read_text(encoding="utf-8")
        assert expected_prefix in config, config_path.name
        assert expected_url in config, config_path.name


def test_font_release_attests_a_content_complete_reproducible_sbom() -> None:
    workflow = _FONTS_WORKFLOW.read_text(encoding="utf-8")

    assert "python tools/generate_font_sbom.py" in workflow
    assert '--source-commit "$GITHUB_SHA"' in workflow
    assert '--source-date-epoch "$(git show -s --format=%ct "$GITHUB_SHA")"' in workflow
    assert "sbom-path: release/sbom.spdx.json" in workflow
    assert "anchore/sbom-action" not in workflow


def test_workflow_budgets_allow_builds_and_the_complete_fuzz_session() -> None:
    workflows = _ROOT / ".github" / "workflows"
    for path in workflows.glob("*.yml"):
        budgets = [int(value) for value in re.findall(r"timeout-minutes: (\d+)", path.read_text())]
        assert budgets, path.name
        assert min(budgets) >= 5, path.name

    fuzz = (workflows / "fuzz.yml").read_text()
    duration = re.search(r"-max_total_time=(\d+)", fuzz)
    budget = re.search(r"timeout-minutes: (\d+)", _job(fuzz, "api"))
    assert duration is not None
    assert budget is not None
    # Reserve time for toolchain setup, a cold build, and reproducer upload.
    assert int(budget[1]) * 60 >= int(duration[1]) + 15 * 60


def test_ci_and_release_use_checked_in_dependency_graphs() -> None:
    workflows = _ROOT / ".github" / "workflows"
    for name in ("ci.yml", "fuzz.yml", "docs.yml"):
        workflow = (workflows / name).read_text()
        sync_commands = re.findall(r"uv sync[^\n]*", workflow)
        assert sync_commands
        assert all("--locked" in command for command in sync_commands), name
        assert not re.search(r"uv run (?!\-\-no-sync)", workflow), name
    release = _WORKFLOW.read_text()
    for name in ("build-wheels", "build-free-threaded-wheels"):
        assert "args: --release --locked" in _job(release, name)
    assert "MATURIN_PEP517_ARGS: --locked" in release
    assert (
        'export MATURIN_PEP517_ARGS="${MATURIN_PEP517_ARGS:+${MATURIN_PEP517_ARGS} }--locked"'
        in (_ROOT / "tools" / "build_pyodide.sh").read_text()
    )


def test_fuzz_health_observes_cancellations_without_executing_run_code() -> None:
    health = (_ROOT / ".github" / "workflows" / "fuzz-health.yml").read_text()
    assert "workflow_run:" in health
    assert "workflows: [Fuzz]" in health
    assert "types: [completed]" in health
    assert "permissions: {}" in health
    assert "checkout@" not in health
    assert "github.event.workflow_run.conclusion" in health
    assert '"$FUZZ_CONCLUSION" != "success"' in health
    assert "GITHUB_STEP_SUMMARY" in health
    assert "exit 1" in health
