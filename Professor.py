from Person import Person
from GroupService import GroupService


class Professor(Person):

    def __init__(self, first_name, last_name, email, pay, department):
        super().__init__(first_name, last_name, email)
        self.__pay = pay
        self.__department = department
        self.__classes = []

    def get_pay(self):
        return self.__pay

    def get_department(self):
        return self.__department

    def get_classes(self):
        return self.__classes

    def add_class(self, group):
        GroupService.add_to_group_professor(group, self)

    def list_classes_teaching(self):
        for group in self.get_classes():
            print("Class title: {}, Cr: {}".format(group.get_title(),
                                                  group.get_credits()))
