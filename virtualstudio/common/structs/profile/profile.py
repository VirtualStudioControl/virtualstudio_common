from typing import List, Dict

from ..action.action_info import ActionInfo


class Profile:

    def __init__(self, hardwareFamily: str, name: str, category: List[str]):
        self.hardwareFamily: str = hardwareFamily
        self.name: str = name
        self.category: List[str] = category

        self.actions: Dict[int, ActionInfo] = {}

    def toDict(self):
        result = {
            "hardwareFamily": self.hardwareFamily,
            "name": self.name,
            "category": self.category,
        }

        actionList = []

        for action in self.actions:
            actionList.append({"controlID": action, **self.actions[action].toDict()})

        result["actions"] = actionList

        return result
