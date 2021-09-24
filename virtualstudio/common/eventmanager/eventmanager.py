from typing import List, Callable, Dict

EVENT_SINK: List[Callable[[Dict], None]] = []

def registerSink(sink: Callable[[Dict], None]):
    EVENT_SINK.append(sink)


def removeSink(sink: Callable[[Dict], None]):
    EVENT_SINK.remove(sink)

def sendEvent(event: Dict):
    for sink in EVENT_SINK:
        sink(event)