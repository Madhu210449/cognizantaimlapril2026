#create company type class using enum
from enum import Enum
class CompanyType(Enum):
    PUBLIC = "Public"
    PRIVATE = "Private"
    NON_PROFIT = "Non-Profit"