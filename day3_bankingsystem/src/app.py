from stores.banking_store import BankingStore
from utils.menu import Menu
from models.individual import Individual
from models.savings_account import SavingsAccount
from models.transaction import Transaction


def main():
    store = BankingStore()
    menu = Menu(store)

    customer = Individual(
        "ACC101",
        "Ravi",
        "Kochi",
        "9999999999",
        "ravi@email.com",
        "pass123",
        "Kumar",
        "Male",
        1995,
    )

    account = SavingsAccount(5000.0, "2024-01-01", 3.5)
    transaction = Transaction(1000, "Ravi", "Shop")

    menu.addCustomer(customer)
    menu.openAccount(account)
    menu.initiateTransaction(account, transaction)

    account.showCustomerTransactions()
    print("Total customers:", customer.totalNumberOfCustomers())


if __name__ == "__main__":
    main()
