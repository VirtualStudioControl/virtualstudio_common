class ActionInfo:

    def __init__(self, launcher: str, control: str):
        self.launcher = launcher
        self.control = control

        self.actionParams = {}

    def toDict(self):
        result = {
            "launcher": self.launcher,
            "control": self.control,
            "parameters": self.actionParams
        }

        return result
