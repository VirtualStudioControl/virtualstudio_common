from typing import Dict, Any

from virtualstudio.common.structs.action.abstract_action import AbstractAction, CONTROL_TYPE_BUTTON
from virtualstudio.common.structs.hardware.controls.button_wrapper import LED_ON, LED_OFF
from virtualstudio.common.tools import actiondatatools


class ButtonAction(AbstractAction):

    def setLEDState(self, state: int) -> bool:
        val = True
        for control in self.getControlWrappers():
            if hasattr(control, "setLEDState"):
                if callable(getattr(control, "setLEDState")):
                    val = val & control.setLEDState(state)
        return val

    #region internal

    def registerControlWrapper(self, control):
        super(ButtonAction, self).registerControlWrapper(control)
        if hasattr(control, "setLEDState"):
            if callable(getattr(control, "setLEDState")):
                control.setLEDState(actiondatatools.getValue(self.getParams(),
                                                             actiondatatools.KEY_STATE_BUTTON_LEDSTATE,
                                                             self.getState()))


    def paramsChangedInternal(self, params: Dict[str, Any]):
        self.setLEDState(actiondatatools.getValue(self.getParams(),
                                                  actiondatatools.KEY_STATE_BUTTON_LEDSTATE,
                                                  self.getState()))
        super(ButtonAction, self).paramsChangedInternal(params)

    def stateChangedInternal(self, state):
        self.setLEDState(actiondatatools.getValue(self.getParams(),
                                                  actiondatatools.KEY_STATE_BUTTON_LEDSTATE,
                                                  self.getState()))

    #endregion

    #region Hardware Event Handlers

    def onKeyDown(self):
        pass

    def onKeyUp(self):
        pass

    #endregion