# File: __init__.py

"""
Code for standardized training with NAM
"""

from . import colab  # noqa F401
from . import core  # noqa F401
from . import metadata  # noqa F401

try:
    from . import gui  # noqa F401
except ModuleNotFoundError as e:
    if e.name not in {"tkinter", "_tkinter"}:
        raise
