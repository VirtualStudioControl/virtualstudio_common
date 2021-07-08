from typing import Dict, Any

from virtualstudio.common.structs.action.action_info import ActionInfo
from virtualstudio.common.structs.hardware.hardware_wrapper import HardwareWrapper

CONTROL_TYPE_ANY = "ANY"
CONTROL_TYPE_NONE = "NONE"
CONTROL_TYPE_BUTTON = "BUTTON"
CONTROL_TYPE_IMAGE_BUTTON = "IMAGE_BUTTON"
CONTROL_TYPE_FADER = "FADER"
CONTROL_TYPE_ROTARY_ENCODER = "ROTARY_ENCODER"


class AbstractAction:

    def __init__(self, device: HardwareWrapper, controlID, actionInfo: ActionInfo):
        self.__controlID = controlID
        self.__device: HardwareWrapper = device
        self.__info: ActionInfo = actionInfo

    #region PlugIn API

    def storeParams(self, params: Dict[str, Any], override: bool = False):
        pass

    def loadParams(self) -> Dict[str, Any]:
        pass

    def setState(self, state: int):
        pass

    def getState(self) -> int:
        pass

    #endregion

    #region UI

    def onUiParamsChanged(self, parameters: dict):
        pass

    #endregion

    #region handlers

    def onAppear(self):
        pass

    def onDisappear(self):
        pass

    def onSettingsGUIAppear(self):
        pass

    def onSettingsGUIDisappear(self):
        pass

    #endregion