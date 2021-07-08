from typing import List, Tuple, Optional

from ..tools.bytetools import *


def disassembleMessage(message : bytes, buffersize=16384) -> List[bytes]:
    length = bytearray()
    putInt(length, len(message), append=True)

#    if len(message) < buffersize - 4:
    return [length + message]

    #messages = []
#
#    currentPos = 0
#    while currentPos < len(message):
#        print("Message Length:", "{:08X}".format(len(message)))
#        print("Sending Message:", message[currentPos:min(currentPos + (buffersize - 4), len(message))])
#        messages.append(length + message[currentPos:min(currentPos + (buffersize - 4), len(message))])
#        currentPos = min(currentPos + (buffersize - 4), len(message))
#    return messages


def assembleMessage(messageStub: Optional[bytes], packet) -> Tuple[bytes, List[bytes]]:
    if messageStub is None:
        messageStub = bytes()
    offset = len(messageStub)
    processed = 0
    messages = []
    while processed < len(packet):
        print("Offset: {:08X}".format(offset))
        messageLen = getInt(packet, start=processed)
        processed += 4
        msgEnd = min((messageLen-offset) + processed, len(packet))
        messageStub += packet[processed:msgEnd]
        if (messageLen-offset) + processed <= len(packet):
            messages.append(messageStub)
            messageStub = bytes()
            offset = 0
        processed = msgEnd

    return messageStub, messages