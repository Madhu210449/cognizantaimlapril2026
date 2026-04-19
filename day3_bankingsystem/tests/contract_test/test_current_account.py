from models.current_account import CurrentAccount


def test_current_account_overdraft():
    acc = CurrentAccount(500, "2024-01-01", 2000)
    assert acc.overdraft_limit() == 2000

    acc.overdraft_limit(3000)
    assert acc.overdraft_limit() == 3000