from unittest import TestCase

from Group import Group
from Professor import Professor


class TestProfessor(TestCase):
    def setUp(self):
        self.obj = Professor("William", "Adams", "wmm200@aubg.edu", 65000, "Computer Science")
        self.class_obj = Group("Cos101", 3)

    def test_setDepartment_match(self):
        self.assertEqual(self.obj.get_department(), "Computer Science")
        self.obj.set_department("Cos")
        self.assertEqual(self.obj.get_department(), "Cos")

    def test_setDepartment_noMatch(self):
        self.assertEqual(self.obj.get_department(), "Computer Science")
        self.obj.set_department("434")
        self.assertEqual(self.obj.get_department(), "No_department")

    def test_setPay_success(self):
        self.assertEqual(self.obj.get_pay(), 65000)
        self.obj.set_pay(30000)
        self.assertEqual(self.obj.get_pay(), 30000)

    def test_setPay_fail(self):
        self.assertEqual(self.obj.get_pay(), 65000)
        self.obj.set_pay("30000")
        self.assertEqual(self.obj.get_pay(), 10000)