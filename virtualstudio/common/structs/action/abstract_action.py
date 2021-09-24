from typing import Dict, Any

from virtualstudio.common.eventmanager import eventmanager
from virtualstudio.common.net.protocols.virtualstudiocom import server
from virtualstudio.common.structs.action.action_info import ActionInfo
from virtualstudio.common.structs.hardware.hardware_wrapper import HardwareWrapper
from virtualstudio.common.tools import actiondatatools

CONTROL_TYPE_NONE = "NONE"
CONTROL_TYPE_BUTTON = "BUTTON"
CONTROL_TYPE_IMAGE_BUTTON = "IMAGE_BUTTON"
CONTROL_TYPE_FADER = "FADER"
CONTROL_TYPE_ROTARY_ENCODER = "ROTARY_ENCODER"


class AbstractAction:

    def __init__(self, launcher, controlID, actionInfo: ActionInfo):
        self.__launcher = launcher
        self.__controlID = controlID
        self.__info: ActionInfo = actionInfo
        self.__control_wrappers = []
        self.onLoad()
    #region PlugIn API

    def storeParams(self, params: Dict[str, Any], replace: bool = False):
        if not replace:
            actiondatatools.merge(self.__info.actionParams, params)
            self.paramsChangedInternal(self.__info.actionParams)
            return

        self.__info.actionParams = params
        self.paramsChangedInternal(self.__info.actionParams)

    def getActionInfo(self):
        return self.__info

    def getParams(self) -> Dict[str, Any]:
        return self.__info.actionParams
        #return actiondatatools.getValueOrDefault(data=self.__info.actionParams, key=actiondatatools.KEY_PARAMETERS,
        #                                         state=self.__info.currentState, default={})

    def setState(self, state: int):
        self.__info.currentState = state
        self.stateChangedInternal(state)

    def getState(self) -> int:
        return self.__info.currentState

    def setGUIParameter(self, widgetName: str, parameter: str, value: Any, silent: bool = False):
        actiondatatools.setValue(self.__info.actionParams, [*actiondatatools.KEY_GUI, widgetName, parameter], value)
        if not silent:
            eventmanager.sendEvent(server.updateActionData(self.__info))

    def getGUIParameter(self, widgetName: str, parameter: str):
        return actiondatatools.getValue(self.__info.actionParams, [*actiondatatools.KEY_GUI, widgetName, parameter])

    def nextState(self):
        state = self.getState()
        self.setState((state + 1) % self.__launcher.getActionStateCount(self.__info.controlType))

    def prevState(self):
        state = self.getState()
        self.setState((state - 1) % self.__launcher.getActionStateCount(self.__info.controlType))

    def isActive(self):
        return len(self.__control_wrappers) > 0

    #endregion

    #region internal

    def registerControlWrapper(self, control):
        self.__control_wrappers.append(control)

    def unregisterControlWrapper(self, control):
        self.__control_wrappers.remove(control)

    def getControlWrappers(self):
        return self.__control_wrappers

    def paramsChangedInternal(self, params: Dict[str, Any]):
        self.onParamsChanged(params)
        eventmanager.sendEvent(server.updateActionData(self.__info))

    def stateChangedInternal(self, state):
        pass

    #endregion

    #region handlers

    def onLoad(self):
        pass

    def onAppear(self):
        pass

    def onDisappear(self):
        pass

    def onSettingsGUIAppear(self):
        pass

    def onSettingsGUIDisappear(self):
        pass

    def onParamsChanged(self, parameters: dict):
        pass

    #endregion