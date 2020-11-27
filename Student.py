from Group import Group
from Person import Person
from GroupService import GroupService


class Student(Person):
    def __init__(self, first_name, last_name, email, major, standing):
        super().__init__(first_name, last_name, email)
        self.set_major(major)
        self.set_standing(standing)
        self.__classes = []

    def get_classes(self):
        return self.__classes

    def get_major(self):
        return self.__major

    def set_major(self, major):
        self.__major = major

    def get_standing(self):
        return self.__standing

    def set_standing(self, standing):
        self.__standing = standing

    def add_class(self, group):
        GroupService.add_to_group(group, self)

    def print_classes(self):
        for group in self.__classes:
            print(group.get_title())
