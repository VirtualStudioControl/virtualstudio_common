from . import constants as consts
from .common import createRequest

def requestDeviceList():
    return createRequest(consts.REQ_DEVICE_LIST)