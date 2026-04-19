from models.transaction import Transaction


def test_transaction_deposit_and_withdraw():
    txn = Transaction(1000, "A", "B")

    txn.deposit_money(500)
    assert txn.get_amount() == 1500

    txn.withdraw_money(300)
    assert txn.get_amount() == 1200