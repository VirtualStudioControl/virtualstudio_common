from virtualstudio.common.structs.action.action_info import ActionInfo
from .common import createEvent
from . import constants as consts


#region Actions

def updateActionData(action: ActionInfo):
    return createEvent(consts.EVT_UPDATE_PARAMS, "CORE", {consts.EVT_UPDATE_PARAMS_PARAM_ACTION: action.toDict()})

#endregion
