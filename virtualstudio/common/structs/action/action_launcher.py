CONTROL_TYPE_BUTTON = "BUTTON"
CONTROL_TYPE_IMAGE_BUTTON = "IMAGE_BUTTON"
CONTROL_TYPE_FADER = "IMAGE_BUTTON"
CONTROL_TYPE_ROTARY_ENCODER = "IMAGE_BUTTON"


class ActionLauncher:

    #region Metadata

    def getName(self):
        return "Abstract Action"

    def getIcon(self):
        return ""

    def getCategory(self):
        return ["Custom"]

    def getCategoryIcon(self):
        return ""

    def getAuthor(self):
        return "Unknown"

    def getVersion(self):
        return (0,0,0)

    def allowedControls(self):
        return []

    def getActionForControl(self, control):
        pass

    #endregion