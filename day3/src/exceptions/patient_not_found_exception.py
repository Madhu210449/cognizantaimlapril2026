"""
patient not found exception to handle patient not found error
"""
class PatientNotFoundException(Exception):
    """
    patient not found exception to handle patient not found error
    """
    def __init__(self, message="Patient not found"):
        self.message = message
        super().__init__(self.message)