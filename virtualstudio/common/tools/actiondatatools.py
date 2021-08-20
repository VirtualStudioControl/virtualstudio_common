from typing import Any

STATE_VAR = "%STATE%"

KEY_STATE_BUTTON_LEDSTATE = ["states", STATE_VAR, "button", "ledstate"]

KEY_STATE_IMAGEBUTTON_IMAGE = ["states", STATE_VAR, "imagebutton", "image"]
KEY_STATE_IMAGEBUTTON_IMAGE_SRC = ["states", STATE_VAR, "imagebutton", "imagesrc"]
KEY_STATE_IMAGEBUTTON_IMAGE_BASE = ["states", STATE_VAR, "imagebutton", "imagebase"]

KEY_STATE_IMAGEBUTTON_DEVICESPECIFIC = ["states", STATE_VAR, "imagebutton", "devicespecific"]

KEY_STATE_IMAGEBUTTON_TEXT_SHOW = ["states", STATE_VAR, "imagebutton", "text", "show"]
KEY_STATE_IMAGEBUTTON_TEXT_TEXT = ["states", STATE_VAR, "imagebutton", "text", "text"]
KEY_STATE_IMAGEBUTTON_TEXT_FONT = ["states", STATE_VAR, "imagebutton", "text", "font"]
KEY_STATE_IMAGEBUTTON_TEXT_BOLD = ["states", STATE_VAR, "imagebutton", "text", "bold"]
KEY_STATE_IMAGEBUTTON_TEXT_ITALICS = ["states", STATE_VAR, "imagebutton", "text", "italics"]
KEY_STATE_IMAGEBUTTON_TEXT_UNDERLINE = ["states", STATE_VAR, "imagebutton", "text", "underline"]
KEY_STATE_IMAGEBUTTON_TEXT_STRIKETHROUGH = ["states", STATE_VAR, "imagebutton", "text", "strikethrough"]
KEY_STATE_IMAGEBUTTON_TEXT_FONTSIZE = ["states", STATE_VAR, "imagebutton", "text", "fontsize"]
KEY_STATE_IMAGEBUTTON_TEXT_ALIGNV = ["states", STATE_VAR, "imagebutton", "text", "alignv"]
KEY_STATE_IMAGEBUTTON_TEXT_ALIGNH = ["states", STATE_VAR, "imagebutton", "text", "alignh"]
KEY_STATE_IMAGEBUTTON_TEXT_COLOR_FG = ["states", STATE_VAR, "imagebutton", "text", "color_fg"]
KEY_STATE_IMAGEBUTTON_COLOR_BACKGROUND = ["states", STATE_VAR, "imagebutton", "color_background"]

KEY_STATE_ROTARYENCODER_LEDRINGMODE = ["states", STATE_VAR, "rotaryencoder", "ledringmode"]

KEY_PARAMETERS = ["params"]
KEY_GUI = ["gui"]

KEY_DESCRIPTION_TITLE = ["description", "title"]
KEY_DESCRIPTION_CONTENT = ["description", "content"]


def getValue(data, key, state: int = 0):
    return getValueOrDefault(data, key, state)


def getValueOrDefault(data, key, state: int = 0, default: Any = None):

    if isinstance(key, (list, tuple)):
        return __getValue_list(data, key, state, default)

    return __getValue_direct(data, key, state, default)


def __getValue_direct(data, key, state, default: Any = None):
    if key in data:
        return data[key]
    return default


def __getValue_list(data, key, state, default: Any = None):
    result = data
    for subkey in key:
        if subkey == STATE_VAR:
            if state < len(result):
                result = result[state]
            else:
                return None
        elif subkey not in result:
            return default
        else:
            result = result[subkey]
    return result


def setValue(data, key, value, state: int = 0):
    """
    Sets the value of the given Key in data. All keys in data not defined in value are discarded
    :param data:
    :param key:
    :param value:
    :param state:
    :return:
    """
    if isinstance(key, (list, tuple)):
        __setValue_list(data, key, value, state)
        return

    __setValue_direct(data, key, value, state)


def __setValue_direct(data, key, value, state):
    data[key] = value


def __setValue_list(data, key, value, state):
    result = data

    for subkey in key[:-1]:
        if subkey == STATE_VAR:
            while len(result) <= state:
                result.append({})
            result = result[state]
        elif subkey not in result:
            if subkey == "states":
                result[subkey] = []
            else:
                result[subkey] = {}
            result = result[subkey]
        else:
            result = result[subkey]

    result[key[-1]] = value


def updateValue(data, key, value, state: int = 0):
    """
    Merges the value with the data. (All fields not defined in value are left alone in data)

    :param data:
    :param key:
    :param value:
    :param state:
    :return:
    """
    if isinstance(key, (list, tuple)):
        __updateValue_list(data, key, value, state)
        return

    __updateValue_direct(data, key, value, state)


def __updateValue_direct(data, key, value, state):
    merge(data[key], value)


def __updateValue_list(data, key, value, state):
    result = data

    for subkey in key[:-1]:
        if subkey == STATE_VAR:
            while len(result) <= state:
                result.append({})
            result = result[state]
        elif subkey not in result:
            if subkey == "states":
                result[subkey] = []
            else:
                result[subkey] = {}
            result = result[subkey]
        else:
            result = result[subkey]

    if key[-1] not in result:
        result[key[-1]] = {}

    merge(result[key[-1]], value)


def merge(oldDict: dict, newDict: dict):

    for k in newDict:
        if k in oldDict:
            if isinstance(newDict[k], dict) and isinstance(oldDict[k], dict):
                merge(oldDict[k], newDict[k])
            else:
                oldDict[k] = newDict[k]
        else:
            oldDict[k] = newDict[k]


def ensureDefaultValue(data, key, state: int = 0, value: Any = None):
    if isinstance(key, (list, tuple)):
        __ensureDefaultValue_list(data, key, value, state)
        return

    __ensureDefaultValue_direct(data, key, value, state)


def __ensureDefaultValue_direct(data, key, value, state):
    if key not in data or data[key] is None:
        data[key] = value


def __ensureDefaultValue_list(data, key, value, state):
    result = data

    for subkey in key[:-1]:
        if subkey == STATE_VAR:
            while len(result) <= state:
                result.append({})
            result = result[state]
        elif subkey not in result:
            if subkey == "states":
                result[subkey] = []
            else:
                result[subkey] = {}
            result = result[subkey]
        else:
            result = result[subkey]

    if key[-1] not in result or result[key[-1]] is None:
        result[key[-1]] = value
