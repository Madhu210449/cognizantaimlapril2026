from stores.banking_store import BankingStore
from models.transaction import Transaction
from models.account import Account
from models.customer import Customer


class Menu:
    """
    Menu handles user actions and delegates work to BankingStore.
    """

    def __init__(self, store: BankingStore):
        self.__store = store

    def addCustomer(self, customer: Customer) -> None:
        self.__store.add_customer(customer)

    def deleteCustomer(self, account_number: str) -> None:
        self.__store.delete_customer(account_number)

    def openAccount(self, account: Account) -> None:
        self.__store.open_account(account)

    def closeAccount(self, account: Account) -> None:
        self.__store.close_account(account)

    def initiateTransaction(self, account: Account, transaction: Transaction) -> None:
        self.__store.initiate_transaction(account, transaction)

    def editCustomerDetails(self):
        print("Editing customer details...")

    def login(self):
        print("Login successful")

    def logout(self):
        print("Logout successful")
