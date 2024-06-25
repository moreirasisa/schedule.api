class AppointmentTypeException(Exception):
    def __init__(self, message: str = "An error has occurred", name: str = "Appointment Type"):
        self.message = message
        self.name = name
        super().__init__(self.message, self.name)
        
class AppointmentNotFoundException(AppointmentTypeException):
    def __init__(self):
        self.message = "The appointment type doesn't exist"
        super().__init__(self.message)