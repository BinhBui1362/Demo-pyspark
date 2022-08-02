class Subject:
    def __init__(self,  subjectID, subjectName, appliedGroup, subjectQuantity):
        self._subjectID = subjectID
        self._subjectName = subjectName
        self._appliedGroup = appliedGroup
        self._subjectQuantity = subjectQuantity

    def get_subject_name(self): return self._subjectName

    def get_subject_quantity(self): return self._subjectQuantity

    def get_subject_ID(self): return self._subjectID

    def get_subject_classGroup(self): return self._appliedGroup

    def __str__(self): return str(self._subjectName) + " " + str(self._appliedGroup)