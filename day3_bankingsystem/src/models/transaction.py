from datetime import datetime

class Transaction:
    def __init__(self, amount: float, sender : str, receiver : str):
        self.__amount = amount
        self.__sender = sender
        self.__receiver = receiver
        self.__timestamp = datetime.now()
    
    # Getters
    @property
    def amount(self) -> float:
        return self.__amount
    @property
    def sender(self) -> str:
        return self.__sender
    @property
    def receiver(self) -> str:
        return self.__receiver
    
    #business methods
    def depositMoney(self, amount: float):
        self.__amount += amount

    def withdrawMoney(self, amount: float):
        if self.__amount >= amount:
            self.__amount -= amount
        else:
            raise ValueError("Insufficient funds for withdrawal.")
    