#design data validation for full name
from pydantic import BaseModel, Field
class FullName(BaseModel):
    first_name: str = Field(..., pattern=r'^[A-Za-z]+$', description="First name of the customer")
    last_name: str = Field(..., pattern=r'^[A-Za-z]+$', description="Last name of the customer")
