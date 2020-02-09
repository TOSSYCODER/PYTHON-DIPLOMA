class Employee:
    no_of_employee= 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.no_of_employee +=1
            

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)

    pass

class Developer(Employee):
    def __init__(self,first,last,pay,prog_lang1,prog_lang2):
        Employee.__init__(self,first,last,pay)
        self.prog_lang1 = prog_lang1
        self.prog_lang2 = prog_lang2

class Manager(Employee):
    def __init__(self,first,last,pay,n_emp = None):
        Employee.__init__(self,first,last,pay)
        if n_emp is None:
            self.n_emp = []
        else:
            self.n_emp = n_emp

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def add_emp(self, emp):
        if emp not in self.n_emp:
            self.n_emp.append(emp)

    def remove_emp(self, emp):
        if emp in self.n_emp:
            self.n_emp.remove(emp)

    def print_emps(self):
        for emp in self.n_emp:
            print('--->', emp.fullname())



emp_1 = Employee('some','one',500000)
emp_2 = Employee('any','one',600000)
dev_1 = Developer('Tauseef','Shaikh',50000,'SWIFT','C++')
man_1 = Manager('HARIS','KHAN',50000,int(Employee.no_of_employee))

print('EMPLOYEE: ')
print(emp_1.fullname)
print(emp_1.email)
print(emp_1.pay)
print(emp_1.__dict__)

print('DEVELOPER:')
print(dev_1.fullname)
print(dev_1.email)
print(dev_1.pay)
print(dev_1.__dict__)

print('MANAGER: ')
print(man_1.fullname)
print(man_1.email)
print(man_1.pay)
print(man_1.__dict__)
