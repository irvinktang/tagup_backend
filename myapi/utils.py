import time

# Units of time and their relation to seconds
UNITS_OF_TIME = {
    'second': 1,
    'millisecond': 1000
}


def getUnixTime(*, unit_of_time='millisecond'):
    return time.time() * UNITS_OF_TIME[unit_of_time]
