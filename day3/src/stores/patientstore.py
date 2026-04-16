"""
create patient crud operations to manage patient data
"""
class PatientStore:
    """
    patient store to manage patient data
    """
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_all_patients(self):
        return self.patients

    def get_patient_by_id(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        raise PatientNotFoundException(f"Patient with id {patient_id} not found")
    
    def update_patient(self, patient_id, name=None, age=None, doctor_id=None):
        patient = self.get_patient_by_id(patient_id)
        if patient:
            if name:
                patient.name = name
            if age:
                patient.age = age
            if doctor_id:
                patient.doctor_id = doctor_id
                