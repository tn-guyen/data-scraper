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

    # Getters
    def getDegreeName(self):
        return self.degree_name

    def getAvailability(self):
        return self.availability

    def getLearningMode(self):
        return self.learning_mode

    def getEntryScore(self):
        return self.entry_score

    def getDuration(self):
        return self.duration

    def getFees(self):
        return self.fees

    def getNextIntake(self):
        return self.next_intake

    def getLocation(self):
        return self.location

    # Setters
    def setDegreeName(self, degree_name: str):
        self.degree_name = degree_name

    def setAvailability(self, availability: dict):
        self.availability = availability

    def setLearningMode(self, learning_mode: dict):
        self.learning_mode = learning_mode

    def setEntryScore(self, entry_score: dict):
        self.entry_score = entry_score

    def setDuration(self, duration: dict):
        self.duration = duration

    def setFees(self, fees: dict):
        self.fees = fees

    def setNextIntake(self, next_intake: dict):
        self.next_intake = next_intake

    def setLocation(self, location: dict):
        self.location = location
