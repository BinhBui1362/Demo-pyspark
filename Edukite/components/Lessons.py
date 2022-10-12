class Lesson:
    def __init__(self, lessonID):
        self._lessonID = lessonID
        self._classroom = None
        self._subject = None
        self._teacher = None
        self._timeslot = None
        self._school_day = None

    def get_lesson_ID(self): return self._lessonID

    def get_lesson_classroom(self): return self._classroom

    def get_lesson_subject(self): return self._subject

    def get_lesson_teacher(self): return self._teacher

    def get_lesson_timeslot(self): return self._timeslot

    def set_lesson_classroom(self, classroom): self._classroom = classroom

    def set_lesson_subject(self, subject): self._subject = subject

    def set_lesson_teacher(self, teacher): self._teacher = teacher

    def set_lesson_timeslot(self, timeslot): self._timeslot = timeslot

    def set_lesson_school_day(self, school_day): self._school_day = school_day

    def get_lesson_school_day(self): return self._school_day

    def __str__(self): return str(self._lessonID)
