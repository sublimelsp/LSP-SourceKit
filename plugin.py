from __future__ import annotations

from LSP.plugin import LspPlugin


class SourceKit(LspPlugin):
    pass


def plugin_loaded() -> None:
    SourceKit.register()


def plugin_unloaded() -> None:
    SourceKit.unregister()
