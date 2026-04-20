#create address class associate with customer class
from src.models.customer import Customer
from pydantic import BaseModel, Field
class Address(BaseModel):
    customer: Customer
    street: str = Field(..., min_length=2, max_length=100, description="Street address of the customer")
    city: str = Field(..., min_length=2, max_length=100, description="City of the customer")
    state: str = Field(..., min_length=2, max_length=100, description="State of the customer")
    zip_code: str = Field(..., min_length=5, max_length=10, description="Zip code of the customer")
    country: str = Field(..., min_length=2, max_length=100, description="Country of the customer")