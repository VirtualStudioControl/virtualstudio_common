from typing import List, Dict

from ..action.abstract_action import AbstractAction
from ..action.action_info import ActionInfo
from ..action.action_info import fromDict as actionInfoFromDict
from ...action_manager.actionmanager import getActionByID


class Profile:

    def __init__(self, hardwareFamily: str, name: str, category=None):
        if category is None:
            category = []
        self.hardwareFamily: str = hardwareFamily
        self.name: str = name
        self.category: List[str] = category

        self.actions: Dict[int, AbstractAction] = {}

    def setAction(self, controlID: int, action: ActionInfo):
        action.profileName = self.name
        action.deviceFamily = self.hardwareFamily
        actionLauncher = getActionByID(action.launcher)
        if actionLauncher is not None:
            self.actions[controlID] = actionLauncher.getActionForControl(controlID, action)

    def getAction(self, index: int):
        if index in self.actions:
            return self.actions[index]
        return None

    def updateActionData(self, controlID: int, actionParams: dict):
        if controlID in self.actions:
            self.actions[controlID].getActionInfo().actionParams = actionParams
            self.actions[controlID].getActionInfo().onDataChanged()

    def getActions(self):
        return self.actions

    def removeAction(self, controlID: int):
        self.actions[controlID].getActionInfo().profileName = None
        self.actions[controlID].getActionInfo().deviceFamily = None
        del self.actions[controlID]

    def update(self, other):
        #TODO: Merge Data Only, Preserve Action Instances where possible
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
            actionList.append(self.actions[action].getActionInfo().toDict())

        result["actions"] = actionList

        return result

def fromDict(values: dict):
    profile = Profile(hardwareFamily=values["hardwareFamily"], name=values["name"],
                      category=values["category"])
    for actionDict in values["actions"]:
        info = actionInfoFromDict(actionDict)
        profile.setAction(controlID=info.control, action=info)

    return profile