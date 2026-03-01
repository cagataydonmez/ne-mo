# File: __init__.py

# Hack to recover graceful shutdowns in Windows.
# This has to happen ASAP
def _ensure_graceful_shutdowns():
    import os

    if os.name == "nt":  # OS is Windows
        os.environ["FOR_DISABLE_CONSOLE_CTRL_HANDLER"] = "1"


_ensure_graceful_shutdowns()

from ._version import __version__  # Must be before models or else circular

from . import _core  # noqa F401
from . import data  # noqa F401
from . import models  # noqa F401
from . import util  # noqa F401
from . import train  # noqa F401
