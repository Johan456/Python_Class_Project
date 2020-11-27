import os
from Group import Group
from Professor import Professor
from Student import Student
import csv
import re


def read_classes_from_file():
    global title, group
    classes_dict = {}
    # fileInput = input("Enter the name of the file you want to read the classes info from:")
    # path = fileInput + ".csv"
    if os.path.isfile("classes_data.csv"):
        file = open("classes_data.csv")
        reader = csv.reader(file)
        for line in reader:
            title = str(line[0])
            credit = int(line[1])
            group = Group(title, credit)
            classes_dict[title] = group

    else:
        print('No such file!')

    return classes_dict


def read_students_from_file(classes_dict):
    global first, student
    students_dict = {}
    # fileInput = input("Enter the name of the file you want to read the student info from:")
    # path = fileInput + ".csv"
    file = open("student_data.csv")
    reader = csv.reader(file)
    if os.path.isfile("student_data.csv"):
        for line in reader:
            first = str(line[0])
            last = str(line[1])
            email = str(line[2])
            major = str(line[3])
            standing = str(line[4])
            classes = str(line[5]).split(sep="-")
            student = Student(first, last, email, major, standing)
            full_name = first + " " + last
            students_dict[full_name] = student
            for group2 in classes:
                for title1, group1 in classes_dict.items():
                    if group2 == title1:
                        student.add_class(group1)
                    else:
                        pass
    else:
        print('No such file!')

    return students_dict


def read_professors_from_file(classes_dict):
    all_teachers = []
    # fileInput = input("Enter the name of the file you want to read the professors info from:")
    # path = fileInput + ".csv"
    file = open("professor_data.csv")
    reader = csv.reader(file)
    if os.path.isfile("professor_data.csv"):
        for line in reader:
            first = str(line[0])
            last = str(line[1])
            email = str(line[2])
            wage = int(line[3])
            department = str(line[4])
            classes = str(line[5]).split(sep="-")
            professor = Professor(first, last, email, wage, department)
            all_teachers.append(professor)
            for group2 in classes:
                for title1, group1 in classes_dict.items():
                    if group2 == title1:
                        professor.add_class(group1)
                    else:
                        pass
    else:
        print('No such file!')

    return all_teachers


def search_students(students_dict):
    subs = input("Enter the full or part of the name of the student that you are searching for: ")
    result = {}
    input_list = []
    for first_name, student_obj in students_dict.items():
        input_list.append(student_obj.full_name)

    for name, student_obj in students_dict.items():
        if re.search(subs, name):
            result[name] = student_obj

    if len(result) > 1:
        counter = 0
        print("Here is the list of students that have {} in their names:".format(subs))
        for name in result:
            print("{}. {}".format(counter, name))
            counter += 1
    elif len(result) == 1:
        print("Here is the name of the student that matched the search:")
        print(list(result.keys())[0])
    else:
        print("There are no students with that name.")

    return result


def get_classes_of_students(students_dict):
    if len(students_dict) > 1:
        number = input("Press the number associated with each student if you'd like more information about them:")
        try:
            if 0 <= int(number) < len(students_dict):
                for index, key in enumerate(students_dict):
                    if index == int(number):
                        print("{}'s classes: ".format(key))
                        students_dict[key].print_classes()
        except IndexError:
            print(print("Please enter a valid value!"))
    else:
        toggle = True
        while toggle:
            answer = input("Would you like more information about this student? 0 - No | 1 - Yes ")
            try:
                if int(answer) == 1:
                    for name, st in students_dict.items():
                        print("{}'s classes: ".format(name))
                        st.print_classes()
                        toggle = False
                elif int(answer) == 0:
                    toggle = False
            except TypeError:
                print("Please enter a valid value!")


def main():
    # Reading the classes from the csv file and assigning the values to a dictionary
    # classes_dict = {"Title" = Group object}
    classes_dict = read_classes_from_file()

    # Reading the students from the csv file and assigning the values to a dictionary
    # students_dict = {"First Name" = Student Object}
    students_dict = read_students_from_file(classes_dict)

    # Reading the professors from the csv file and assigning them into the classes they are teaching
    professors = read_professors_from_file(classes_dict)

    toggle = True
    while toggle:
        print("------------------------------------------------------------")
        print("1 - List all the professors and the classes they're teaching")
        print("2 - List all the classes and the students enrolled in them")
        print("3 - Search students by their name/surname")
        print("4 - Exit")
        option = int(input("Choose an option: "))
        if option == 1:
            for prof in professors:
                print("---------------------")
                print(prof.get_first())
                prof.list_classes_teaching()
        elif option == 2:
            for title1, group1 in classes_dict.items():
                print(group1.get_title())
                group1.list_all_students()
        elif option == 3:
            result_dict = search_students(students_dict)
            toggle2 = True
            while toggle2:
                if not bool(result_dict):
                    toggle2 = False
                else:
                    get_classes_of_students(result_dict)
                    toggle2 = False
        elif option == 4:
            toggle = False


if __name__ == "__main__":
    main()
