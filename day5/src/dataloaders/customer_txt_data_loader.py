#create customer txt data loader class to load customer data from txt file
from src.models.customer import Customer
from src.models.full_name import FullName
from src.dataloaders.customer_data_loader import CustomerDataLoader

class CustomerTXTDataLoader(CustomerDataLoader):
    def load_data(self, file_path, customer_store):
        customers = []
        current_customer = {}
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    if key == 'customer_id' and current_customer:
                        customers.append(current_customer)
                        current_customer = {}
                    current_customer[key] = value
            if current_customer:
                customers.append(current_customer)
        
        for cust in customers:
            customer_id = int(cust['customer_id'])
            first_name = cust['first_name']
            last_name = cust['last_name']
            full_name = FullName(first_name=first_name, last_name=last_name)
            email = cust['email']
            phone_no = int(cust['phone_no'])
            customer = Customer(customer_id=customer_id, full_name=full_name, email=email, phone_no=phone_no)
            customer_store.add_customer(customer)