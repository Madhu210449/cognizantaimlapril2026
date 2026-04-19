from models.savings_account import SavingsAccount


def test_savings_account_interest_rate():
    acc = SavingsAccount(1000, "2024-01-01", 4.5)
    assert acc.get_interest_rate() == 4.5

    acc.set_interest_rate(5.0)
    assert acc.get_interest_rate() == 5.0