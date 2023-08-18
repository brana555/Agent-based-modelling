import random
import math
from enum import Enum

#Parameters
a = 0.5 #cost of effort           
H = 1 #contribution of hard workers to group effort
L = 0 #contribution of lzy workers to group effort
n = 5 #group size
N = 100 #population of students


class StudentStrategy(Enum):
    H = 1
    L = 0


class Student:
    def __init__(self, student_strategy: int) -> None:
        self.student_strategy = student_strategy
        self._mark = 0

    @property
    def mark(self) -> int:
        return self._mark

    @mark.setter
    def mark(self, m):
        self._mark = m

    @property
    def measure(self): 
        return self.mark - a * float(self.student_strategy)

    def imitate_strategy(self, reference_student) -> None:
        if self.measure >= reference_student.measure:
            return None

        difference = reference_student.measure - self.measure
        random_number = random.uniform(0, H)
        if random_number <= difference:
            self.student_strategy = reference_student.student_strategy


class Group:
    def __init__(self, size: int) -> None:
        self.size = size
        self.__students = list()
        self.hard_students_number = 0
        self.lazy_students_number = 0

    @property
    def students(self):
        return self.__students

    @property
    def effort(self):
        return H * self.hard_students_number + L * self.lazy_students_number

    def set_mark(self):
        mark = self.effort / self.size
        for student in self.students:
            student.mark = mark

    def add_students(self, student: Student) -> None:
        if len(self.__students) >= self.size:
            raise Exception("Students is enough")
        self.__students.append(student)
        if student.student_strategy == H:
            self.hard_students_number += 1
        else:
            self.lazy_students_number += 1

    def __str__(self):
        return "hard_students_number: {},\tlazy_students_number: {}".format(self.hard_students_number, self.lazy_students_number)


class Model:
    def __init__(self, N: int):
        self.N = N
        self.students = []

    @property
    def student_composition(self) -> list:
        if not self.students:
            return [1, 1]
        res = [0, 0]
        for student in self.students:
            if student.student_strategy == H:
                res[0] += 1
            else:
                res[1] += 1
        return res

    def init_students(self, hard_number: int, lazy_number: int):
        for _ in range(hard_number):
            self.students.append(Student(H))
        for _ in range(lazy_number):
            self.students.append(Student(L))

    def group(self, size):
        group_number = math.ceil(N / size)
        random.shuffle(self.students)
        groups = []
        i = 0
        for _ in range(group_number):
            g = Group(size)
            for _ in range(size):
                if i <= len(self.students) - 1:
                    g.add_students(self.students[i])
                    i += 1
            groups.append(g)
        return groups

    def imitate_strategy(self):
        for student in self.students:
            new_students = self.students[::]
            new_students.remove(student)
            rand_n = random.randint(1, self.N - 1)
            try:
                student.imitate_strategy(new_students[rand_n - 1])
            except Exception:
                print(rand_n, len(new_students))
        
        

    