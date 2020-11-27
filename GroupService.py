class GroupService:

    @staticmethod
    def add_to_group(group, student):
        group.get_students().append(student)
        student.get_classes().append(group)

    @staticmethod
    def add_to_group_professor(group, professor):
        group.set_professor(professor)
        professor.get_classes().append(group)