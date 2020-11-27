import re
import sys

from GroupService import GroupService


class Group:
    classPattern = re.compile('^[A-Z]([a-z]{2,3})+[0-9]{3}$')

    def __init__(self, title, credit, professor=None):
        self.set_title(title)
        self.set_credits(credit)
        self.__professor = professor
        self.__students = []

    def get_professor(self):
        return self.__professor

    def set_professor(self, professor):
        self.__professor = professor

    def get_title(self):
        return self.__title

    def set_title(self, title):
        if self.classPattern.search(title):
            self.__title = title
        else:
            self.__title = "No_title"

    def set_credits(self, credit):
        if credit == 3 or credit == 4:
            self.__credit = credit
        else:
            self.__credit = 0

    def get_credits(self):
        return self.__credit

    def add_student(self, student):
        GroupService.add_to_group(self, student)

    def add_professor(self, professor):
        GroupService.add_to_group_professor(self, professor)

    def get_students(self):
        return self.__students

    def list_all_students(self):
        for student in self.get_students():
            print("{}, {}".format(student.get_first(),
                                  student.get_last()))
