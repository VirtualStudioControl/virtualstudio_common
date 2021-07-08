from virtualstudio.common.exceptions.ObjectDeserialisationException import ObjectDeserialisationException
from virtualstudio.common.structs.data.objectserialiser import OBJECT_TYPE_FONT

KEY_FONT_FAMILY = "fontFamily"

class Font:
    def __init__(self, fontFamily = ""):
        self.fontFamily = fontFamily

    def toDict(self):
        res = {
            "type": OBJECT_TYPE_FONT,
            KEY_FONT_FAMILY : self.fontFamily
        }
        return res

def fromDict(dictionary: dict) -> Font:
    if KEY_FONT_FAMILY not in dictionary:
        raise ObjectDeserialisationException
    return Font(dictionary[KEY_FONT_FAMILY])