"""
Name: Christian Fowler
sales_person.py

Problem: Creates Class 'Sales_Person'

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total_sales = sum(self.sales)
        return total_sales

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if sum(self.sales) >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if self.total_sales() < other.total_sales():
            return -1
        elif self.total_sales() > other.total_sales():
            return 1
        elif self.total_sales() == other.total_sales():
            return 0

    def __str__(self):
        return self.employee_id + '-' + self.name() + ': ' + self.total_sales
