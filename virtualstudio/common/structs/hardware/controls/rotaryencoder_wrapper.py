from typing import Callable

from virtualstudio.common.structs.action.abstract_action import AbstractAction, CONTROL_TYPE_ROTARY_ENCODER
from virtualstudio.common.structs.hardware.controls.abstract_control_wrapper import AbstractControlWrapper

LED_RING_MODE_SINGLE = 0x00
LED_RING_MODE_PAN = 0x01
LED_RING_MODE_FAN = 0x02
LED_RING_MODE_SPREAD = 0x03
LED_RING_MODE_TRIM = 0x04


class RotaryEncoderWrapper(AbstractControlWrapper):

    def __init__(self, ledValueSetter: Callable[[int], bool], ledModeSetter: Callable[[int], bool]):
        self.setLEDRingValue = ledValueSetter
        self.setLEDRingMode = ledModeSetter
        super(RotaryEncoderWrapper, self).__init__()

    def getType(self):
        return CONTROL_TYPE_ROTARY_ENCODER

    def setAction(self, action: AbstractAction):
        super(RotaryEncoderWrapper, self).setAction(action)

    def setLEDRingValue(self, ringvalue: int = 0) -> bool:
        #DUMMY for Code Completion and Documentation
        return False

    def setLEDRingMode(self, ringMode: int = 0) -> bool:
        #DUMMY for Code Completion and Documentation
        return False

    def keyDown(self):
        if self.action is not None:
            self.action.onKeyDown()

    def keyUp(self):
        if self.action is not None:
            self.action.onKeyUp()

    def rotate(self, value: int):
        if self.action is not None:
            self.action.onRotate(value)
