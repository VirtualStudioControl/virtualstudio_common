from . import constants as consts
from .common import createRequest


def requestActionList():
    return createRequest(consts.REQ_ACTION_LIST)


def requestDeviceList():
    return createRequest(consts.REQ_DEVICE_LIST)


def requestProfileSet(hardwareID: str):
    return createRequest(consts.REQ_PROFILE_SET, {consts.REQ_PROFILE_SET_PARAM_DEVICE: hardwareID})
