from virtualstudio.common.structs.action.abstract_action import *


class AbstractControlWrapper:

    def __init__(self, ident):
        super().__init__()
        self.action = None
        self.controlID = ident

    def getType(self):
        return CONTROL_TYPE_NONE

    def setAction(self, action: AbstractAction):
        if self.action == action:
            if action is None:
                self.clearState()
            return
        if self.action is not None:
            self.action.unregisterControlWrapper(self)
            self.action.onDisappear()
            if action is None:
                self.clearState()

        self.action = action

        if self.action is not None:
            self.action.registerControlWrapper(self)
            self.action.onAppear()

    def clearState(self):
        pass