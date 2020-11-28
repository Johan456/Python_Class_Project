from unittest import TestCase
from Person import Person


class TestPerson(TestCase):
    def setUp(self):
        self.obj = Person("Johan", "Muco", "jmm170@aubg.edu")

    def test_setFirst_match(self):
        self.assertEqual(self.obj.get_first(), "Johan")
        self.obj.set_first("Jhn")
        self.assertEqual(self.obj.get_first(), "Jhn")

    def test_setFirst_noMatch(self):
        self.assertEqual(self.obj.get_first(), "Johan")
        self.obj.set_first("434")
        self.assertEqual(self.obj.get_first(), "No_first")

    def test_setLast_match(self):
        self.assertEqual(self.obj.get_last(), "Muco")
        self.obj.set_last("Mu")
        self.assertEqual(self.obj.get_last(), "Mu")

    def test_setLast_noMatch(self):
        self.assertEqual(self.obj.get_last(), "Muco")
        self.obj.set_last("111")
        self.assertEqual(self.obj.get_last(), "No_last")

    def test_setEmail_match(self):
        self.assertEqual(self.obj.get_email(), "jmm170@aubg.edu")
        self.obj.set_email("jmm@test.com")
        self.assertEqual(self.obj.get_email(), "jmm@test.com")

    def test_setEmail_noMatch(self):
        self.assertEqual(self.obj.get_email(), "jmm170@aubg.edu")
        self.obj.set_email(" ")
        self.assertEqual(self.obj.get_email(), "No_email")

    def test_fullName(self):
        self.assertEqual(self.obj.full_name, "Johan Muco")
