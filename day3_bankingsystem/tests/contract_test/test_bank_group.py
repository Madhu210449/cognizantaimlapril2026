from models.abc_banking_group import ABCBankingGroup
from models.savings_account import SavingsAccount


def test_add_account_to_bank():
    bank = ABCBankingGroup()
    acc = SavingsAccount(1000, "2024-01-01", 4.5)

    bank.add_account(acc)
    assert len(bank.get_accounts()) == 1