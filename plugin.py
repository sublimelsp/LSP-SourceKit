from LSP.plugin import AbstractPlugin
from LSP.plugin import register_plugin
from LSP.plugin import unregister_plugin

class SourceKit(AbstractPlugin):
    @classmethod
    def name(cls) -> str:
        return cls.__name__

def plugin_loaded() -> None:
    register_plugin(SourceKit)


def plugin_unloaded() -> None:
    unregister_plugin(SourceKit)
