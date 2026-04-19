from src.models.transaction import Transaction

class DirectDebit(Transaction):
    def __init__(self, amount: float, sender: str, receiver: str, payment_date: str):
        super().__init__(amount, sender, receiver)
        self.__payment_date = payment_date

    # Getter for payment_date
    @property
    def payment_date(self) -> str:
        return self.__payment_date