class Teacher:
    def __init__(self, teacherID, teacherName, subject, teacherGrade):
        self._teacherID = teacherID
        self._teacherName = teacherName
        self._subject = subject
        self._teacherGrade = teacherGrade

    def get_teacher_ID(self): return self._teacherID

    def get_teacher_name(self): return self._teacherName

    def get_teacher_subject(self): return self._subject

    def get_teacher_grade(self): return self._teacherGrade

    def __str__(self): return str(self._teacherName) + '|' + str(self._subject)
