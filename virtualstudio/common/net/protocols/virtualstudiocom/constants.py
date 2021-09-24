#region Client Messages
INTERN_REQUEST_TYPE = "request"
INTERN_MESSAGE_ID = "messageid"
INTERN_MESSAGE_PAYLOAD = "payload"

#region Actions

REQ_ACTION_LIST = "listActions"

REQ_GET_ACTION_STATES = "getActionStates"
REQ_GET_ACTION_STATES_PARAM_ACTION = "action"

REQ_GET_ACTION_WIDGET = "getActionWidget"
REQ_GET_ACTION_WIDGET_PARAM_ACTION = "action"

REQ_SET_ACTION_DATA = "setActionData"
REQ_SET_ACTION_DATA_PARAM_ACTION = "action"
REQ_SET_ACTION_DATA_PARAM_DATA = "data"

#endregion

REQ_DEVICE_LIST = "listDevices"

#region Profile Requests

REQ_PROFILE_SET = "getProfileSet"
REQ_PROFILE_SET_PARAM_DEVICE = "deviceID"

REQ_SET_CURRENT_PROFILE = "setCurrentProfile"
REQ_SET_CURRENT_PROFILE_PARAM_DEVICE = "deviceID"
REQ_SET_CURRENT_PROFILE_PARAM_PROFILENAME = "profileName"

REQ_ADD_PROFILE = "addProfile"
REQ_ADD_PROFILE_PARAM_DEVICE = "deviceID"
REQ_ADD_PROFILE_PARAM_PROFILE = "profile"

REQ_UPDATE_PROFILE = "updateProfile"
REQ_UPDATE_PROFILE_PARAM_DEVICE = "deviceID"
REQ_UPDATE_PROFILE_PARAM_PROFILE = "profile"

REQ_REMOVE_PROFILE = "removeProfile"
REQ_REMOVE_PROFILE_PARAM_DEVICE = "deviceID"
REQ_REMOVE_PROFILE_PARAM_PROFILENAME = "profileName"

#endregion
#endregion

#region Events

INTERN_EVENT_TYPE = "event"
INTERN_EVENT_SOURCE = "source"

#region Sources

EVT_SRC_CORE = "core"
EVT_SRC_PLUGIN = "plugin"

#endregion

#region Actions

EVT_UPDATE_PARAMS = "paramUpdate"
EVT_UPDATE_PARAMS_PARAM_ACTION = "action"

#endregion

#endregion