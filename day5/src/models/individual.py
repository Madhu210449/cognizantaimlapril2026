#create class individual using pydantic
from pydantic import BaseModel, Field
from models.customer import Customer
from models.gender import Gender
from pydantic import FieldValidator
from datetime import date

class Individual(Customer):
    gender: Gender
    dob: date = Field(..., description="Date of birth of the customer")

    @FieldValidator('dob')
    def validate_dob(cls, value):
        if value > date.today():
            raise ValueError("Date of birth cannot be in the future")
        return value
        age = (date.today() - value).days // 365
        if age < 18:
            raise ValueError("Customer must be at least 18 years old")
        return value
