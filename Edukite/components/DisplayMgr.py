from distutils.command.sdist import sdist
import prettytable as prettytable
import json
from components.db import connect_db as db


class DisplayMgr:
    def __init__(self, inData):
        self._data = inData

    def print_available_data(self):
        print("> All available data")
        self.print_room()
        self.print_instructor()
        self.print_meeting_times()
        self.print_subject()

    def print_subject(self):
        availableSubject = prettytable.PrettyTable(["Subject", "Group", "Quantity"])
        subjects = self._data.get_subjects()
        for i in range(0, len(subjects)):
            availableSubject.add_row([subjects[i].get_subject_ID(), subjects[i].get_subject_type_of_education(),
                                      subjects[i].get_subject_quantity()])
        print(availableSubject)

    def print_instructor(self):
        availableInstructorTable = prettytable.PrettyTable(['Subject', "Teacher", "Grade"])
        instructors = self._data.get_teachers()
        for i in range(0, len(instructors)):
            availableInstructorTable.add_row([instructors[i].get_teacher_subject(),
                                              instructors[i].get_teacher_ID(),
                                              instructors[i].get_teacher_grade()])
        print(availableInstructorTable)

    def print_room(self):
        availableRoomTable = prettytable.PrettyTable(['# Room'])
        rooms = self._data.get_classrooms()
        for i in range(0, len(rooms)):
            availableRoomTable.add_row([rooms[i].get_classroom_name()])
        print(availableRoomTable)

    def print_meeting_times(self):
        availableMeetingTimeTable = prettytable.PrettyTable(["Format Type", "Time Slot"])
        meetingTimes = self._data.get_format_types()
        for i in range(0, len(meetingTimes)):
            availableMeetingTimeTable.add_row(
                [meetingTimes[i].get_format_name(), meetingTimes[i].get_format_rs_school_day_time_slot_list_id()])
        print(availableMeetingTimeTable)

    def print_generation(self, population):
        table1 = prettytable.PrettyTable(['Schedule #', 'Fitness', '# of Conflicts', 'Classes [room, '
                                                                                     'instructor, time]'])
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            table1.add_row([str(i), round(schedules[i].get_fitness(), 3),
                            schedules[i].get_numbOfConflicts(),
                            schedules[i].str()])
        print(table1)

    def print_schedule_as_table(self, schedule):
        classes = schedule.get_lessons()
        table = prettytable.PrettyTable(['Class #', 'Room', 'Instructor', 'Subject', "Meeting Time"])
        for i in range(0, len(classes)):
            table.add_row([str(i),
                           classes[i].get_lesson_classroom().get_classroom_name(),
                           classes[i].get_lesson_teacher().get_teacher_ID(),
                           classes[i].get_lesson_teacher().get_teacher_subject(),
                           classes[i].get_lesson_timeslot()])
        print(table)
        with open('timetable.txt', 'w+', encoding='utf-8') as file:
            file.write(str(table))

    def writeToJsonFile(self, schedule):
        classes = schedule.get_lessons()
        json_data = []
        for i in range(0, len(classes)):
            a = dict()
            a['class_id'] = classes[i].get_lesson_classroom().get_classroom_ID()
            a['subject_id'] = classes[i].get_lesson_subject().get_subject_ID()
            a['teacher_id'] = classes[i].get_lesson_teacher().get_teacher_ID()
            sdts_ids = self._data.get_rs_school_day_time_slot()
            for x in sdts_ids:
                if x[0] == classes[i].get_lesson_timeslot():
                    a['school_day_id'] = x[1]
                    a['timeslot_id'] = x[2]
                    break
            json_data.append(a)
        with open('check.json', 'w+', encoding='utf-8') as check:
            json.dump(json_data, check, ensure_ascii=False, indent=4)
        return json_data
