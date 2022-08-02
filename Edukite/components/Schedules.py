import random as rnd
from components import Lessons
from components.Subjects import Subject
import itertools


class Schedule:
    def __init__(self, inData):
        self._data = inData
        self._lessons = []
        self._HCW = 0
        self._SCW = 0
        self._fitness = 0
        self._lessonNumb = 0
        self._isFitnessChanged = True

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
            timetableFormat = []
            for ts in self._data.get_timeslots():
                if ts.get_timeslot_format() == c.get_classroom_format(): timetableFormat.append(ts)
            for x in timetableFormat:
                newLesson = Lessons.Lesson(self._lessonNumb)
                self._lessonNumb += 1
                newLesson.set_lesson_classroom(c)
                newLesson.set_lesson_timeslot(x)

                check = True
                while check:
                    random_index = rnd.randrange(0, len(self._data.get_teachers()))
                    assignedTeacher = self._data.get_teachers()[random_index]
                    assignedSubject = None
                    for s in self._data.get_subjects():
                        if assignedTeacher.get_teacher_subject() == s.get_subject_name() and \
                                newLesson.get_lesson_classroom().get_classroom_group() == s.get_subject_classGroup():
                            assignedSubject = s
                        # check quantity
                    subject_count = 0
                    for les in self._lessons:
                        if les.get_lesson_subject() == assignedSubject: subject_count += 1
                    if subject_count < int(assignedSubject.get_subject_quantity()):
                        newLesson.set_lesson_teacher(assignedTeacher)
                        newLesson.set_lesson_subject(assignedSubject)
                        check = False
                self._lessons.append(newLesson)
        return self

    def calculate_fitness(self):
        self._HCW = 0
        self._SCW = 0
        base = 1.15
        lesson = self._lessons
        for i, j in itertools.combinations(lesson, 2):
            # Hard1: No duplicates
            if i.get_lesson_timeslot() == j.get_lesson_timeslot() and i.get_lesson_ID() != j.get_lesson_ID():
                if i.get_lesson_classroom() == j.get_lesson_classroom(): self._HCW += 1
                if i.get_lesson_teacher() == j.get_lesson_teacher(): self._HCW += 1
                if i.get_lesson_subject() == j.get_lesson_subject(): self._HCW += 1
            # Hard2: Consecutive repeated lessons
            if i.get_lesson_timeslot().get_timeslot_day() == j.get_lesson_timeslot().get_timeslot_day() and \
                    i.get_lesson_teacher() == j.get_lesson_teacher() and i.get_lesson_classroom() == j.get_lesson_classroom() and \
                    abs(i.get_lesson_ID() - j.get_lesson_ID()) != 1: self._HCW += 1
            # Hard3: One teacher for one subject of a class
            if i.get_lesson_classroom() == j.get_lesson_classroom() and i.get_lesson_subject() == j.get_lesson_subject() and \
                    i.get_lesson_teacher() != j.get_lesson_teacher(): self._HCW += 1
        #  Hard4: No limit exceeding
        # No teacher exceeding
        for t in self._data.get_teachers():
            teacher_count = 0
            for x in self._lessons:
                if t.get_teacher_ID() == x.get_lesson_teacher().get_teacher_ID():  teacher_count += 1
            if teacher_count > 35: self._HCW += 1
        # No subject exceeding
        return 5000 - (self._HCW * base ** 3 + self._SCW * base)

    def str(self):
        returnValue = ""
        for i in range(0, len(self._lessons) - 1):
            returnValue += str(self._lessons[i]) + ","
        returnValue += str(self._lessons[len(self._lessons) - 1])
        return returnValue
