import sys
import os
from faker import Faker

#add project root to python path

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..','..')
)
sys.path.insert(0, project_root)
from conf.logger_conf import setup_logger
from src.models.staff import Staff
from src.models.role import Role
logger = setup_logger("main.log")
from src.models.person import Person

def create_person():
    person = Person(adhar_number="123456789012", mobile_number=9876543210)
    print(f"Person created: Adhar Number: {person.adhar_number}, Mobile Number: {person.mobile_number}")
    """
    update mobile number
    """
    
    try:
        person.mobile_number = Faker().random_number(digits=10)  
        logger.info(f"Mobile number updated: {person.mobile_number}")
    except ValueError as e:
        logger.error(f"Error updating mobile number: {e}")

def create_staff():
    role = Role(name="Nurse", description="Responsible for patient care")
    staff = Staff(adhar_number="987654321012", mobile_number=1234567890, role=role)
    print(f"Staff created: Adhar Number: {staff.adhar_number}, Mobile Number: {staff.mobile_number}, Role: {staff.role.name}")
    
if __name__ == "__main__":
    create_person()
    create_staff()