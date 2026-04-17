import sys
import os
from src.models.doctor import Doctor
from src.models.patient import Patient
from src.models.appoinment import Appointment
from src.stores.doctorstore import DoctorStore
from src.stores.patientstore import PatientStore
from src.exceptions.appoinment_not_found_exception import AppoinmentNotFoundException
"""
add project root to python path
"""
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..','..')
)
sys.path.insert(0, project_root)
from conf.logger_conf import setup_logger
logger = setup_logger("appointmentstore.log")

class AppoinmentStore:
    """
    appoinment store to manage appoinment data
    """
    def __init__(self):
        self.appoinments = []

    def add_appoinment(self, appoinment: Appointment):
        logger.info(f"Adding appoinment {appoinment}")
        self.appoinments.append(appoinment)

    def get_all_appoinments(self):
        logger.info("Getting all appoinments")
        return self.appoinments

    def get_appoinment_by_id(self, appoinment_id: int) -> Appointment:
        logger.info(f"Getting appoinment with id {appoinment_id}")
        for appoinment in self.appoinments:
            if appoinment.appointment_id == appoinment_id:
                return appoinment
        raise AppoinmentNotFoundException(f"Appoinment with id {appoinment_id} not found")
    
    def update_appoinment(self, appoinment_id: int, date: str = None, time: str = None, doctor: Doctor = None, patient: Patient = None):
        logger.info(f"Updating appoinment with id {appoinment_id}")
        appoinment = self.get_appoinment_by_id(appoinment_id)
        if appoinment:
            if date:
                appoinment.date = date
            if time:
                appoinment.time = time
            if doctor:
                appoinment.doctor = doctor
            if patient:
                appoinment.patient = patient
        raise AppoinmentNotFoundException(f"Appoinment with id {appoinment_id} not found")

    def delete_appoinment(self, appoinment_id: int):
        logger.info(f"Deleting appoinment with id {appoinment_id}")
        appoinment = self.get_appoinment_by_id(appoinment_id)
        if appoinment:
            self.appoinments.remove(appoinment)
        raise AppoinmentNotFoundException(f"Appoinment with id {appoinment_id} not found")