#create corporate class inherit from customer using pydantic
from src.models.company_type import CompanyType
from src.models.customer import Customer
from pydantic import Field
class Corporate(Customer):
    company_type: CompanyType
    registration_number: str = Field(..., description="Registration number of the company")
    