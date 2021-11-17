from typing import Dict, Any

from virtualstudio.common.structs.action.abstract_action import AbstractAction, CONTROL_TYPE_BUTTON
from virtualstudio.common.tools import actiondatatools


class RotaryEncoderAction(AbstractAction):

    def setLEDRingValue(self, value: int = 0) -> bool:
        val = True
        for control in self.getControlWrappers():
            if hasattr(control, "setLEDRingValue"):
                if callable(getattr(control, "setLEDRingValue")):
                    val = val & control.setLEDRingValue(value)
        return val

    def setLEDRingMode(self, mode: int = 0) -> bool:
        val = True
        for control in self.getControlWrappers():
            if hasattr(control, "setLEDRingMode"):
                if callable(getattr(control, "setLEDRingMode")):
                    val = val & control.setLEDRingMode(mode)
        return val

    #region internal

    def registerControlWrapper(self, control):
        super(RotaryEncoderAction, self).registerControlWrapper(control)
        if hasattr(control, "setLEDRingMode"):
            if callable(getattr(control, "setLEDRingMode")):
                control.setLEDRingMode(actiondatatools.getValue(self.getParams(),
                                       actiondatatools.KEY_STATE_ROTARYENCODER_LEDRINGMODE,
                                       self.getState()))


    def paramsChangedInternal(self, params: Dict[str, Any]):
        self.setLEDRingMode(actiondatatools.getValue(self.getParams(),
                                                  actiondatatools.KEY_STATE_ROTARYENCODER_LEDRINGMODE,
                                                  self.getState()))
        super(RotaryEncoderAction, self).paramsChangedInternal(params)

    def stateChangedInternal(self, state):
        self.setLEDRingMode(actiondatatools.getValue(self.getParams(),
                                                     actiondatatools.KEY_STATE_ROTARYENCODER_LEDRINGMODE,
                                                     self.getState()))

    #endregion

    #region Hardware Event Handlers

    def onKeyDown(self):
        pass

    def onKeyUp(self):
        pass

    def onRotate(self, value: int):
        pass

    #endregion