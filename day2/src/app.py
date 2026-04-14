# creating entry point for application
import faker
from store.customerstore import CustomerStore
from view.customerview import CustomerView

"""
  creating main entry point
"""


def check():
    """
    this function creates an instance of faker class and prints a fake name
    """
    customer_store = CustomerStore(num_customers = 100)
    customer_view = CustomerView(customer_store)
    customer_view.display_customers()
    


if __name__ == "__main__":
    check()
