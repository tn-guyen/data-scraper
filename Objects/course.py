class Course:
    def __init__(self):
        self.course_title = None
        self.course_code = {}
        self.credit_points = None
        self.course_coordinator = None
        self.prerequisites = {}
        self.description = None
        self.outcomes = None
        self.activities = None
        self.resources = None
        pass

    def __init__(self, course_title, course_code, credit_points, course_coordinator, prerequisites, description, outcomes, activities, resources):
        self