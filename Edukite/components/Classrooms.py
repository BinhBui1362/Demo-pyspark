class Classroom:
    def __init__(self, classID, className, classGrade, classGroup, totalLesson, timetableFormatType):
        self._classID = classID
        self._className = className
        self._classGrade = classGrade
        self._classGroup = classGroup
        self._totalLesson = totalLesson
        self._timetableFormatType = timetableFormatType

    def get_classroom_ID(self): return self._classID

    def get_classroom_name(self): return self._className

    def get_classroom_grade(self): return self._classGrade

    def get_classroom_group(self): return self._classGroup

    def get_classroom_lesson(self): return self._totalLesson

    def get_classroom_format(self): return self._timetableFormatType

    def __str__(self): return str(self._className)
