from typing import List
from models.customer import Customer
from models.account import Account
from models.transaction import Transaction


class BankingStore:
    """
    BankingStore handles all core banking operations.
    """

    def __init__(self):
        self.__customers: List[Customer] = []
        self.__accounts: List[Account] = []
        self.__transactions: List[Transaction] = []

    # ---------- CUSTOMER OPERATIONS ----------

    def add_customer(self, customer: Customer) -> None:
        self.__customers.append(customer)

    def delete_customer(self, account_number: str) -> None:
        self.__customers = [
            c for c in self.__customers if c.account_number != account_number
        ]

    def get_customers(self) -> List[Customer]:
        return self.__customers

    # ---------- ACCOUNT OPERATIONS ----------

    def open_account(self, account: Account) -> None:
        self.__accounts.append(account)

    def close_account(self, account: Account) -> None:
        self.__accounts.remove(account)

    def get_accounts(self) -> List[Account]:
        return self.__accounts

    # ---------- TRANSACTION OPERATIONS ----------

    def initiate_transaction(self, account: Account, transaction: Transaction) -> None:
        account.add_transaction(transaction)
        self.__transactions.append(transaction)

    def get_transactions(self) -> List[Transaction]:
        return self.__transactions