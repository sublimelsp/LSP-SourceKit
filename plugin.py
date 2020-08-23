from LSP.plugin import AbstractPlugin, WorkspaceFolder, ClientConfig
from LSP.plugin.core.typing import List, Optional
import shutil
import sublime


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
        if not shutil.which("xcrun"):
            return "Cannot start SourceKit without Xcode command-line tools"
        return None
