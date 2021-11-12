from virtualstudio.common.structs.action.abstract_action import AbstractAction, CONTROL_TYPE_BUTTON


class FaderAction(AbstractAction):

    def setFaderValue(self, value: int = 0) -> bool:
        val = True
        for control in self.getControlWrappers():
            if hasattr(control, "setFaderValue"):
                if callable(getattr(control, "setFaderValue")):
                    val = val & control.setFaderValue(int(value))
        return val

    #region Hardware Event Handlers

    def onTouchStart(self):
        pass

    def onTouchEnd(self):
        pass

    def onMove(self, value):
        pass

    #endregion