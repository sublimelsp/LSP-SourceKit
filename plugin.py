from LSP.plugin import AbstractPlugin
from LSP.plugin import ClientConfig
from LSP.plugin import register_plugin
from LSP.plugin import unregister_plugin
from LSP.plugin import WorkspaceFolder
import shutil
import sublime

# TODO: Once on Python 3.8, use the built-in typing module
from LSP.plugin.core.typing import List
from LSP.plugin.core.typing import Optional


class SourceKit(AbstractPlugin):
    @classmethod
    def name(cls) -> str:
        return cls.__name__

    @classmethod
    def can_start(
        cls,
        window: sublime.Window,
        initiating_view: sublime.View,
        workspace_folders: List[WorkspaceFolder],
        configuration: ClientConfig
    ) -> Optional[str]:
        if sublime.platform() == "osx" and not shutil.which("xcrun"):
            return "missing Xcode command-line tools"
        return None


def plugin_loaded() -> None:
    register_plugin(SourceKit)


def plugin_unloaded() -> None:
    unregister_plugin(SourceKit)
