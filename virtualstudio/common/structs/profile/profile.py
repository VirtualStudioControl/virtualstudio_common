from typing import List, Dict

from ..action.action_info import ActionInfo
from ..action.action_info import fromDict as actionInfoFromDict

class Profile:

    def __init__(self, hardwareFamily: str, name: str, category=None):
        if category is None:
            category = []
        self.hardwareFamily: str = hardwareFamily
        self.name: str = name
        self.category: List[str] = category

        self.actions: Dict[int, ActionInfo] = {}

    def setAction(self, controlID: int, action: ActionInfo):
        self.actions[controlID] = action

    def removeAction(self, controlID: int):
        del self.actions[controlID]

    def update(self, other):
        self.hardwareFamily = other.hardwareFamily
        self.actions = other.actions

    def toDict(self):
        result = {
            "hardwareFamily": self.hardwareFamily,
            "name": self.name,
            "category": self.category,
        }

        actionList = []

        for action in self.actions:
            actionList.append(self.actions[action].toDict())

        result["actions"] = actionList

        return result

def fromDict(values: dict):
    profile = Profile(hardwareFamily=values["hardwareFamily"], name=values["name"],
                      category=values["category"])
    for actionDict in values["actions"]:
        info = actionInfoFromDict(actionDict)
        profile.setAction(controlID=info.control, action=info)

    return profile