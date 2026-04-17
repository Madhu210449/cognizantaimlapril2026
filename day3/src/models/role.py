"""
role model defination
"""
class Role:
    """
    role model to represent role data
    """
    def __init__(self, name: str,description: str):
        self.__name = name
        self.__description = description
    #getter for name
    @property
    def name(self):
        return self.__name
    #getter for description
    @property
    def description(self):
        return self.__description
    #setter for description
    @description.setter
    def description(self, value):
        self.__description = value
    