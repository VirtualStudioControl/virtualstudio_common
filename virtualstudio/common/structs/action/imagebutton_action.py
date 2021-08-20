from typing import Dict, Any, Union

from virtualstudio.common.structs.action.abstract_action import AbstractAction, CONTROL_TYPE_BUTTON
from virtualstudio.common.tools import actiondatatools, icontools


class ImageButtonAction(AbstractAction):

    def setImage(self, image: Union[bytes, bytearray, list]) -> bool:
        print("Set Image")
        val = True
        for control in self.getControlWrappers():
            if hasattr(control, "setImage"):
                if callable(getattr(control, "setImage")):
                    print("Trying to Set image")
                    val = val & control.setImage(image)

        return val

    #region internal

    def registerControlWrapper(self, control):
        super(ImageButtonAction, self).registerControlWrapper(control)
        if hasattr(control, "setImage"):
            if callable(getattr(control, "setImage")):
                print("Trying to Set image")
                control.setImage(icontools.decodeIconData(actiondatatools.getValue(self.getParams(),
                                                                        actiondatatools.KEY_STATE_IMAGEBUTTON_IMAGE,
                                                                        self.getState())))


    def paramsChangedInternal(self, params: Dict[str, Any]):
        self.setImage(icontools.decodeIconData(actiondatatools.getValue(params,
                                                                        actiondatatools.KEY_STATE_IMAGEBUTTON_IMAGE,
                                                                        self.getState())))
        super(ImageButtonAction, self).paramsChangedInternal(params)

    def stateChangedInternal(self, state):
        self.setImage(icontools.decodeIconData(actiondatatools.getValue(self.getParams(),
                                                                        actiondatatools.KEY_STATE_IMAGEBUTTON_IMAGE,
                                                                        self.getState())))

    #endregion

    #region Hardware Event Handlers

    def onKeyDown(self):
        pass

    def onKeyUp(self):
        pass

    #endregion