from typing import Callable, Union

from virtualstudio.common.structs.action.abstract_action import AbstractAction, CONTROL_TYPE_IMAGE_BUTTON
from virtualstudio.common.structs.hardware.controls.abstract_control_wrapper import AbstractControlWrapper


class ImagebuttonWrapper(AbstractControlWrapper):

    def __init__(self, imageSetter: Callable[[Union[bytes, bytearray, list, None]], bool], ident):
        self.setImage = imageSetter
        super(ImagebuttonWrapper, self).__init__(ident)

    def getType(self):
        return CONTROL_TYPE_IMAGE_BUTTON

    def setAction(self, action: AbstractAction):
        super(ImagebuttonWrapper, self).setAction(action)

    def setImage(self, image: Union[bytes, bytearray, list, None]) -> bool:
        # DUMMY for Code Completion and Documentation
        return False


    def clearState(self):
        self.setImage(None)

    def keyDown(self):
        if self.action is not None:
            self.action.onKeyDown()

    def keyUp(self):
        if self.action is not None:
            self.action.onKeyUp()