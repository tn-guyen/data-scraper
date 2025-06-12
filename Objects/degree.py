from Objects.degree_plan import *

class Degree:
    degree_name = None
    level_of_study = None
    availability = {"domestic": "no", "international" : "no"}
    learning_mode = {"domestic": None, "international" : None}
    entry_score = {"domestic": None, "international" : None}
    duration = {"domestic": None, "international" : None}
    fees = {"domestic": None, "international" : None}
    next_intake = {"domestic": [], "international": []}
    location = {"domestic": None, "international" : None}
    degree_plans = {}

    def __init__(self):
        pass

    # Getters
    def getDegreeName(self):
        return self.degree_name
    
    def getLevelOfStudy(self):
        return self.level_of_study

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
    
    def getDegreePlans(self):
        return self.degree_plans

    # Setters
    def setDegreeName(self, degree_name: str):
        self.degree_name = degree_name
    
    def setLevelOfStudy(self, level_of_study):
        self.level_of_study = level_of_study

    def setAvailability(self, student_type: str, value: bool):
        self.availability.update({student_type: value})

    def setLearningMode(self, student_type: str, learning_mode: str):
        self.learning_mode.update({student_type: learning_mode})

    def setEntryScore(self, student_type: str, entry_score: str):
        self.entry_score.update({student_type: entry_score})

    def setDuration(self, student_type: str, duration: str):
        self.duration.update({student_type: duration})

    def setFees(self, student_type: str, fees: str):
        self.fees.update({student_type: fees})

    def setNextIntake(self, student_type: str, next_intake: str):
        self.next_intake.update({student_type: next_intake})

    def setLocation(self, student_type: str, location: str):
        self.location.update({student_type: location})
    
    def setDegreePlans(self, degree_plan: DegreePlan):
        self.degree_plans.update({degree_plan.getPlanCode() : degree_plan})