#!/usr/bin/python

import unittest

class TestStudent(unittest.TestCase):

	def test_average(self):
		test_std = Student("Test",16)
		grade1 = test_std.add_grade(4.5)
		grade2 = test_std.add_grade(5.0)
		average = test_std.calculate_average()
		self.assertEqual(4.75,average)


class Student(object):
	
	grades = []

	def __init__(self,name,age):
		self.name = name
		self.age = age

	def add_grade(self,grade):
		self.grade = grade
		Student.grades.append(grade)

	def calculate_average(self):
		return sum(Student.grades) / len(Student.grades)


if __name__ == '__main__':
	unittest.main()

		



