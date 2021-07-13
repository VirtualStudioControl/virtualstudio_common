from typing import Callable

from virtualstudio.common.structs.action.abstract_action import AbstractAction
from virtualstudio.common.structs.hardware.controls.abstract_control_wrapper import AbstractControlWrapper

LED_OFF = 0
LED_ON = 1

class ButtonWrapper(AbstractControlWrapper):

    def __init__(self, ledStateSetter: Callable[[int], bool]):
        self.setLEDState = ledStateSetter
        super(ButtonWrapper, self).__init__()

    def setAction(self, action: AbstractAction):
        super(ButtonWrapper, self).setAction(action)

    def setLEDState(self, ledState: int = 0) -> bool:
        #DUMMY for Code Completion and Documentation
        return False
