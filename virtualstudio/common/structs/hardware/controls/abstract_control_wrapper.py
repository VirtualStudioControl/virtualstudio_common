from virtualstudio.common.structs.action.abstract_action import AbstractAction


class AbstractControlWrapper:

    def __init__(self):
        super().__init__()
        self.action = None

    def setAction(self, action: AbstractAction):
        self.action = action