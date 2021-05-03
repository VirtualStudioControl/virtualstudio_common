from . import constants as consts
from .common import createRequest


def requestActionList():
    return createRequest(consts.REQ_ACTION_LIST)


def requestActionIcon(action_id):
    params = {
        "actionID": action_id
    }
    return createRequest(consts.REQ_ACTION_ICON, params)


def requestDeviceList():
    return createRequest(consts.REQ_DEVICE_LIST)