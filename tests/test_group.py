from unittest import TestCase

from Group import Group
from Professor import Professor


class TestGroup(TestCase):
    def setUp(self):
        self.class_obj = Group("Cos101", 3)
        self.professor_obj = Professor("William", "Adams", "wmm200@aubg.edu", 65000, "Computer Science")

    def test_setProfessor_success(self):
        self.class_obj.set_professor(self.professor_obj)
        self.assertEqual(self.class_obj.get_professor(), self.professor_obj)