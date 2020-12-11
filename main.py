# Course CS30
# Period: PM
# Date Created: December 11th, 2020
# Date Last Modified: December 11th, 2020
# Name: Teashen James

# Defining the Employee Class
class Employee:

    # Defining the values of each object, First, Last, and pay
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # Defining email as first.last@company.com
        self.email = first + '.' + last + '@company.com'
    # Creates function called full name to easily print the full name
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Teashen', 'James', 50000)
emp_2 = Employee('Test', 'User', 25000)

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())

class Goons(Employee):
    pass

goon_1 = Goons('Gruul', 'Ghoul', 'N/A')
goon_2 = Goons('Scroth', 'Ghool', 'N/A')