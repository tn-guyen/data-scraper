class DegreePlan:
    degree_name = None
    plan_code = None
    credit_description = None
    major_minor_description = None
    core_units = {} #{course_code: year}
    major_options = {}
    minor_options = {}
    other_options = {}

    # def __init__(self, degree_name, plan_code, credit_description, major_minor_description, core_units, major_options, minor_options):
    #     self.degree_name = degree_name
    #     self.plan_code = plan_code
    #     self.credit_description = credit_description
    #     self.major_minor_description = major_minor_description
    #     self.core_units = core_units
    #     self.major_options = major_options
    #     self.minor_options = minor_options

    def getDegreeName(self):
        return self.degree_name

    def getPlanCode(self):
        return self.plan_code

    def getCreditDescription(self):
        return self.credit_description

    def getMajorMinorDescription(self):
        return self.major_minor_description

    def getCoreUnits(self):
        return self.core_units

    def getMajorOptions(self):
        return self.major_options

    def getMinorOptions(self):
        return self.minor_options
    
    def getOtherOptions(self):
        return self.other_options

    def setDegreeName(self, degree_name):
        self.degree_name = degree_name

    def setPlanCode(self, plan_code):
        self.plan_code = plan_code

    def setCreditDescription(self, credit_description):
        self.credit_description = credit_description

    def setMajorMinorDescription(self, major_minor_description):
        self.major_minor_description = major_minor_description

    def setCoreUnits(self, section,course):
        self.core_units.update({course : section})

    def setMajorOptions(self, section, course):
        self.major_options.update({course:section})

    def setMinorOptions(self, section, course):
        self.minor_options.update({course:section})
    
    def setOtherOptions(self, section, course):
        self.other_options.update({course:section})