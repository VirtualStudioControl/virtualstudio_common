from typing import List, Tuple, Optional

from ..tools.bytetools import *

def disassembleMessage(message : bytes, buffersize=16384) -> List[bytes]:
    length = bytearray()
    putInt(length, len(message), append=True)

    if len(message) < buffersize - 4:
        return [length + message]

    messages = []

    currentPos = 0
    while currentPos < len(message):
        messages.append(length + message[currentPos:min(currentPos + (buffersize - 4), len(message))])
        currentPos += (buffersize - 4)
    return messages

def assembleMessage(messageStub: Optional[bytes], packet) -> Tuple[bytes, List[bytes]]:
    processed = 0
    messages = []
    while processed < len(packet):
        if messageStub is None:
            messageStub = bytes()
        messageLen = getInt(packet, start=processed)
        processed += 4
        msgEnd = min(messageLen + processed, len(packet))
        messageStub += packet[processed:msgEnd]
        if messageLen + processed <= len(packet):
            messages.append(messageStub)
            messageStub = None
        processed = msgEnd

    return messageStub, messages


