"""
Name: Christian Fowler
sales_force.py

Problem: Creates Class 'Sales_Force'

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        data_list = open(file_name, 'r').readlines()
        self.sales_people.append(data_list)

    def quota_report(self, quota):
        sales_list = self.sales_people[0]
        output = []
        for section in sales_list:
            insert_list = []
            math_list = []
            sales_str = section.split(', ')
            sales_nums = sales_str[2].split()
            for sale in sales_nums:
                math_list.append(eval(sale))
            sales_total = sum(math_list)
            if sales_total >= quota:
                met_quota = True
            else:
                met_quota = False
            insert_list.append(sales_str[0])
            insert_list.append(sales_str[1])
            insert_list.append(sales_total)
            insert_list.append(met_quota)
            output.append(insert_list)
        return output

    def top_seller(self):
        raw_data = self.sales_people[0]
        temp_list = []
        math_list = []
        new_list = []
        sales_list = []
        output = []
        for section in raw_data:
            section = section.split(', ')
            sales_nums = section[2].split()
            temp_list.append(sales_nums)
            new_list.append(section[:2])
        for section in temp_list:
            insert_list = []
            for sale in section:
                insert_list.append(eval(sale))
            math_list.append(insert_list)
        for section in math_list:
            total = sum(section)
            sales_list.append(total)
        iter = 0
        for num in sales_list:
            new_list[iter].insert(2, num)
            iter += 1
        iter = 0
        top = max(sales_list)
        for num in sales_list:
            if num == top:
                output.append(new_list[iter])
            else:
                pass
            iter += 1
        return output

    def individual_sales(self, employee_id):
        split_list = []
        found = False
        iter = 1
        output = 0
        for section in self.sales_people[0]:
            section = section.split(', ')
            split_list.append(section)
        while iter <= len(split_list) and not found:
            for section in split_list:
                if section[0] == str(employee_id):
                    output = section
                    found = True
                else:
                    pass
            iter += 1
        if found:
            return output
        else:
            return None

    def get_sale_frequencies(self):
        raw_data = self.sales_people[0]
        sales_list = []
        count_list = []
        frequency_dict = {}
        for section in raw_data:
            section = section.split(', ')
            sales_nums = section[2].split()
            sales_list.append(sales_nums)
        for section in sales_list:
            for sale in section:
                num = eval(sale)
                num = int(num)
                count_list.append(num)
                count = count_list.count(num)
                frequency_dict[num] = count
        return frequency_dict


'''
NOTES:


I ran tests below because my test.py constantly threw an error
saying "no module named 'tests'"


My Pycharm also kept telling me that certain files are corrupted
and are unable to be used until I restart the application.

'''


'''

TESTS:

sales_force = SalesForce()

sales_list = sales_force.add_data('sales_data.txt')

quota_report = sales_force.quota_report(750)
print(quota_report)
quota_report = sales_force.quota_report(1200)
print(quota_report)
quota_report = sales_force.quota_report(2420)
print(quota_report)
quota_report = sales_force.quota_report(4855)
print(quota_report)

top_seller = sales_force.top_seller()
print(top_seller)

individual_sales = sales_force.individual_sales(123)
print(individual_sales)
individual_sales = sales_force.individual_sales(234)
print(individual_sales)
individual_sales = sales_force.individual_sales(345)
print(individual_sales)
individual_sales = sales_force.individual_sales(456)
print(individual_sales)
individual_sales = sales_force.individual_sales(567)
print(individual_sales)

get_sale_frequencies = sales_force.get_sale_frequencies()
print(get_sale_frequencies)

'''
