import pandas as pd

from components import Classrooms
from components import Subjects
from components import Teachers
from components import Timeslots


class Data:
    file = pd.ExcelFile('Sample Data.xlsx')
    subjects10 = pd.read_excel(file, 'Subjects10')
    subjects11 = pd.read_excel(file, 'Subjects11')
    subjects12 = pd.read_excel(file, 'Subjects12')
    teachers10 = pd.read_excel(file, 'Teachers10')
    teachers11 = pd.read_excel(file, 'Teachers11')
    teachers12 = pd.read_excel(file, 'Teachers12')
    classrooms10 = pd.read_excel(file, 'Classes10')
    classrooms11 = pd.read_excel(file, 'Classes11')
    classrooms12 = pd.read_excel(file, 'Classes12')
    timeslot_format = pd.read_excel(file, 'TimeslotFormat')

    SUBJECTS_10 = subjects10.to_numpy()
    SUBJECTS_11 = subjects11.to_numpy()
    SUBJECTS_12 = subjects12.to_numpy()
    TEACHERS_10 = teachers10.to_numpy()
    TEACHERS_11 = teachers11.to_numpy()
    TEACHERS_12 = teachers12.to_numpy()
    CLASSROOMS_10 = classrooms10.to_numpy()
    CLASSROOMS_11 = classrooms11.to_numpy()
    CLASSROOMS_12 = classrooms12.to_numpy()
    TIMESLOT_FORMAT = timeslot_format.to_numpy()

    def __init__(self, grade):
        self._timeslots = []
        self._teachers = []
        self._classrooms = []
        self._subjects = []

        if grade == 11:
            for c in range(0, len(self.CLASSROOMS_11)):
                self._classrooms.append(
                    Classrooms.Classroom(self.CLASSROOMS_11[c][0], self.CLASSROOMS_11[c][1], self.CLASSROOMS_11[c][2],
                                         self.CLASSROOMS_11[c][3], self.CLASSROOMS_11[c][4], self.CLASSROOMS_11[c][5]))
            for t in range(0, len(self.TEACHERS_11)):
                self._teachers.append(
                    Teachers.Teacher(self.TEACHERS_11[t][0], self.TEACHERS_11[t][1], self.TEACHERS_11[t][2],
                                     self.TEACHERS_11[t][3]))
            for s in range(0, len(self.SUBJECTS_11)):
                self._subjects.append(
                    Subjects.Subject(self.SUBJECTS_11[s][0], self.SUBJECTS_11[s][1], self.SUBJECTS_11[s][2],
                                     self.SUBJECTS_11[s][3]))
            for ts in range(0, len(self.TIMESLOT_FORMAT)):
                self._timeslots.append(
                    Timeslots.Timeslot(self.TIMESLOT_FORMAT[ts][0], self.TIMESLOT_FORMAT[ts][1], self.TIMESLOT_FORMAT[ts][2], self.TIMESLOT_FORMAT[ts][3]))
        if grade == 12:
            for c in range(0, len(self.CLASSROOMS_12)):
                self._classrooms.append(
                    Classrooms.Classroom(self.CLASSROOMS_12[c][0], self.CLASSROOMS_12[c][1], self.CLASSROOMS_12[c][2],
                                         self.CLASSROOMS_12[c][3], self.CLASSROOMS_12[c][4], self.CLASSROOMS_12[c][5]))
            for t in range(0, len(self.TEACHERS_12)):
                self._teachers.append(
                    Teachers.Teacher(self.TEACHERS_12[t][0], self.TEACHERS_12[t][1], self.TEACHERS_12[t][2],
                                     self.TEACHERS_12[t][3]))
            for s in range(0, len(self.SUBJECTS_12)):
                self._subjects.append(
                    Subjects.Subject(self.SUBJECTS_12[s][0], self.SUBJECTS_12[s][1], self.SUBJECTS_12[s][2],
                                     self.SUBJECTS_12[s][3]))
            for ts in range(0, len(self.TIMESLOT_FORMAT)):
                self._timeslots.append(
                    Timeslots.Timeslot(self.TIMESLOT_FORMAT[ts][0], self.TIMESLOT_FORMAT[ts][1],
                                       self.TIMESLOT_FORMAT[ts][2], self.TIMESLOT_FORMAT[ts][3]))

    def get_teachers(self):
        return self._teachers

    def get_subjects(self):
        return self._subjects

    def get_classrooms(self):
        return self._classrooms

    def get_timeslots(self):
        return self._timeslots

