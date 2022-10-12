class Teacher:
    def __init__(self, rs_teacher_subject_grade_id, subject_ID, teacher_ID, grade_id):
        self._teacherID = teacher_ID
        self._subjectID = subject_ID
        self._teacherGrade = grade_id
        self._rs_teacher_subject_grade_id = rs_teacher_subject_grade_id

    def get_teacher_ID(self): return self._teacherID

    def get_teacher_subject(self): return self._subjectID

    def get_teacher_grade(self): return self._teacherGrade

    def get_rs_teacher_subject_grade_id(self): return self._rs_teacher_subject_grade_id

    def __str__(self): return str(self._teacherID) + '|' + str(self._subjectID)
