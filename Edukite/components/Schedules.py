import random as rnd
import time
from components import Teachers
from components import Lessons
from components.EmptyLessons import EmptyLesson
import itertools
import json
from components.db import connect_db as db


class Schedule:
    def __init__(self, inData):
        self._data = inData
        self.manipulated_data = []
        global_subject_list = self._data.get_subject_list()
        for sj in global_subject_list:
            connection = db.connect_to_db()
            teacher_list = db.get_teacher_by_subject(connection, sj[0], self._data.get_grade())
            db.close_connection(connection)
            if len(teacher_list) > 0:
                self.manipulated_data.append({"subject_id": sj[0], "teacher_exist": True, "teacher_list_id": teacher_list})
            elif len(teacher_list) == 0:
                self.manipulated_data.append({"subject_id": sj[0], "teacher_exist": False, "teacher_list_id": teacher_list})
        self._lessons = []
        self._HCW = 0
        self._SCW = 0
        self._fitness = 0
        self._lessonNumb = 0
        self._isFitnessChanged = True
        self._inChargeTeacher = []
        self._subject_by_classroom = []

    def get_lessons(self):
        self._isFitnessChanged = True
        return self._lessons

    def get_numbOfConflicts(self):
        return self._HCW + self._SCW

    def get_fitness(self):
        if self._isFitnessChanged:
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness

    def initialize(self):
        for c in self._data.get_classrooms():
            timeslotList = []
            inchargeTeacher = []
            totalLesson = 0
            tempLesson = []
            school_days = self._data.get_rs_school_day_time_slot()
            subject_list = []
            # get format type
            for fm in self._data.get_format_types():
                if fm.get_format_id() == c.get_classroom_format_type():
                    timeslotList = json.loads(fm.get_format_rs_school_day_time_slot_list_id())
                    break
            # get subject list
            optional_list = c.get_classroom_optionalSubject()
            if optional_list is None:
                optional_list = []
            else: optional_list = json.loads(optional_list)
            subject_list = json.loads(c.get_classroom_compulsorySubject()) + optional_list
            global_dict = self.manipulated_data
            for sl in subject_list:
                for sj in global_dict:
                    if sl == sj['subject_id']:
                        if sj['teacher_exist']:
                            random_teacher = sj['teacher_list_id'][rnd.randrange(0, len(sj['teacher_list_id']))]
                            for select_teacher in self._data.get_teachers():
                                if select_teacher.get_teacher_ID() == random_teacher[1] and select_teacher.get_teacher_subject() == random_teacher[0]:
                                    inchargeTeacher.append(select_teacher)
                                    break
                        elif not sj['teacher_exist']:
                            inchargeTeacher.append(Teachers.Teacher(-1, sj['subject_id'], -1, self._data.get_grade()))
                            break
                        break
            for edutype in self._data.get_total_lesson_by_edutype():
                if edutype['type_of_education'] == c.get_classroom_type_of_education():
                    totalLesson = edutype['total_lesson'] + len(optional_list)*2
            for x in timeslotList:
                newLesson = Lessons.Lesson(self._lessonNumb)
                self._lessonNumb += 1
                newLesson.set_lesson_classroom(c)
                newLesson.set_lesson_timeslot(x)
                for sd in school_days:
                    if x == sd[0]:
                        newLesson.set_lesson_school_day(sd[1])
                        break
                if len(tempLesson) < totalLesson:
                    check = True
                    while check:
                        if len(inchargeTeacher) == 0:
                            newLesson.set_lesson_subject(EmptyLesson())
                            newLesson.set_lesson_teacher(EmptyLesson())
                            break
                        rd = rnd.randrange(0, len(inchargeTeacher))
                        assignedTeacher = inchargeTeacher[rd]
                        assignedSubject = None
                        for s in self._data.get_subjects():
                            if assignedTeacher.get_teacher_subject() == s.get_subject_ID() and \
                                    newLesson.get_lesson_classroom().get_classroom_type_of_education() == s.get_subject_type_of_education():
                                assignedSubject = s
                                break
                        # check quantity
                        subject_count = 0
                        for n in tempLesson:
                            if n.get_lesson_classroom().get_classroom_ID() == c.get_classroom_ID():
                                if n.get_lesson_subject().get_subject_ID() == assignedSubject.get_subject_ID(): subject_count += 1
                        if subject_count < assignedSubject.get_subject_quantity():
                            newLesson.set_lesson_teacher(assignedTeacher)
                            newLesson.set_lesson_subject(assignedSubject)
                            check = False
                        elif subject_count == assignedSubject.get_subject_quantity():
                            inchargeTeacher.remove(inchargeTeacher[rd])
                elif len(tempLesson) >= totalLesson:
                    newLesson.set_lesson_subject(EmptyLesson())
                    newLesson.set_lesson_teacher(EmptyLesson())
                self._lessons.append(newLesson)
                tempLesson.append(newLesson)
        return self

    def calculate_fitness(self):
        self._HCW = 0
        self._SCW = 0
        base = 1
        lesson = self._lessons

        for i, j in itertools.combinations(lesson, 2):
            # No duplicates
            if i.get_lesson_teacher().get_teacher_ID() == -1 or j.get_lesson_teacher().get_teacher_ID() == -1:
                continue
            else:
                if i.get_lesson_timeslot() == j.get_lesson_timeslot() and i.get_lesson_teacher().get_teacher_ID() == j.get_lesson_teacher().get_teacher_ID() \
                        and i.get_lesson_subject().get_subject_ID() == j.get_lesson_subject().get_subject_ID() and \
                        i.get_lesson_classroom().get_classroom_ID() != j.get_lesson_classroom().get_classroom_ID():
                    self._HCW += 1
            # Same subjects must be consecutive
            if i.get_lesson_school_day() == j.get_lesson_school_day() and i.get_lesson_subject() == j.get_lesson_subject() and \
                    i.get_lesson_classroom() == j.get_lesson_classroom() and \
                    abs(i.get_lesson_timeslot() - j.get_lesson_timeslot()) != 1:
                self._SCW += 1

        # for les in lesson:
        #     # Empty lessons should be the last one
        #     if les.get_lesson_teacher().get_teacher_ID() == -1:
        #         a = les.get_lesson_timeslot()
        #         if les.get_lesson_timeslot() % 5 != 0:
        #             self._SCW += 1
        return 1000 - (self._HCW * base + self._SCW * base * 0.5)

    def str(self):
        returnValue = ""
        for i in range(0, len(self._lessons) - 1):
            returnValue += str(self._lessons[i]) + ","
        returnValue += str(self._lessons[len(self._lessons) - 1])
        return returnValue
