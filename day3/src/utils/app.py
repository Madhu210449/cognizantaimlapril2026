import sys
import os

#add project root to python path

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..','..')
)
sys.path.insert(0, project_root)

from conf.logger_conf import setup_logger
from src.models.doctor import Doctor
from src.models.patient import Patient
from src.models.appoinment import Appointment
from src.stores.doctorstore import DoctorStore
from src.stores.patientstore import PatientStore
from src.stores.appoinmentstore import AppoinmentStore
from src.exceptions.doctor_not_found_exception import DoctorNotFoundException
from src.exceptions.patient_not_found_exception import PatientNotFoundException
from src.exceptions.appoinment_not_found_exception import AppoinmentNotFoundException

"""
entry point for healthcare application . this module will initialize the application and start the main loop
"""

logger = setup_logger()
doctor_id=0
patient_id=0
def doctor_app(doctor_store: DoctorStore, id: int, name: str, specialization: str):
    """
    add doctor to doctor store
    """
    global doctor_id
    doctor_id += 1
    doctor = Doctor(doctor_id, name, specialization)
    doctor_store.add_doctor(doctor)
    logger.info(f"Doctor {doctor} added successfully")
    doctor_store.get_all_doctors()
    doctor_store.get_doctor_by_id(id)
    doctor_store.update_doctor(id, name="Dr. Smith", specialization="Cardiology")


def patient_app(patient_store: PatientStore, id: int, name: str, age: int, doctor_id: int):
    """
    add patient to patient store
    """
    global patient_id
    patient_id += 1
    patient = Patient(patient_id, name, age, doctor_id)
    patient_store.add_patient(patient)
    logger.info(f"Patient {patient} added successfully")
    patient_store.get_all_patients()
    patient_store.get_patient_by_id(id)
    patient_store.update_patient(id, name="Jane Doe", age=25, doctor_id=2)

def appoinment_add(appoinment_store: AppoinmentStore, id: int, patient_id: int, doctor_id: int, date: str):
    """
    add appointment to appointment store
    """
    appoinment = Appoinment(id, patient_id, doctor_id, date)
    appoinment_store.add_appoinment(appoinment)
    logger.info(f"Appoinment {appoinment} added successfully")
    appoinment_store.get_all_appoinments()
    appoinment_store.get_appoinment_by_id(id)
    appoinment_store.update_appoinment(id, date="2023-01-01", time="10:00", doctor=Doctor(1, "Dr. Smith", "Cardiology"), patient=Patient(1, "Jane Doe", 25, 2))

if __name__ == "__main__":
    doctor_store = DoctorStore()
    patient_store = PatientStore()
    appoinment_store = AppoinmentStore()
