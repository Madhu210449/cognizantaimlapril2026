"""
test for doctor contract
"""
import sys
import os
import pytest
import csv
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)
from src.models.patient import Patient

@pytest.fixture
def intialize_patient():
    patient = Patient(id=1, name="John Doe", dob="1990-01-01", ailment="Flu")
    return patient
def test_patient_creation(intialize_patient):
    patient = intialize_patient
    assert patient.id == 1
    assert patient.name == "John Doe"
    assert patient.dob == "1990-01-01"
    assert patient.ailment == "Flu"

@pytest.mark.parametrize("id, name, dob, ailment", [
    (1, "John Doe", "1990-01-01", "Flu"),
    (2, "Jane Smith", "1985-05-15", "Cold"),
    (3, "Alice Johnson", "1978-09-30", "Allergy")
])
def test_parameterized_patient_creation(id, name, dob, ailment):
    patient = Patient(id=id, name=name, dob=dob, ailment=ailment)
    assert patient.id == id
    assert patient.name == name
    assert patient.dob == dob
    assert patient.ailment == ailment

def read_patient_data_from_csv():
    patients_list = []
    with open('tests/patient.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
           patients_list.append((int(row['id']), row['name'], row['dob'], row['ailment']))
    return patients_list
    
@pytest.mark.parametrize("id, name, dob, ailment", read_patient_data_from_csv())
def test_parameterized_patient_creation_from_csv(id, name, dob, ailment):
    patient = Patient(id=id, name=name, dob=dob, ailment=ailment)
    assert patient.id == id
    assert patient.name == name
    assert patient.dob == dob
    assert patient.ailment == ailment
