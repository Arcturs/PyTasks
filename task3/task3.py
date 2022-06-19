from collections import defaultdict

expel_data = []
eps = 1e-08


class Student:
    def __init__(self, name, sex, average_point):
        self.name = name
        self.sex = sex
        self.average_point = average_point


def students_input(file_name):
    input_lines = []
    global expel_data
    with open(file_name) as f:
        for line in f:
            input_line = line.split(', ')
            if len(input_line) == 2:
                expel_data.append(int(input_line[0]))
                expel_data.append(abs(float(input_line[1])))
            else:
                input_lines.append(input_line)
    students_map = defaultdict(list)
    for array in input_lines:
        students_map[int(array[2])].append(Student(array[0], array[1], float(array[3].strip())))
    return students_map


def solution(students_map):
    new_students_map = defaultdict(list)
    for key in students_map.keys():
        new_students_map[key].append(expel_students(students_map[key]))
    return new_students_map


def expel_students(student_list):
    global expel_data
    student_list = sorted(student_list, key=lambda student: student.average_point)
    if len(student_list) <= expel_data[0]:
        return None
    else:
        past_element = student_list[0]
        if past_element.average_point >= expel_data[1]:
            return None
        same_points_amount = 1
        points_amount = 0
        start_el_index = 0
        for i in range(1, len(student_list)):
            if abs(student_list[i].average_point - past_element.average_point) <= eps:
                same_points_amount += 1
            else:
                points_amount += same_points_amount
                same_points_amount = 1
                past_element = student_list[i]
                if len(student_list) - points_amount < expel_data[0]:
                    return student_list[0:start_el_index]
                start_el_index = i
            if student_list[i].average_point >= expel_data[1]:
                return student_list[0:i]


def students_output(students_map):
    for key in students_map.keys():
        print(f'From year {key} were expelled:')
        for student_list in students_map[key]:
            if student_list is None or len(student_list) == 0:
                print('No students')
                break
            for value in student_list:
                print(f'Student {value.name} with average point {value.average_point}')


try:
    students_map = students_input(input())
    students_output(solution(students_map))
except Exception:
    print('Failed with exception')
