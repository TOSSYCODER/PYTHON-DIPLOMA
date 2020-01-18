# fn = input("ENTER FIRST NAME: ")
# ln = input("ENTER LAST NAME: ")
# ph = input("ENTER PHONE NO.: ")
# e = input("ENTER EMAIL ADRESS: ")
# 
# dict[emp] = {'first_name' : fn, 'last_name':ln, 'phone_no':ph, 'email':e}

class Employee:
    no_of_employee= 0
    raise_amt = 0.2;
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@Company'
        Employee.no_of_employee +=1
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def araise(self):
        self.pay = int(self.pay * self.raise_amt)   
        
    pass
emp_1 = Employee('tauseef','shaikh',200000)
emp_2 = Employee('savrae','awzdsav',6898726)

print('EMAIL')
print(emp_1.email)
print(emp_2.email)

# print('FULL NAME')
# print(emp_1.first + ' ' + emp_1.last)
# print(emp_2.first + ' ' + emp_2.last)

print('FULL NAME USING A FUNCTION')
# print(emp_1.fullname())
# print(emp_2.fullname())

print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))

print('PAYMENT')
print(emp_1.pay)
print(emp_2.pay)

print("RAISE")
emp_1.araise()
print(emp_1.pay)
emp_2.araise()
print(emp_2.pay)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

Employee.raise_amt = 2
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print(emp_1.__dict__)
print(Employee.__dict__)

print(Employee.no_of_employee)