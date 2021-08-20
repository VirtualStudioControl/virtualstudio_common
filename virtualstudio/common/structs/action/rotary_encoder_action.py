from virtualstudio.common.structs.action.abstract_action import AbstractAction, CONTROL_TYPE_BUTTON


class RotaryEncoderAction(AbstractAction):

    #region Hardware Event Handlers

    def onKeyDown(self):
        pass

    def onKeyUp(self):
        pass

    def onRotate(self, value: int):
        pass

    #endregion