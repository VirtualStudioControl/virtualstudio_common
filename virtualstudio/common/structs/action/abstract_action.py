from typing import Dict, Any

class AbstractAction:

    def __init__(self):
        self.params = None

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