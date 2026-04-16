"""
create doctor not found exception to handle doctor not found error
"""
class DoctorNotFoundException(Exception):
    """
    doctor not found exception to handle doctor not found error
    """
    def __init__(self, message="Doctor not found"):
        self.message = message
        super().__init__(self.message)