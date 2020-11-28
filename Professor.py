import re

from Person import Person
from GroupService import GroupService


class Professor(Person):
    departmentPattern = re.compile('^[A-Za-z_]+( [a-zA-Z0-9_]+)*$')

    def __init__(self, first_name, last_name, email, pay, department):
        super().__init__(first_name, last_name, email)
        self.set_pay(pay)
        self.__department = department
        self.__classes = []

    def get_pay(self):
        return self.__pay

    def set_pay(self, pay):
        if int(pay) > 0 and type(pay) == int:
            self.__pay = pay
        else:
            self.__pay = 10000

    def get_department(self):
        return self.__department

    def set_department(self, department):
        if self.departmentPattern.search(department):
            self.__department = department
        else:
            self.__department = "No_department"

    def get_classes(self):
        return self.__classes

    def add_class(self, group):
        GroupService.add_to_group_professor(group, self)

    def list_classes_teaching(self):
        for group in self.get_classes():
            print("Class title: {}, Cr: {}".format(group.get_title(),
                                                  group.get_credits()))
