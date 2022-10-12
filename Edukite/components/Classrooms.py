class Classroom:
    def __init__(self, class_ID, class_name, grade_id, type_of_education_id, format_type_id, compulsory_subject_list, optional_subject_list):
        self._classID = class_ID
        self._className = class_name
        self._classGrade = grade_id
        self._classTypeOfEducation = type_of_education_id
        self._timetableFormatType = format_type_id
        self._compulsorySubject = compulsory_subject_list
        self._optionalSubject = optional_subject_list

    def get_classroom_ID(self): return self._classID

    def get_classroom_name(self): return self._className

    def get_classroom_grade(self): return self._classGrade

    def get_classroom_type_of_education(self): return self._classTypeOfEducation

    def get_classroom_format_type(self): return self._timetableFormatType

    def get_classroom_compulsorySubject(self): return self._compulsorySubject

    def get_classroom_optionalSubject(self): return self._optionalSubject

    def __str__(self): return str(self._className)
