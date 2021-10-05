from typing import Dict

from virtualstudio.common.account_manager.account_info import AccountInfo
from virtualstudio.common.structs.action.action_info import ActionInfo
from virtualstudio.common.structs.profile.profile import Profile
from . import constants as consts
from .common import createRequest

#region Accounts


def requestAccountList():
    return createRequest(consts.REQ_ACCOUNT_LIST)


def setAccountData(account: AccountInfo):
    return createRequest(consts.REQ_ACCOUNT_SET_DATA,
                         {consts.REQ_ACCOUNT_SET_DATA_PARAM_ACCOUNT: account.toDictWthPasswd()})

#endregion

#region Actions


def requestActionList():
    return createRequest(consts.REQ_ACTION_LIST)


def getActionStates(action: ActionInfo):
    return createRequest(consts.REQ_GET_ACTION_STATES, {consts.REQ_GET_ACTION_STATES_PARAM_ACTION: action.toDict()})


def getActionWidget(action: ActionInfo):
    return createRequest(consts.REQ_GET_ACTION_WIDGET, {consts.REQ_GET_ACTION_WIDGET_PARAM_ACTION: action.toDict()})


def setActionData(action: ActionInfo, data: Dict):
    return createRequest(consts.REQ_SET_ACTION_DATA, {consts.REQ_SET_ACTION_DATA_PARAM_ACTION: action.toDict(),
                                                      consts.REQ_SET_ACTION_DATA_PARAM_DATA: data})

#endregion


def requestDeviceList():
    return createRequest(consts.REQ_DEVICE_LIST)


# region Profile Requests


def requestProfileSet(hardwareID: str):
    return createRequest(consts.REQ_PROFILE_SET, {consts.REQ_PROFILE_SET_PARAM_DEVICE: hardwareID})


def requestSetCurrentProfile(hardwareID: str, profileName: str):
    return createRequest(consts.REQ_SET_CURRENT_PROFILE, {consts.REQ_SET_CURRENT_PROFILE_PARAM_DEVICE: hardwareID,
                                                          consts.REQ_SET_CURRENT_PROFILE_PARAM_PROFILENAME: profileName}
                         )


def requestAddProfile(hardwareID: str, profile: Profile):
    return createRequest(consts.REQ_ADD_PROFILE, {consts.REQ_ADD_PROFILE_PARAM_DEVICE: hardwareID,
                                                  consts.REQ_ADD_PROFILE_PARAM_PROFILE: profile.toDict()})


def requestUpdateProfile(hardwareID: str, profile: Profile):
    return createRequest(consts.REQ_UPDATE_PROFILE, {consts.REQ_UPDATE_PROFILE_PARAM_DEVICE: hardwareID,
                                                     consts.REQ_UPDATE_PROFILE_PARAM_PROFILE: profile.toDict()})


def requestRemoveProfile(hardwareID: str, profileName: str):
    return createRequest(consts.REQ_REMOVE_PROFILE, {consts.REQ_REMOVE_PROFILE_PARAM_DEVICE: hardwareID,
                                                     consts.REQ_REMOVE_PROFILE_PARAM_PROFILENAME: profileName}
                         )

# endregion
