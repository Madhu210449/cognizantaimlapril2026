#create customer data loader class to load customer data from csv file
from abc import ABC, abstractmethod
class CustomerDataLoader(ABC):
    @abstractmethod
    def load_data(self, file_path):
        pass
    