from typing import Optional, List

from ..structs.action.action_launcher import ActionLauncher
from ..tools.icontools import computeCategoryID, readPNGIcon

ACTION_LAUNCHERS: Optional[dict] = None
CATEGORY_ICONS: dict = {}


def registerCategoryIcon(category: List[str], iconPath):
    categoryID = computeCategoryID(category)
    if categoryID in CATEGORY_ICONS:
        return
    CATEGORY_ICONS[categoryID] = iconPath

def listCategoryIcons():
    result = []
    for key in CATEGORY_ICONS:
        result.append({
            'name': key,
            'icon': readPNGIcon(CATEGORY_ICONS[key])
        })
    return result

def areActionsLoaded():
    return ACTION_LAUNCHERS is not None


def loadActions():
    launchers = ActionLauncher.__subclasses__()
    for action in launchers:
        registerActionLauncher(action())


def registerActionLauncher(launcher: ActionLauncher):
    global ACTION_LAUNCHERS

    if ACTION_LAUNCHERS is None:
        ACTION_LAUNCHERS = {}

    ACTION_LAUNCHERS[launcher.getID()] = launcher


def getAllLaunchers():
    return ACTION_LAUNCHERS


def getActionByID(identifier) -> ActionLauncher:
    if identifier not in ACTION_LAUNCHERS:
        return None
    return ACTION_LAUNCHERS[identifier]
