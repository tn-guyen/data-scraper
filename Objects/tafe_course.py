class TafeCourse:
  course_name = None
  course_code = None
  contact_name = None
  hours = None
  campus = None
  career = None
  school = None
  learning_mode = None
  description = None
  competency_code = None
  competency_description = None

  def __init__(self, course_name, course_code, contact_name, hours, campus, career, school, learning_mode, description, competency_code, competency_description):
    self.course_name = course_name
    self.course_code = course_code
    self.contact_name = contact_name
    self.hours = hours
    self.campus = campus
    self.career = career
    self.school = school
    self.learning_mode = learning_mode
    self.description = description
    self.competency_code = competency_code
    self.competency_description = competency_description

  # Getters
  def getCourseName(self):
    return self.course_name

  def getCourseCode(self):
    return self.course_code

  def getContactName(self):
    return self.contact_name

  def getHours(self):
    return self.hours

  def getCampus(self):
    return self.campus

  def getCareer(self):
    return self.career

  def getSchool(self):
    return self.school

  def getLearningMode(self):
    return self.learning_mode

  def getDescription(self):
    return self.description

  def getCompetencyCode(self):
    return self.competency_code

  def getCompetencyDescription(self):
    return self.competency_description

  # Setters
  def setCourseName(self, course_name):
    self.course_name = course_name

  def setCourseCode(self, course_code):
    self.course_code = course_code

  def setContactName(self, contact_name):
    self.contact_name = contact_name

  def setHours(self, hours):
    self.hours = hours

  def setCampus(self, campus):
    self.campus = campus

  def setCareer(self, career):
    self.career = career

  def setSchool(self, school):
    self.school = school

  def setLearningMode(self, learning_mode):
    self.learning_mode = learning_mode

  def setDescription(self, description):
    self.description = description

  def setCompetencyCode(self, competency_code):
    self.competency_code = competency_code

  def setCompetencyDescription(self, competency_description):
    self.competency_description = competency_description