
HARDWARE_TYPE_UNKNOWN = 0x00
HARDWARE_TYPE_ELGATO = 0x01
HARDWARE_TYPE_MIDI = 0x02

class HardwareWrapper:

    def __init__(self, device, identifier: str, name: str, manufacturer: str):
        self.device = device
        self.name = name
        self.manufacturer = manufacturer
        self.identifier = identifier

    def __str__(self):
        return f'{self.manufacturer} {self.name} ({self.identifier})'

    def toDict(self):
        result = {
            "type": self.getType(),
            "name": self.name,
            "manufacturer": self.manufacturer,
            "identifier": self.identifier
        }

        return result

    def getType(self):
        return HARDWARE_TYPE_UNKNOWN

    def bindProfile(self, profile):
        pass

    def clearProfile(self):
        pass
