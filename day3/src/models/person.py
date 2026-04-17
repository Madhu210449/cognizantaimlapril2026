"""
person model defination
"""
import re
class Person:
    """
    person model to represent person data
    """
    def __init__(self, adhar_number: str, mobile_number: int):
        self.__adhar_number = adhar_number
        self.__mobile_number = mobile_number
    
    #getter for adhar_number
    @property
    def adhar_number(self):
        return self.__adhar_number
    #getter for mobile_number
    @property
    def mobile_number(self):
        return self.__mobile_number


    #setter for mobile_number
    @mobile_number.setter
    def mobile_number(self, value):
        if not re.match(r'^\d{10}$', str(value)):
            raise ValueError("Mobile number must be a 10-digit number.")
        self.__mobile_number = value