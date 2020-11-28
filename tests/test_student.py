from unittest import TestCase

from Group import Group
from Student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.obj = Student("Johan", "Muco", "jmm170@aubg.edu", "Computer Science", "Senior")
        self.class_obj = Group("Cos101", 3)

    def test_setMajor_match(self):
        self.assertEqual(self.obj.get_major(), "Computer Science")
        self.obj.set_major("Journalism")
        self.assertEqual(self.obj.get_major(), "Journalism")

    def test_setMajor_noMatch(self):
        self.assertEqual(self.obj.get_major(), "Computer Science")
        self.obj.set_major("333")
        self.assertEqual(self.obj.get_major(), "No_major")

    def test_setStanding_match(self):
        self.assertEqual(self.obj.get_standing(), "Senior")
        self.obj.set_standing("Freshman")
        self.assertEqual(self.obj.get_standing(), "Freshman")

    def test_setStanding_noMatch(self):
        self.assertEqual(self.obj.get_standing(), "Senior")
        self.obj.set_standing("444")
        self.assertEqual(self.obj.get_standing(), "No_standing")

    def test_add_class_failure(self):
        self.assertEqual(self.obj.add_class(self.obj), "Object needs to be of Group type")

    def test_get_classes_success(self):
        self.obj.add_class(self.class_obj)
        self.assertEqual(self.obj.get_classes(), [self.class_obj])

    def test_get_classes_empty(self):
        self.assertEqual(self.obj.get_classes(), [])