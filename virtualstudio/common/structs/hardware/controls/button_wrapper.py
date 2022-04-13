from typing import Callable

from virtualstudio.common.structs.action.abstract_action import AbstractAction, CONTROL_TYPE_BUTTON
from virtualstudio.common.structs.hardware.controls.abstract_control_wrapper import AbstractControlWrapper

LED_OFF = 0
LED_ON = 1

class ButtonWrapper(AbstractControlWrapper):

    def __init__(self, ledStateSetter: Callable[[int], bool], ident):
        self.setLEDState = ledStateSetter
        super(ButtonWrapper, self).__init__(ident)

    def getType(self):
        return CONTROL_TYPE_BUTTON

    def setAction(self, action: AbstractAction):
        super(ButtonWrapper, self).setAction(action)

    def setLEDState(self, ledState: int = 0) -> bool:
        #DUMMY for Code Completion and Documentation
        return False

    def keyDown(self):
        if self.action is not None:
            self.action.onKeyDown()

    def keyUp(self):
        if self.action is not None:
            self.action.onKeyUp()

    def clearState(self):
        self.setLEDState(0)