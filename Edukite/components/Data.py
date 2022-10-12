from components import Classrooms
from components import Subjects
from components import Teachers
from components import Timeslots
from components.db import connect_db as db


class Data:

    subject = []
    teacher = []
    classrooms = []
    format_type = []
    type_of_education = []
    school_day = []
    rs_school_day_time_slot = []
    rs_teacher_subject_grade = []
    rs_subject_grade_type_of_education = []

    def __init__(self, grade):
        self._grade = grade
        connection = db.connect_to_db()
        self.subject = db.get_subject(connection)
        self.teacher = db.get_teacher(connection)
        self.classrooms = db.get_classroom(connection)
        self.format_type = db.get_format_type(connection)
        self.type_of_education = db.get_type_of_education(connection)
        self.school_day = db.get_school_day(connection)
        self.rs_school_day_time_slot = db.get_rs_school_day_time_slot(connection)
        self.rs_teacher_subject_grade = db.get_rs_teacher_subject_grade(connection)
        self.rs_subject_grade_type_of_education = db.get_rs_subject_grade_type_of_education(connection)
        db.close_connection(connection)
        self._format_type = []
        self._teachers = []
        self._classrooms = []
        self._subjects = []
        self._subject_list = []
        self._totalLesson = []
        self._timeslot = []
        self._optional_subject = []
        if grade == 11:
            for c in self.classrooms:
                if c[2] == 11:  self._classrooms.append(Classrooms.Classroom(c[0], c[1], c[2], c[3], c[4], c[5], c[6]))
            for t in self.rs_teacher_subject_grade:
                if t[3] == 11: self._teachers.append(Teachers.Teacher(t[0], t[1], t[2], t[3]))
            for s in self.rs_subject_grade_type_of_education:
                if s[1] == 11: self._subjects.append(Subjects.Subject(s[0], s[1], s[2], s[3], s[4], s[5]))
            for edutype in self.type_of_education:
                total_lesson = 0
                for x in self._subjects:
                    if x.get_subject_type_of_education() == edutype[0]: total_lesson += x.get_subject_quantity()
                self._totalLesson.append({'type_of_education': edutype[0], 'total_lesson': total_lesson})
        if grade == 12:
            for c in self.classrooms:
                if c[2] == 12:  self._classrooms.append(Classrooms.Classroom(c[0], c[1], c[2], c[3], c[4], c[5], c[6]))
            for t in self.rs_teacher_subject_grade:
                if t[3] == 12: self._teachers.append(Teachers.Teacher(t[0], t[1], t[2], t[3]))
            for s in self.rs_subject_grade_type_of_education:
                if s[1] == 12: self._subjects.append(Subjects.Subject(s[0], s[1], s[2], s[3], s[4], s[5]))
            for edutype in self.type_of_education:
                total_lesson = 0
                for x in self._subjects:
                    if x.get_subject_type_of_education() == edutype[0]: total_lesson += x.get_subject_quantity()
                self._totalLesson.append({'type_of_education': edutype[0], 'total_lesson': total_lesson})
        if grade == 10:
            for c in self.classrooms:
                if c[2] == 10:  self._classrooms.append(Classrooms.Classroom(c[0], c[1], c[2], c[3], c[4], c[5], c[6]))
            for t in self.rs_teacher_subject_grade:
                if t[3] == 10: self._teachers.append(Teachers.Teacher(t[0], t[1], t[2], t[3]))
            for s in self.rs_subject_grade_type_of_education:
                if s[1] == 10: self._subjects.append(Subjects.Subject(s[0], s[1], s[2], s[3], s[4], s[5]))
            for edutype in self.type_of_education:
                total_lesson = 0
                for x in self._subjects:
                    if x.get_subject_type_of_education() == edutype[0] and x.get_subject_status() == 0:
                        total_lesson += x.get_subject_quantity()
                self._totalLesson.append({'type_of_education': edutype[0], 'total_lesson': total_lesson})
        for f in self.format_type:
            self._format_type.append(Timeslots.Format(f[0], f[1], f[2]))
        for sl in self.subject:
            self._subject_list.append(sl)
        for ts in self.rs_school_day_time_slot:
            self._timeslot.append(ts)

    def get_teachers(self):
        return self._teachers

    def get_subjects(self):
        return self._subjects

    def get_classrooms(self):
        return self._classrooms

    def get_format_types(self):
        return self._format_type

    def get_rs_subject_grade_type_of_education(self):
        return self.rs_subject_grade_type_of_education

    def get_subject_list(self):
        return self._subject_list

    def get_total_lesson_by_edutype(self):
        return self._totalLesson

    def get_rs_school_day_time_slot(self):
        return self._timeslot

    def get_grade(self):
        return self._grade
