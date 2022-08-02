class Timeslot:
    def __init__(self, timeslotID, day, timeslotNumber, timetableFormatType):
        self._day = day
        self._timeslotNumber = timeslotNumber
        self._timeslotID = timeslotID
        self._timetableFormatType = timetableFormatType

    def get_timeslot_number(self): return self._timeslotNumber
    def get_timeslot_day(self): return self._day
    def get_timeslot_ID(self): return self._timeslotID
    def get_timeslot_format(self): return self._timetableFormatType
    def __str__(self): return str(self._day) + " " + str(self._timeslotNumber)
