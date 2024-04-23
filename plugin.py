from LSP.plugin import AbstractPlugin
from LSP.plugin import ClientConfig
from LSP.plugin import register_plugin
from LSP.plugin import unregister_plugin
from LSP.plugin import WorkspaceFolder
import sublime

# TODO: Once on Python 3.8, use the built-in typing module
from LSP.plugin.core.typing import List
from LSP.plugin.core.typing import Optional


class SourceKit(AbstractPlugin):
    @classmethod
    def name(cls) -> str:
        return cls.__name__

def plugin_loaded() -> None:
    register_plugin(SourceKit)


def plugin_unloaded() -> None:
    unregister_plugin(SourceKit)
