from components import Schedules


class Population:
    def __init__(self, size, inData):
        self._size = size
        self._data = inData
        self._schedules = []
        for i in range(0, size):
            self._schedules.append(Schedules.Schedule(self._data).initialize())

    def get_schedules(self): return self._schedules
