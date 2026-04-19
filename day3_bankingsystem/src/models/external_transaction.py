from models.transaction import Transaction


class ExternalTransaction(Transaction):
    def __init__(
        self,
        amount,
        sender,
        receiver,
        branchName,
        branchAddress,
        branchPostCode,
        branchCode,
    ):
        super().__init__(amount, sender, receiver)
        self.__branchName = branchName
        self.__branchAddress = branchAddress
        self.__branchPostCode = branchPostCode
        self.__branchCode = branchCode

    @property
    def branch_name(self):
        return self.__branchName