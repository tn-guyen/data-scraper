class CourseCode:
    name = None
    code = None
    campus = None
    career = None
    school = None
    learning_mode = None

    def __init__(self):
        # self.code = None
        # self.campus = None
        # self.career = None
        # self.school = None
        # self.learning_mode = None
        pass

    # getters
    def getName(self):
        return self.name

    def getCode(self):
        return self.code

    def getCampus(self):
        return self.campus

    def getCareer(self):
        return self.career

    def getSchool(self):
        return self.campus

    def getLearningMode(self):
        return self.learning_mode

    # setters
    def setName(self, name):
        self.name = name

    def setCode(self, code):
        self.code = code

    def setCampus(self, campus):
        self.campus = campus

    def setCareer(self, career):
        self.career = career

    def setSchool(self, school):
        self.school = school

    def setLearningMode(self, learning_mode):
        self.learning_mode = learning_mode