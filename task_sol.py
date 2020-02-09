class Employee:
 raise_amount = 1.04
 no_emp = 0
 def __init__(self,first,last,pay):
 self.first = first
 self.last = last
 self.pay = pay
 #self.email = first + '.' + last + '@company.com'
 Employee.no_emp +=1
 def fullname(self):
 return '{}{}'.format(self.first,self.last)
 def apply_raise(self):
 self.pay = int(self.pay * self.raise_amount)
 @classmethod
 def set_raise_amount(cls,amount):
 cls.raise_amount = amount
 @classmethod
 def from_string(cls, emp_str):
 first, last, pay = emp_str.split('-')
 return cls(first,last,pay)
 @staticmethod
 def is_workday(day):
 if day.weekday() ==5 or day.weekday() == 6:
 return False
 return True
 @property
 def email(self):
 return '{}.{}@email.com'.format(self.first,self.last)
class Developer(Employee):
 def __init__(self,first,last,pay,prog_lang):
 Employee.__init__(self, first, last, pay)
 self.prog_lang= prog_lang
 @property
 def email(self):
 return '{}.{}@email.com'.format(self.first,self.last)
class Manager (Employee):
 def __init__(self, first, last, pay, employees=None):
 Employee.__init__(self,first, last, pay)
 if employees is None:
 self.employees = []
 else:
 self.employees = employees
 def add_emp(self, emp):
 if emp not in self.employees:
 self.employees.append(emp)
 def remove_emp(self, emp):
 if emp in self.employees:
 self.employees.remove(emp)
 def print_emps(self):
 for emp in self.employees:
 print('-->', emp.fullname())
emp_2 = Employee('John', 'Doe', 12000)
emp_1 = Employee('abdul','Khan',20000)
mgr_1 = Manager('haris','khan',25000,[emp_2])