class Degree:
    degree_name = None
    availability = {"domestic": "no", "international" : "no"}
    learning_mode = {"domestic": None, "international" : None}
    entry_score = {"domestic": None, "international" : None}
    duration = {"domestic": None, "international" : None}
    fees = {"domestic": None, "international" : None}
    next_intake = {"domestic": [], "international": []}
    location = {"domestic": None, "international" : None}

    def __init__(self):
        pass

    def setDegreeName(self, degree_name: str):
        self.degree_name = degree_name