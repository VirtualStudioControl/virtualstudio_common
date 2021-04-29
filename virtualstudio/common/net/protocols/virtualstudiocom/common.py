from . import constants as consts

MESSAGE_ID = 0

def getMessageID() -> str:
    return "MSGID-{}".format(MESSAGE_ID)

def createRequest(messageType, args=None):
    if args is None:
        args = {}
    request = {consts.INTERN_REQUEST_TYPE: messageType, consts.INTERN_MESSAGE_ID: getMessageID(), "payload": args}
    return request