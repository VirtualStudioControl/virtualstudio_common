from typing import Callable

from virtualstudio.common.structs.action.abstract_action import AbstractAction
from virtualstudio.common.structs.hardware.controls.abstract_control_wrapper import AbstractControlWrapper

LED_OFF = 0
LED_ON = 1

class RotaryEncoderWrapper(AbstractControlWrapper):

    def __init__(self, ledValueSetter: Callable[[int], bool], ledModeSetter: Callable[[int], bool]):
        self.setLEDRingValue = ledValueSetter
        self.setLEDRingMode = ledModeSetter
        super(RotaryEncoderWrapper, self).__init__()

    def setAction(self, action: AbstractAction):
        super(RotaryEncoderWrapper, self).setAction(action)

    def setLEDRingValue(self, ringvalue: int = 0) -> bool:
        #DUMMY for Code Completion and Documentation
        return False

    def setLEDRingMode(self, ringMode: int = 0) -> bool:
        #DUMMY for Code Completion and Documentation
        return False
