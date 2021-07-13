from typing import Callable, Union

from virtualstudio.common.structs.action.abstract_action import AbstractAction
from virtualstudio.common.structs.hardware.controls.abstract_control_wrapper import AbstractControlWrapper


class ImagebuttonWrapper(AbstractControlWrapper):

    def __init__(self, imageSetter: Callable[[Union[bytes, bytearray, list]], bool]):
        self.setImage = imageSetter
        super(ImagebuttonWrapper, self).__init__()

    def setAction(self, action: AbstractAction):
        super(ImagebuttonWrapper, self).setAction(action)

    def setImage(self, image: Union[bytes, bytearray, list]) -> bool:
        # DUMMY for Code Completion and Documentation
        return False

    def keyDown(self):
        if self.action is not None:
            self.action.onKeyDown()

    def keyUp(self):
        if self.action is not None:
            self.action.onKeyUp()