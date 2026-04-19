from typing import List
from models.transaction import Transaction


class Account:
    def __init__(self, runningTotals: float, openDate: str):
        self.__runningTotals = runningTotals
        self.__openDate = openDate
        self.__transactions: List[Transaction] = []

    # getters / setters
    @property
    def running_totals(self):
        return self.__runningTotals

    @running_totals.setter
    def running_totals(self, value):
        self.__runningTotals = value

    @property
    def open_date(self):
        return self.__openDate

    @property
    def transactions(self):
        return self.__transactions

    # business method
    def showCustomerTransactions(self) -> None:
        for txn in self.__transactions:
            print(txn.amount, txn.sender, txn.receiver)

    # association helper
    def add_transaction(self, transaction: Transaction) -> None:
        self.__transactions.append(transaction)