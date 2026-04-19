from models.customer import Customer


class Corporate(Customer):
    def __init__(
        self,
        accountNumber,
        name,
        address,
        contactNumber,
        email,
        password,
        companyType,
    ):
        super().__init__(accountNumber, name, address, contactNumber, email, password)
        self.__companyType = companyType

    @property
    def company_type(self):
        return self.__companyType
``