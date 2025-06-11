class Coordinator:
    coordinator_name = None
    coordinator_phone = None
    coordinator_email = None
    coordinator_location = None
    coordinator_availablity = None

    def __init__(self, coordinator_name, coordinator_phone, coordinator_email, coordinator_location, coordinator_availablity):
        self.coordinator_name = coordinator_name
        self.coordinator_phone = coordinator_phone
        self.coordinator_email = coordinator_email
        self.coordinator_location = coordinator_location
        self.coordinator_availablity = coordinator_availablity

    # Getters
    def getCoordinatorName(self):
        return self.coordinator_name

    def getCoordinatorPhone(self):
        return self.coordinator_phone

    def getCoordinatorEmail(self):
        return self.coordinator_email

    def getCoordinatorLocation(self):
        return self.coordinator_location

    def getCoordinatorAvailability(self):
        return self.coordinator_availablity

    # Setters
    def setCoordinatorName(self, coordinator_name):
        self.coordinator_name = coordinator_name

    def setCoordinatorPhone(self, coordinator_phone):
        self.coordinator_phone = coordinator_phone

    def setCoordinatorEmail(self, coordinator_email):
        self.coordinator_email = coordinator_email

    def setCoordinatorLocation(self, coordinator_location):
        self.coordinator_location = coordinator_location

    def setCoordinatorAvailability(self, coordinator_availablity):
        self.coordinator_availablity = coordinator_availablity