from models.account import Account


class SavingsAccount(Account):
    def __init__(self, runningTotals, openDate, interestRate):
        super().__init__(runningTotals, openDate)
        self.__interestRate = interestRate

    @property
    def interest_rate(self):
        return self.__interestRate

    @interest_rate.setter
    def interest_rate(self, value):
        self.__interestRate = value