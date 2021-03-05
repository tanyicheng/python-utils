class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    # def get_salary(self):
    #     return self.__salary
    #
    # def set_salary(self,salary):
    #     if 1000<salary<50000:
    #         self.__salary=salary
    #     else:
    #         print('金额只能在1000到5w之间')

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print('金额只能在1000到5w之间')


emp = Employee("barrett", 30000)

# print(emp.get_salary())
# emp.set_salary(100)
# print(emp.get_salary())


print(emp.salary)
emp.salary = -2500
print(emp.salary)
