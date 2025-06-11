class OptionDetails:
  optionName = None
  optionType = None

  def __init__(self, optionName, optionType):
    self.optionName = optionName
    self.optionType = optionType

  # Getters
  def getOptionName(self):
    return self.optionName

  def getOptionType(self):
    return self.optionType

  # Setters
  def setOptionName(self, optionName):
    self.optionName = optionName

  def setOptionType(self, optionType):
    self.optionType = optionType
