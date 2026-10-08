//! Stream output to an already-open Python file without reopening its pathname.

use std::io::{self, Write};

use pyo3::prelude::*;
use pyo3::types::PyBytes;

pub(crate) struct PythonWriter(pub(crate) Py<PyAny>);

impl Write for PythonWriter {
    fn write(&mut self, buffer: &[u8]) -> io::Result<usize> {
        // Bound each temporary Python bytes copy even when lopdf supplies an
        // entire stream payload to write_all in one operation.
        let buffer = &buffer[..buffer.len().min(64 * 1024)];
        Python::attach(|py| {
            let written = self
                .0
                .bind(py)
                .call_method1("write", (PyBytes::new(py, buffer),))
                .and_then(|result| result.extract::<usize>())
                .map_err(|error| io::Error::other(error.to_string()))?;
            if written > buffer.len() {
                return Err(io::Error::other(
                    "file writer reported an invalid byte count",
                ));
            }
            Ok(written)
        })
    }

    fn flush(&mut self) -> io::Result<()> {
        Python::attach(|py| {
            self.0
                .bind(py)
                .call_method0("flush")
                .map(|_| ())
                .map_err(|error| io::Error::other(error.to_string()))
        })
    }
}
