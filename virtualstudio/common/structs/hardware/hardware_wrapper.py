from typing import Optional, Dict, List, NewType, Any, Callable

from ...data.constants import PROFILE_NAME_DEFAULT
from ...logging import logengine

HARDWARE_TYPE_UNKNOWN = 0x00
HARDWARE_TYPE_ELGATO = 0x01
HARDWARE_TYPE_MIDI = 0x02

logger = logengine.getLogger()

class HardwareWrapper:

    def __init__(self, device, identifier: str, name: str, manufacturer: str, profile=None):
        self.device = device
        self.name = name
        self.manufacturer = manufacturer
        self.identifier = identifier

        self.label = "{} {}".format(manufacturer, name)

        self.currentProfile = PROFILE_NAME_DEFAULT

        self.controls: List[Any] = []

        if profile is not None:
            self.currentProfile = profile

        self.profileChangeCallbacks = []

    def __str__(self):
        return f'{self.manufacturer} {self.name} ({self.identifier})'

    def toDict(self):
        result = {
            "type": self.getType(),
            "name": self.name,
            "manufacturer": self.manufacturer,
            "label": self.label,
            "identifier": self.identifier,
            "currentProfile": self.currentProfile
        }

        params = self.getHardwareParameters()

        if params is not None:
            result["parameters"] = params

        return result

    def close(self):
        pass

    #region Metadata
    def getHardwareParameters(self) -> Optional[Dict]:
        return None

    def getType(self):
        return HARDWARE_TYPE_UNKNOWN

    def getHardwareFamily(self):
        return "{} {}".format(self.manufacturer, self.name)
    #endregion

    #region Controls

    def getControlType(self, index: int):
        return self.controls[index].getType()

    def getControl(self, index: int):
        return self.controls[index]

    #endregion

    #region Profiles

    def addProfileChangedCallback(self, callback: Callable[[str], None]):
        if callback not in self.profileChangeCallbacks:
            self.profileChangeCallbacks.append(callback)

    def removeProfileChangedCallback(self, callback: Callable[[str], None]):
        if callback in self.profileChangeCallbacks:
            self.profileChangeCallbacks.append(callback)

    def profileChanged(self, profileName):
        for callback in self.profileChangeCallbacks:
            try:
                callback(profileName)
            except Exception as ex:
                logger.error("An exception occured during processing profile change callbacks for profile {} of device family {}".format(profileName, self.getHardwareFamily()))
                logger.exception(ex)

    def bindProfile(self, profile):
        if profile is None:
            logger.error("Profile is None !, Device: {}".format(self.getHardwareFamily()))
            return
        self.currentProfile = profile.name
        actions: Dict[int, None] = profile.getActions()
        logger.debug("Binding Profile {} to {}".format(profile.name, profile.hardwareFamily))
        for control in self.controls:
            if not (control.controlID in actions.keys()):
                control.setAction(None)

        for controlID in actions:
            self.controls[controlID].setAction(actions[controlID])

        self.profileChanged(self.currentProfile)

    def clearProfile(self):
        try:
            raise Exception()
        except Exception as ex:
            logger.info("clearProfile() Called !, see Exception for callstack")
            logger.exception(ex)

        for control in self.controls:
            control.setAction(None)
            #control.clearState()

    #endregion