from typing import List, Callable, Dict

from virtualstudio.common.logging import logengine

EVENT_SINK: List[Callable[[Dict], None]] = []

logger = logengine.getLogger()

def registerSink(sink: Callable[[Dict], None]):
    logger.debug("Registered Event Sink !")
    EVENT_SINK.append(sink)


def removeSink(sink: Callable[[Dict], None]):
    EVENT_SINK.remove(sink)

def sendEvent(event: Dict):
    for sink in EVENT_SINK:
        sink(event)