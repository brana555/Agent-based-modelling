###Agent Based Model for COMP6216 Coursework 2###
#Brijee Rana
#br1e21
#33385874

import matplotlib.pyplot as plt

import Classes
from Classes import Model

#Parameters
a = 0.5 #cost of effort           
H = 1 #contribution of hard workers to group effort
L = 0 #contribution of lzy workers to group effort
n = 5 #group size
N = 100 #population of students

num_courses= 20

xh = 0.5 #inital concentration of H
num_h = int(N*xh) # initial composition of the population
num_l = N - num_h

model = Model(N)
model.init_students(num_h, num_l)
groups = model.group(n)
hard_students = [num_h]
lazy_students = [num_l]

for i in range(num_courses):
    # random grouping
    groups = model.group(n)
    for group in groups:
        group.set_mark()
    model.imitate_strategy()
    hard_students.append(model.student_composition[0])
    lazy_students.append(model.student_composition[1])

time = list(range(num_courses + 1))
plt.figure()
plt.grid()
plt.plot(time, hard_students, label="Hard students")
plt.plot(time, lazy_students, label="Lazy students")
plt.xlabel("Number of courses")
plt.ylabel("Composition of population")
plt.title("N={}, n={}, H={}, L={}, a={}".format(N, n, H, L, a))
plt.legend()
plt.show()

