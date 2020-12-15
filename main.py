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

# Defining the employe Variable Values
emp_1 = Employee('Teashen', 'James', 50000)
emp_2 = Employee('Test', 'User', 25000)
# Prininting the objects
print(emp_1)
print(emp_2)
# Printing the email of each object
print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())

# Creating the Child Class 'Goons'
class Goons(Employee):
    pass
# Defining the Goons, using the defined values in the Employees Class
goon_1 = Goons('Gruul', 'Ghoul', 'N/A')
goon_2 = Goons('Scront', 'Ghool', 'N/A')

print(goon_1.pay)
print(goon_2.first)
