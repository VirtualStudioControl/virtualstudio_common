from typing import Dict, Any

from virtualstudio.common.structs.action.action_info import ActionInfo
from virtualstudio.common.structs.hardware.hardware_wrapper import HardwareWrapper
from virtualstudio.common.tools import actiondatatools

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
        self.__currentState = 0

    #region PlugIn API

    def storeParams(self, params: Dict[str, Any], replace: bool = True):
        if replace:
            actiondatatools.updateValue(data=self.__info.actionParams, key=actiondatatools.KEY_PARAMETERS,
                                        state=self.__currentState, value=params)
            return

        actiondatatools.setValue(data=self.__info.actionParams, key=actiondatatools.KEY_PARAMETERS,
                                 state=self.__currentState, value=params)

    def getParams(self) -> Dict[str, Any]:
        return actiondatatools.getValueOrDefault(data=self.__info.actionParams, key=actiondatatools.KEY_PARAMETERS,
                                                 state=self.__currentState, default={})

    def setState(self, state: int):
        self.__currentState = state

    def getState(self) -> int:
        return self.__currentState

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