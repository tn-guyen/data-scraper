class Course:
    def __init__(self):
        self.course_title = None
        self.course_code = {}
        self.credit_points = None
        self.course_coordinator = None
        self.prerequisites = {}
        self.description = None

    def __init__(self, course_title, course_code, credit_points, course_coordinator, prerequisites, description):
        self.course_title = course_title
        self.course_code = course_code
        self.credit_points = credit_points
        self.course_coordinator = course_coordinator
        self.prerequisites = prerequisites
        self.description = description

    def getCourseTitle(self):
        return self.course_title

    def getCourseCode(self):
        return self.course_code

    def getCreditPoints(self):
        return self.credit_points

    def getCourseCoordinator(self):
        return self.course_coordinator

    def getPrerequisites(self):
        return self.prerequisites

    def getDescription(self):
        return self.description

    def setCourseTitle(self, course_title):
        self.course_title = course_title

    def setCourseCode(self, course_code):
        self.course_code = course_code

    def setCreditPoints(self, credit_points):
        self.credit_points = credit_points

    def setCourseCoordinator(self, course_coordinator):
        self.course_coordinator = course_coordinator

    def setPrerequisites(self, prerequisites):
        self.prerequisites = prerequisites

    def setDescription(self, description):
        self.description = description
