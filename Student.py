import re

from Group import Group
from Person import Person
from GroupService import GroupService


class Student(Person):
    majorPattern = re.compile('^[A-Za-z_]+( [a-zA-Z0-9_]+)*$')
    standingPattern = re.compile('^[A-Z][a-z]+$')

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
        if self.majorPattern.search(major):
            self.__major = major
        else:
            self.__major = "No_major"

    def get_standing(self):
        return self.__standing

    def set_standing(self, standing):
        if self.standingPattern.search(standing):
            self.__standing = standing
        else:
            self.__standing = "No_standing"

    def add_class(self, group):
        if isinstance(group, Group):
            return GroupService.add_to_group(group, self)
        else:
            return "Object needs to be of Group type"

