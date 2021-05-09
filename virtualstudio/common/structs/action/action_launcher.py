from typing import List, Tuple

from .abstract_action import *


class ActionLauncher:

    #region Metadata

    def getName(self) -> str:
        return "Abstract Action"

    def getIcon(self) -> str:
        return ""

    def getCategory(self) -> List[str]:
        return ["Custom"]

    def getAuthor(self) -> str:
        return "Unknown"

    def getVersion(self) -> Tuple[int, int, int]:
        return (0,0,0)

    def getID(self) -> str:
        return "{}.{}.{}-{}".format(self.getAuthor(), self.getCategory(), self.getName(), self.getVersion())

    def allowedControls(self) -> List[str]:
        return []

    def toDict(self) -> dict:
        result = {
            "name": self.getName(),
            "category": self.getCategory(),
            "author": self.getAuthor(),
            "version": self.getVersion(),
            "id": self.getID(),
            "allowedControls": self.allowedControls(),
            "icon": self.getIcon()
        }
        return result

    def getActionUI(self, control):
        return ""

    # endregion

    def getActionForControl(self, control):
        pass

