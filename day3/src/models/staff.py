"""
create a class Staff inherit from Person class and add 
"""

from src.models.person import Person
from src.models.role import Role
class Staff(Person):
    """
    staff model to represent staff data
    """
    def __init__(self, adhar_number: str, mobile_number: int, role: Role):
        super().__init__(adhar_number, mobile_number)
        self.__role = role #associate role with staff

    #getter for role
    @property
    def role(self):
        return self.__role
    #setter for role
    @role.setter
    def role(self, value):
        self.__role = value