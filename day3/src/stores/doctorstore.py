"""
create doctor store to manage doctor data
"""
import sys
import os
from models.doctor import Doctor
from exceptions.doctor_not_found_exception import DoctorNotFoundException

#add project root to python path

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..','..')
)
sys.path.insert(0, project_root)

from conf.logger_conf import setup_logger

class DoctorStore:
    """
    doctor store to manage doctor data
    """
    def __init__(self):
        self.doctors = []

    def add_doctor(self, doctor: Doctor):
        logger.info(f"Adding doctor {doctor}")
        self.doctors.append(doctor)

    def get_all_doctors(self):
        logger.info("Getting all doctors")
        return self.doctors

    def get_doctor_by_id(self, doctor_id: int):-> Doctor:
        logger.info(f"Getting doctor with id {doctor_id}")
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        raise DoctorNotFoundException(f"Doctor with id {doctor_id} not found")

    def update_doctor(self, doctor_id: int, name: str = None, specialization: str = None):
        logger.info(f"Updating doctor with id {doctor_id}")
        doctor = self.get_doctor_by_id(doctor_id)
        if doctor:
            if name:
                doctor.name = name
            if specialization:
                doctor.specialization = specialization
    def delete_doctor(self, doctor_id: int):
        logger.info(f"Deleting doctor with id {doctor_id}")
        doctor = self.get_doctor_by_id(doctor_id)
        if doctor:
            self.doctors.remove(doctor)