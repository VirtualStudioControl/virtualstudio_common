from typing import Optional, Dict, List, NewType, Any

from ...data.constants import PROFILE_NAME_DEFAULT

HARDWARE_TYPE_UNKNOWN = 0x00
HARDWARE_TYPE_ELGATO = 0x01
HARDWARE_TYPE_MIDI = 0x02


class HardwareWrapper:

    def __init__(self, device, identifier: str, name: str, manufacturer: str, profile=None):
        self.device = device
        self.name = name
        self.manufacturer = manufacturer
        self.identifier = identifier

        self.currentProfile = PROFILE_NAME_DEFAULT

        self.controls: List[Any] = []

        if profile is not None:
            self.currentProfile = profile

    def __str__(self):
        return f'{self.manufacturer} {self.name} ({self.identifier})'

    def toDict(self):
        result = {
            "type": self.getType(),
            "name": self.name,
            "manufacturer": self.manufacturer,
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

    def bindProfile(self, profile):
        self.currentProfile = profile.name
        actions = profile.getActions()

        for control in self.controls:
            control.setAction(None)

        for controlID in actions:
            self.controls[controlID].setAction(actions[controlID])


    def clearProfile(self):
        for control in self.controls:
            control.setAction(None)

    #endregion