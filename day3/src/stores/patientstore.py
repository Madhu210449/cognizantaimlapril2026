"""
create patient crud operations to manage patient data
"""
import sys
import os
from src.models.patient import Patient
from src.exceptions.patient_not_found_exception import PatientNotFoundException
"""
add project root to python path
"""
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..','..')
)
sys.path.insert(0, project_root)
from conf.logger_conf import setup_logger
logger = setup_logger("patientstore.log")


class PatientStore:
    """
    patient store to manage patient data
    """
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        logger.info(f"Adding patient {patient}")
        self.patients.append(patient)

    def get_all_patients(self):
        logger.info("Retrieving all patients")
        return self.patients

    def get_patient_by_id(self, patient_id):
        logger.info(f"Retrieving patient with id {patient_id}")
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        raise PatientNotFoundException(f"Patient with id {patient_id} not found")
    
    def update_patient(self, patient_id, name=None, age=None, doctor_id=None):
        logger.info(f"Updating patient with id {patient_id}")
        patient = self.get_patient_by_id(patient_id)
        if patient:
            if name:
                patient.name = name
            if age:
                patient.age = age
            if doctor_id:
                patient.doctor_id = doctor_id
        logger.info(f"Patient with id {patient_id} updated")
        raise PatientNotFoundException(f"Patient with id {patient_id} not found")

    def delete_patient(self, patient_id):
        logger.info(f"Deleting patient with id {patient_id}")
        patient = self.get_patient_by_id(patient_id)
        if patient:
            self.patients.remove(patient)
        logger.info(f"Patient with id {patient_id} deleted")
        raise PatientNotFoundException(f"Patient with id {patient_id} not found")