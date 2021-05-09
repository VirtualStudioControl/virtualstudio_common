from typing import Dict, Any

CONTROL_TYPE_ANY = "ANY"
CONTROL_TYPE_NONE = "NONE"
CONTROL_TYPE_BUTTON = "BUTTON"
CONTROL_TYPE_IMAGE_BUTTON = "IMAGE_BUTTON"
CONTROL_TYPE_FADER = "FADER"
CONTROL_TYPE_ROTARY_ENCODER = "ROTARY_ENCODER"


class AbstractAction:

    def __init__(self):
        self.params = None

    def getControlType(self):
        return CONTROL_TYPE_NONE

    #region Params
    def setParams(self, params: Dict[str, Any]):
        self.params = params

    def getParams(self):
        return self.params
    #endregion

    #region binding

    def bind(self, control):
        pass

    #endregion