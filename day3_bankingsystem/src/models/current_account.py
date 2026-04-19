from models.account import Account


class CurrentAccount(Account):
    def __init__(self, runningTotals, openDate, overdraftLimit):
        super().__init__(runningTotals, openDate)
        self.__overdraftLimit = overdraftLimit

    @property
    def overdraft_limit(self):
        return self.__overdraftLimit

    @overdraft_limit.setter
    def overdraft_limit(self, value):
        self.__overdraftLimit = value
