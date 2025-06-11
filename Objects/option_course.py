class OptionCourse:
  option_name = None
  course_code = {}
  course_name = None

  def __init__(self, option_name, course_code, course_name):
    self.option_name = option_name
    self.course_code = course_code
    self.course_name = course_name

  # Getters
  def getOptionName(self):
    return self.option_name

  def getCourseCode(self):
    return self.course_code

  def getCourseName(self):
    return self.course_name

  # Setters
  def setOptionName(self, option_name):
    self.option_name = option_name

  def setCourseCode(self, course_code):
    self.course_code = course_code

  def setCourseName(self, course_name):
    self.course_name = course_name
