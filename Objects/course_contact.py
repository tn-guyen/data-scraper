class CourseContact:
  def __init__(self):
    self.contact_name = None
    self.contact_phone = None
    self.contact_email = None

  # def __init__(self, contact_name, contact_phone, contact_email):
  #   self.contact_name = contact_name
  #   self.contact_phone = contact_phone
  #   self.contact_email = contact_email

  # Getters
  def getContactName(self):
    return self.contact_name

  def getContactPhone(self):
    return self.contact_phone

  def getContactEmail(self):
    return self.contact_email

  # Setters
  def setContactName(self, contact_name):
    self.contact_name = contact_name

  def setContactPhone(self, contact_phone):
    self.contact_phone = contact_phone

  def setContactEmail(self, contact_email):
    self.contact_email = contact_email
