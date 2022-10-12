class Format:
    def __init__(self, format_type_id, name,  rs_school_day_time_slot_list_id):
        self._format_type_id = format_type_id
        self._name = name
        self._rs_school_day_time_slot_list_id = rs_school_day_time_slot_list_id

    def get_format_id(self): return self._format_type_id
    def get_format_name(self): return self._name
    def get_format_rs_school_day_time_slot_list_id(self): return self._rs_school_day_time_slot_list_id
    def __str__(self): return str(self._name) + " " + str(self._format_type_id)
