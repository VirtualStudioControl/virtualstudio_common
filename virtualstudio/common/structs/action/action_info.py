from typing import Optional, Callable


class ActionInfo:

    def __init__(self, launcher: str, control: int, controlType: str,
                 deviceFamily: Optional[str] = None, profileName: Optional[str]= None,
                 currentState: int = 0):
        self.launcher = launcher
        self.control = control
        self.controlType = controlType
        self.currentState = currentState
        self.profileName = profileName
        self.deviceFamily = deviceFamily

        self.actionParams = {}

        self.dataChangedCallback: Optional[Callable[[], None]] = None

    def setDataChangedCallback(self, dataChangedCallback: Optional[Callable[[], None]]):
        self.dataChangedCallback = dataChangedCallback

    def onDataChanged(self):
        if self.dataChangedCallback is not None:
            self.dataChangedCallback()

    def toDict(self):
        result = self.toIdent()

        result["parameters"] = self.actionParams

        return result

    def toIdent(self):
        result = {
            "launcher": self.launcher,
            "control": self.control,
            "controlType": self.controlType,
            "currentState": self.currentState,
            "profileName": self.profileName,
            "deviceFamily": self.deviceFamily,
            "parameters": self.actionParams
        }

        return result

def fromDict(values: dict):
    info = ActionInfo(launcher=values["launcher"], control=values["control"], controlType=values["controlType"],
                      deviceFamily=values["deviceFamily"], profileName=values["profileName"], currentState=values["currentState"])
    if "parameters" in values:
        info.actionParams = values["parameters"]
    else:
        info.actionParams = None
    return info
