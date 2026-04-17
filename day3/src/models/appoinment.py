"""
create appointment model to represent appointment data
"""
import typing
from src.models.doctor import Doctor
from src.models.patient import Patient
from datetime import date,time
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