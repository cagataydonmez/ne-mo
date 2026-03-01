"""Package version fallback used when setuptools_scm write_to is unavailable."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("neural-modeler")
except PackageNotFoundError:
    __version__ = "0.0.0"
