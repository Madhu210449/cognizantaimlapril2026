import sys
import os
from faker import Faker

#add project root to python path

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..','..')
)
sys.path.insert(0, project_root)
from src.configurations.conf import Config
from src.dataloaders.customer_csv_data_loader import CustomerCSVDataLoader 
from src.dataloaders.customer_json_data_loader import CustomerJSONDataLoader
from src.dataloaders.customer_txt_data_loader import CustomerTXTDataLoader
from src.stores.customer_store_impl import CustomerStoreImpl
from src.utils.pipeline_runner import PipelineRunner

def load_customers(**kwargs):
    config = Config()
    env=config.app_env
    print(f"Loading customers for environment: {env}")
    customers_store = kwargs['customer_store']
    if env == "Development":
        data_loader = CustomerCSVDataLoader()
        data_loader.load_data(config.resource_path, customers_store)
    if env == "Production":
        data_loader = CustomerJSONDataLoader()
        data_loader.load_data(config.resource_path, customers_store)
    if env == "Testing":
        data_loader = CustomerTXTDataLoader()
        data_loader.load_data(config.resource_path, customers_store)
    return customers_store

def update_customer(**kwargs):
    customer_store = kwargs['customer_store']
    customer_id = kwargs['customer_id']
    customer = customer_store.get_customer(customer_id)
    faker = Faker()
    customer.full_name.first_name = faker.first_name()
    customer.full_name.last_name = faker.last_name()
    customer.email = faker.email()
    customer.phone_no = faker.random_number(digits=10, fix_len=True)
    customer_store.update_customer(customer, customer_id)
    return customer_store

def get_customer_by_id(**kwargs):
    customer_store = kwargs['customer_store']
    customer_id = kwargs['customer_id']
    customer = customer_store.get_customer(customer_id)
    print(f"Customer_id: {customer.customer_id}")
    print(f"Name: {customer.full_name.first_name} {customer.full_name.last_name}")
    print(f"Email: {customer.email}")
    print(f"Phone: {customer.phone_no}")
    print("-----------------------------")

def display_customers(**kwargs):    
    customers_store = kwargs['customer_store']
    for customer in customers_store.get_all_customers():
        print(f"Customer_id: {customer.customer_id}")
        print(f"Name: {customer.full_name.first_name} {customer.full_name.last_name}")
        print(f"Email: {customer.email}")
        print(f"Phone: {customer.phone_no}")
        print("-----------------------------")

def delete_customer(**kwargs):
    customer_store = kwargs['customer_store']
    customer_id = kwargs['customer_id']
    customer_store.delete_customer(customer_id)
    print(f"Customer with id {customer_id} deleted successfully.")



if __name__ == "__main__":
    customer_store = CustomerStoreImpl()
    pipeline_runner = PipelineRunner()
    pipeline_runner.add_stage(load_customers)
    pipeline_runner.add_stage(display_customers)
    pipeline_runner.add_stage(update_customer)
    pipeline_runner.add_stage(get_customer_by_id)
    pipeline_runner.add_stage(delete_customer)
    pipeline_runner.run(customer_store=customer_store, customer_id=1)