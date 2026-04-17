"""
Appoinment not found exception
"""
class AppoinmentNotFoundException(Exception):
    """
    Appoinment not found exception to handle appoinment not found error
    """
    def __init__(self, message="Appoinment not found"):
        self.message = message
        super().__init__(self.message)
        