import datetime

class Employee:
    no_of_employee= 0
    raise_amt = 1.04;
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.' + last + '@Company'
        Employee.no_of_employee +=1
    

    def araise(self):
        self.pay = int(self.pay * self.raise_amt)   

    @ classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def eday (emp_day):
        print('NON WORKING DAY! a.k.a. HOLIDAY!!!') if(emp_day.weekday() == 5 or emp_day.weekday() == 6) else  print('WORKING DAY!')
            # print('NON WORKING DAY! a.k.a. HOLIDAY!!!')
            # return False
        # print('WORKING DAY!')
        # return True 

    @property
    def email(self):
        return '{}{}@gmail.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.deleter
    def fullname(self):
        print('DELETED FULL NAME!')
        self.first = None
        self.last = None

    pass
class Developer(Employee):
    raise_amt = 2
    def __init__(self,first,last,pay,prog_lang1,prog_lang2):
        Employee.__init__(self,first,last,pay)
        self.prog_lang1 = prog_lang1
        self.prog_lang2 = prog_lang2


emp_1 = Employee('some','one',500000)
# emp_2 = Employee('Haris','Khan',70000)
# emp_3 = Employee('Jhon','Doe',20000)
# emp_str_1 = 'Tony-Stark-10000'
# emp_4 = Employee.from_string(emp_str_1)
# dev_1 = Developer('kazim','sayed',100000,'KOTLIN','C++')
# dev_2 = Developer('Tauseef','Shaikh',50000,'SWIFT','C++')

# print('EMAIL: ')
# print(emp_1.email)
# print(emp_2.email)
# print(emp_3.email)
# print(emp_4.email)
# print(dev_1.email)
# print(dev_2.email)

# print('FULL NAME')
# print(emp_1.first + ' ' + emp_1.last)
# print(emp_2.first + ' ' + emp_2.last)

# print('FULL NAME USING A FUNCTION: ')
# print(emp_1.fullname())
# print(emp_2.fullname())

# print(Employee.fullname(emp_1))
# print(Employee.fullname(emp_2))
# print(Employee.fullname(emp_3))
# print(Employee.fullname(emp_4))
# print(Developer.fullname(dev_1))
# print(Developer.fullname(dev_2))

print('PAYMENT')
print(emp_1.pay)
# print(emp_2.pay)
# print(emp_3.pay)
# print(emp_4.pay)
# print(dev_1.pay)
# print(dev_2.pay)

# print("RAISE")
# emp_1.araise()
# print(emp_1.pay)
# emp_2.araise()
# print(emp_2.pay)
# emp_3.araise()
# print(emp_2.pay)
#emp_4.araise()
#print(emp_4.pay)
# dev_1.araise()
# print(dev_1.pay)
# dev_2.araise()
# print(dev_2.pay)
# 
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
# 
# Employee.raise_amt = 2
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
#
# print(emp_1.__dict__)
# print(Employee.__dict__)
#
print("NO. OF EMPLOYEES: " + str(Employee.no_of_employee))
#print(Employee.no_of_employee)

my_date = datetime.date(2020,1,18)
d = Employee.eday(my_date)

print(emp_1.__dict__)
# print(emp_2.__dict__)
# print(emp_3.__dict__)
# print(emp_4.__dict__)
# print(dev_1.__dict__)
# print(dev_2.__dict__)

print(emp_1.fullname)
print(emp_1.email)
del emp_1.fullname
print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)
