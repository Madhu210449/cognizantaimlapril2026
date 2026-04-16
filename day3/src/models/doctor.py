"""
define a doctor class with id, name, specialization attributes. include a __str__ method for easy string representation of doctor objects
"""

class Doctor:
    def __init__(self, id, name, specialization):
        self.id = id
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"Doctor(id={self.id}, name='{self.name}', specialization='{self.specialization}')"
