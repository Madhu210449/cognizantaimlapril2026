import sys
import os
from faker import Faker

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

"""
entry point for healthcare application . this module will initialize the application and start the main loop
"""

doctor_logger = setup_logger("doctor.log")
patient_logger = setup_logger("patient.log")
appointment_logger = setup_logger("appointment.log")
app_logger = setup_logger("app.log")
faker = Faker()
doctorstore = DoctorStore()
patientstore = PatientStore()
appoinmentstore = AppoinmentStore()


doctor_id=0
patient_id=0

def doctor_app():
    doctor_logger.info("Welcome to the Doctor App")
    doctor=Doctor(id = faker.random_int(min=1, max=1000), name=faker.name(), specialization=faker.job())
    doctorstore.add_doctor(doctor)
    doctor_logger.info(f"Doctor added: {doctor}")
    global doctor_id
    doctor_id = doctor.id
 

def patient_app():
    patient_logger.info("Welcome to the Patient App")
    patient=Patient(id = faker.random_int(min=1, max=1000), name=faker.name(), dob=faker.date_of_birth(), ailment=faker.sentence())
    patientstore.add_patient(patient)
    patient_logger.info(f"Patient added: {patient}")
    global patient_id
    patient_id = patient.id
    

def appoinment_app():
    appointment_logger.info("Welcome to the Appoinment App")
    appoinment=Appointment(id = faker.random_int(min=1, max=1000), doctor = doctorstore.get_doctor_by_id(doctor_id), patient = patientstore.get_patient_by_id(patient_id), date=faker.date_time(), time=faker.time())
    appoinmentstore.add_appoinment(appoinment)
    appointment_logger.info(f"Appoinment added: {appoinment}")
    
if __name__ == "__main__":
    app_logger.info("Starting Healthcare Application")
    doctor_app()
    patient_app()
    appoinment_app()