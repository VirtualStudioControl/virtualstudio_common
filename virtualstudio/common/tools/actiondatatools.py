STATE_VAR = "%STATE%"

KEY_STATE_BUTTON_LEDSTATE = ["states", STATE_VAR, "button", "ledstate"]

KEY_STATE_IMAGEBUTTON_IMAGE = ["states", STATE_VAR, "imagebutton", "image"]
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
KEY_STATE_IMAGEBUTTON_TEXT_COLOR_OUTLINE = ["states", STATE_VAR, "imagebutton", "text", "color_outline"]

KEY_STATE_ROTARYENCODER_LEDRINGMODE = ["states", STATE_VAR, "rotaryencoder", "ledringmode"]

KEY_DATA = ["data"]

KEY_DESCRIPTION_TITLE = ["description", "title"]
KEY_DESCRIPTION_CONTENT = ["description", "content"]


def getValue(data, key, state: int = 0):

    if isinstance(key, (list, tuple)):
        __getValue_list(data, key, state)

    __getValue_direct(data, key, state)


def __getValue_direct(data, key, state):
    return data[key]


def __getValue_list(data, key, state):
    result = data

    for subkey in key:
        if subkey == STATE_VAR:
            result = result[state]
        elif subkey not in result:
            return None
        else:
            result = result[subkey]

    return result


def setValue(data, key, value, state: int = 0):

    if isinstance(key, (list, tuple)):
        __setValue_list(data, key, value, state)

    __setValue_direct(data, key, value, state)


def __setValue_direct(data, key, value, state):
    data[key] = value


def __setValue_list(data, key, value, state):
    result = data

    for subkey in key[:-1]:
        if subkey == STATE_VAR:
            result = result[state]
        elif subkey not in result:
            result[subkey] = {}
            result = result[subkey]
        else:
            result = result[subkey]

    result[key[-1]] = value
