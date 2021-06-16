class ActionInfo:

    def __init__(self, launcher: str, control: int, controlType: str):
        self.launcher = launcher
        self.control = control
        self.controlType = controlType
        self.actionParams = {}

    def toDict(self):
        result = {
            "launcher": self.launcher,
            "control": self.control,
            "controlType": self.controlType,
            "parameters": self.actionParams
        }

        return result


def fromDict(values: dict):
    info = ActionInfo(launcher=values["launcher"], control=values["control"], controlType=values["controlType"])
    info.actionParams = values["parameters"]
    return info
