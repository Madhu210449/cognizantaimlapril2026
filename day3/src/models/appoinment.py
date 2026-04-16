"""
create appointment model to represent appointment data
"""
import typing
from doctor import Doctor
from patient import Patient
from datetime import datetime
class Appointment:
    """
    appointment model to represent appointment data
    """
    def __init__(self, id: int, date:date, time:time, doctor: Doctor, patient: Patient):
        self.appointment_id = id
        self.date = date
        self.time = time
        self.doctor = doctor
        self.patient = patient
    def __str__(self):
        return f"Appointment(id={self.appointment_id}, date='{self.date}', time='{self.time}', doctor={self.doctor}, patient={self.patient})"