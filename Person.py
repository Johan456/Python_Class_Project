import re


class Person:
    namePattern = re.compile('^[A-Z][a-z]+$')
    emailPattern = re.compile(r'^[a-zA-Z0-9]+@[a-zA-Z_]+\.[a-zA-Z]{2,3}$')

    def __init__(self, first_name='', last_name='', email=''):
        self.set_first(first_name)
        self.set_last(last_name)
        self.set_email(email)

    def get_first(self):
        return self.__first_name

    def get_last(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def set_first(self, first):
        if self.namePattern.search(first):
            self.__first_name = first
        else:
            self.__first_name = "No_first"

    def set_last(self, last):
        if self.namePattern.search(last):
            self.__last_name = last
        else:
            self.__last_name = "No_last"

    def set_email(self, email):
        if self.emailPattern.search(email):
            self.__email = email
        else:
            self.__email = "No_email"

    @property
    def full_name(self):
        return '{} {}'.format(self.get_first(), self.get_last())

    def info(self):
        print('Full Name: {}\nEmail: {}'.format(self.full_name, self.get_email()))
