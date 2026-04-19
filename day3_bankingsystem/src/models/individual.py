from datetime import date
from models.customer import Customer


class Individual(Customer):
    def __init__(
        self,
        accountNumber,
        name,
        address,
        contactNumber,
        email,
        password,
        surname,
        gender,
        dateOfBirth,
    ):
        super().__init__(accountNumber, name, address, contactNumber, email, password)
        self.__surname = surname
        self.__gender = gender
        self.__dateOfBirth = dateOfBirth

    @property
    def surname(self):
        return self.__surname

    # business method
    def workOutAge(self):
        return date.today().year - self.__dateOfBirth