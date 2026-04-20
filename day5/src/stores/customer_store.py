#create customer class with abstract classfrom abc import ABC, abstractmethod
from abc import ABC, abstractmethod
class Customer(ABC):
    @abstractmethod
    def add_customer(self,customer):
        pass

    @abstractmethod
    def get_customer(self,customer_id):
        pass

    @abstractmethod
    def update_customer(self,customer,customer_id):
        pass

    @abstractmethod
    def delete_customer(self,customer_id):
        pass