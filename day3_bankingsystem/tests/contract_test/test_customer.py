from models.customer import Customer


def test_customer_count():
    initial = Customer.get_total_customers()

    Customer("101", "John", "Addr", "999", "a@b.com", "pass")
    Customer("102", "Jane", "Addr", "888", "c@d.com", "pass")

    assert Customer.get_total_customers() == initial + 2