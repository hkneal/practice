"""Practicing named tuples"""
from collections import namedtuple

num_of_records, Grades = int(input()), namedtuple("Grades", input().split())
total = 0

for _ in range(int(num_of_records)):
    new_grade = Grades(*input().split())
    total += int(new_grade.MARKS)

print(format(total / num_of_records, '.2f'))