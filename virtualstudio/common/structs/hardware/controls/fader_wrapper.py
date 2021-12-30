from typing import Callable

from virtualstudio.common.structs.action.abstract_action import AbstractAction, CONTROL_TYPE_FADER
from virtualstudio.common.structs.hardware.controls.abstract_control_wrapper import AbstractControlWrapper

LED_OFF = 0
LED_ON = 1

class FaderWrapper(AbstractControlWrapper):

    def __init__(self, faderValueSetter: Callable[[int], bool], ident):
        self.setFaderValue = faderValueSetter
        self.setFaderValue(0)

        super(FaderWrapper, self).__init__(ident)

    def getType(self):
        return CONTROL_TYPE_FADER

    def setAction(self, action: AbstractAction):
        super(FaderWrapper, self).setAction(action)

    def setFaderValue(self, value: int = 0) -> bool:
        #DUMMY for Code Completion and Documentation
        return False

    def touchStart(self):
        if self.action is not None:
            self.action.onTouchStart()

    def touchEnd(self):
        if self.action is not None:
            self.action.onTouchEnd()

    def touchValueChanged(self, value: int):
        if self.action is not None:
            self.action.onMove(value)

    def clearState(self):
        self.setFaderValue(0)