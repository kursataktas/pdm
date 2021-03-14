from pkgutil import extend_path
from typing import Iterable

__path__: Iterable[str] = extend_path(__path__, __name__)
# Export for plugin use
from pdm.cli.commands.base import BaseCommand
from pdm.core import Core
from pdm.installers import Installer, Synchronizer
from pdm.iostream import stream
from pdm.project import Config, ConfigItem, Project

__all__ = (
    "Project",
    "Config",
    "ConfigItem",
    "BaseCommand",
    "Installer",
    "Synchronizer",
    "Core",
    "stream",
)


def _fix_pkg_resources():
    import importlib
    import sys

    sys.modules["pkg_resources"] = importlib.import_module("pip._vendor.pkg_resources")


_fix_pkg_resources()
del _fix_pkg_resources
