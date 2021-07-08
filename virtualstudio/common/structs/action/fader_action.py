from virtualstudio.common.structs.action.abstract_action import AbstractAction, CONTROL_TYPE_BUTTON


class FaderAction(AbstractAction):

    #region Hardware Event Handlers

    def onTouchStart(self):
        pass

    def onTouchEnd(self):
        pass

    def onMove(self):
        pass

    #endregion