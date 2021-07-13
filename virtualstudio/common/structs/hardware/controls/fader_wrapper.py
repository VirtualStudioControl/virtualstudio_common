from typing import Callable

from virtualstudio.common.structs.action.abstract_action import AbstractAction
from virtualstudio.common.structs.hardware.controls.abstract_control_wrapper import AbstractControlWrapper

LED_OFF = 0
LED_ON = 1

class FaderWrapper(AbstractControlWrapper):

    def __init__(self, faderValueSetter: Callable[[int], bool]):
        self.setFaderValue = faderValueSetter
        self.setFaderValue(0)

        super(FaderWrapper, self).__init__()

    def setAction(self, action: AbstractAction):
        super(FaderWrapper, self).setAction(action)

    def setFaderValue(self, value: int = 0) -> bool:
        #DUMMY for Code Completion and Documentation
        return False
