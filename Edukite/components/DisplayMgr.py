import prettytable as prettytable


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
        availableSubject = prettytable.PrettyTable(["Subject", "Quantity"])
        subjects = self._data.get_subjects()
        for i in range(0, len(subjects)):
            availableSubject.add_row([subjects[i].get_subject_name(), subjects[i].get_subject_quantity()])
        print(availableSubject)

    def print_instructor(self):
        availableInstructorTable = prettytable.PrettyTable(['Subject', "Instructor"])
        instructors = self._data.get_teachers()
        for i in range(0, len(instructors)):
            availableInstructorTable.add_row([instructors[i].get_teacher_subject(),
                                              instructors[i].get_teacher_name()])
        print(availableInstructorTable)

    def print_room(self):
        availableRoomTable = prettytable.PrettyTable(['# Room'])
        rooms = self._data.get_classrooms()
        for i in range(0, len(rooms)):
            availableRoomTable.add_row([rooms[i].get_classroom_name()])
        print(availableRoomTable)

    def print_meeting_times(self):
        availableMeetingTimeTable = prettytable.PrettyTable(['Day', "Time Slot"])
        meetingTimes = self._data.get_timeslots()
        for i in range(0, len(meetingTimes)):
            availableMeetingTimeTable.add_row(
                [meetingTimes[i].get_timeslot_day(), meetingTimes[i].get_timeslot_number()])
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
                           classes[i].get_lesson_teacher().get_teacher_name(),
                           classes[i].get_lesson_teacher().get_teacher_subject(),
                           classes[i].get_lesson_timeslot().get_timeslot_day() + " " +
                           str(classes[i].get_lesson_timeslot().get_timeslot_number())])
        print(table)
