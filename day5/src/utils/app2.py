import sys
import os
from faker import Faker

#add project root to python path

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..','..')
)
sys.path.insert(0, project_root)
from src.configurations.conf import Config
from src.dataloaders.customer_json_data_loader import CustomerJSONDataLoader
from src.stores.customer_store_impl import CustomerStoreImpl
def display_customers(customers_store):
    config = Config()
    env=config.app_env
    if env == "Production":
        data_loader = CustomerJSONDataLoader()
        data_loader.load_data(config.resource_path, customers_store)
        customers = customers_store.get_all_customers()
        for customer in customer_store.get_all_customers():
            print(customer)
if __name__ == "__main__":
    customer_store = CustomerStoreImpl()
    display_customers(customer_store)