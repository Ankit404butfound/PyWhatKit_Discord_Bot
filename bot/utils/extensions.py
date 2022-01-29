import importlib
import inspect
import pkgutil
from typing import Iterator

import cogs


def unqualify(name: str) -> str:
    """Return an Unqualified name given a Qualified module/package Name"""
    return name.rsplit(".", maxsplit=1)[-1]


def walk_extensions() -> Iterator[str]:
    """Get Extension Names from bot.cogs Subpackage"""

    def on_error(name: str) -> None:
        raise ImportError(name=name)

    for module in pkgutil.walk_packages(
        cogs.__path__, f"{cogs.__name__}.", onerror=on_error
    ):
        if unqualify(module.name).startswith("_"):
            continue

        if module.ispkg:
            imported = importlib.import_module(module.name)
            if not inspect.isfunction(getattr(imported, "setup", None)):
                continue

        yield module.name


EXTENSIONS = frozenset(walk_extensions())
