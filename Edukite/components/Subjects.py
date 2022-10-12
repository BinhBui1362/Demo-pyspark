class Subject:
    def __init__(self, rs_subject_grade_type_of_education_id, grade_id, subject_id, type_of_education_id, no_of_lesson, is_optional):
        self._rs_subject_grade_type_of_education_id = rs_subject_grade_type_of_education_id
        self._subjectID = subject_id
        self._subjectGrade = grade_id
        self._type_of_education = type_of_education_id
        self._subjectQuantity = no_of_lesson
        self._isOptional = is_optional

    def get_rs_subject_grade_type_of_education_id(self): return self._rs_subject_grade_type_of_education_id

    def get_subject_grade(self): return self._subjectGrade

    def get_subject_quantity(self): return self._subjectQuantity

    def get_subject_ID(self): return self._subjectID

    def get_subject_type_of_education(self): return self._type_of_education

    def get_subject_status(self): return self._isOptional

    def __str__(self): return str(self._subjectID) + " " + str(self._type_of_education)
