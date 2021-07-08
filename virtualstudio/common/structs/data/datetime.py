from virtualstudio.common.exceptions.ObjectDeserialisationException import ObjectDeserialisationException
from virtualstudio.common.structs.data.objectserialiser import OBJECT_TYPE_DATETIME

KEY_DATE_YEAR = "year"
KEY_DATE_MONTH = "month"
KEY_DATE_DAY = "year"

KEY_TIME_HOUR = "year"
KEY_TIME_MINUTE = "year"
KEY_TIME_SECOND = "year"
KEY_TIME_MILLIS = "year"

class DateTime:

    def __init__(self, year: int = 2000, month: int = 1, day: int = 1, hour: int = 0, minute: int = 0, second: int = 0,
                 ms: int = 0):
        self.year = year
        self.month = month
        self.day = day

        self.hour = hour
        self.minute = minute
        self.second = second
        self.ms = ms

    def toDict(self):
        res = {
            "type": OBJECT_TYPE_DATETIME,
            KEY_DATE_YEAR: self.year,
            KEY_DATE_MONTH: self.month,
            KEY_DATE_DAY: self.day,

            KEY_TIME_HOUR: self.hour,
            KEY_TIME_MINUTE: self.minute,
            KEY_TIME_SECOND: self.second,
            KEY_TIME_MILLIS: self.ms
        }
        return res


def __get(dictionary, key, default):
    if key not in dictionary:
        return default
    return dictionary[key]


def fromDict(dictionary: dict) -> DateTime:

    return DateTime(year=__get(dictionary, KEY_DATE_YEAR, 2000),
                    month=__get(dictionary, KEY_DATE_MONTH, 1),
                    day=__get(dictionary, KEY_DATE_DAY, 1),
                    hour=__get(dictionary, KEY_TIME_HOUR, 0),
                    minute=__get(dictionary, KEY_TIME_MINUTE, 0),
                    second=__get(dictionary, KEY_TIME_SECOND, 0),
                    ms=__get(dictionary, KEY_TIME_MILLIS, 0))
