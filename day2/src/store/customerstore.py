#generate 100 customer
import faker
import typing
from models.customer import Customer
class CustomerStore:
    def __init__(self,num_customers: int):
        self.customers: list[Customer] = []
        self.generate_customer(num_customers)

    def generate_customer(self,num_customers: int):
        fake = faker.Faker()
        for _ in range(num_customers):
            name = fake.name()
            email = fake.email()
            dob = fake.date_of_birth()
            customer = Customer(name,email,dob)
            self.customers.append(customer)
        return self.customers
    def get_customers(self)-> list[Customer]:
        return self.customers