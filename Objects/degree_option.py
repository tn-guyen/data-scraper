class DegreeOption:
  option_name = None
  degree_name = None

  def __init__(self, option_name, degree_name):
    self.option_name = option_name
    self.degree_name = degree_name

  # Getters
  def getOptionName(self):
    return self.option_name

  def getDegreeName(self):
    return self.degree_name

  # Setters
  def setOptionName(self, option_name):
    self.option_name = option_name

  def setDegreeName(self, degree_name):
    self.degree_name = degree_name
