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
from src.models.doctor import Doctor

@pytest.fixture
def intialize_doctor():
    doctor = Doctor(id=1, name="Dr. Smith", specialization="Cardiology")
    return doctor

def test_doctor_creation(intialize_doctor):
    doctor = intialize_doctor
    assert doctor.id == 1
    assert doctor.name == "Dr. Smith"
    assert doctor.specialization == "Cardiology"

@pytest.mark.parametrize("id, name, specialization", [
    (1, "Dr. Smith", "Cardiology"),
    (2, "Dr. Johnson", "Neurology"),
    (3, "Dr. Lee", "Pediatrics"),
])
def test_parameterized_doctor_creation(id, name, specialization):
    doctor = Doctor(id=id, name=name, specialization=specialization)
    assert doctor.id == id
    assert doctor.name == name
    assert doctor.specialization == specialization

def read_doctor_data_from_csv():
    doctors_list = []
    with open('tests/doctors.csv', 'r', newline='', encoding='utf-8') as file:
        
        reader = csv.DictReader(file)
        for row in reader:
           doctors_list.append((int(row['id']), row['name'], row['specialization']))
    return doctors_list

@pytest.mark.parametrize("id, name, specialization", read_doctor_data_from_csv())
def test_parameterized_doctor_creation_from_csv(id, name, specialization):
    doctor = Doctor(id=id, name=name, specialization=specialization)
    assert doctor.id == id
    assert doctor.name == name
    assert doctor.specialization == specialization