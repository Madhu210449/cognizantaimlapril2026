class Customer:
    __totalCustomers = 0

    def __init__(
        self,
        accountNumber,
        name,
        address,
        contactNumber,
        email,
        password,
    ):
        self.__accountNumber = accountNumber
        self.__name = name
        self.__address = address
        self.__contactNumber = contactNumber
        self.__email = email
        self.__password = password
        Customer.__totalCustomers += 1

    # getters
    @property
    def account_number(self):
        return self.__accountNumber

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    # business method
    @classmethod
    def totalNumberOfCustomers(cls):
        return cls.__totalCustomers