#!/usr/bin/python

import unittest

class TestIMC(unittest.TestCase):


	def test_calculate(self):
		test_imc = IMC(101,1.81)
		result = test_imc.calculate()
		self.assertEqual(test_imc.weight/test_imc.height,result)


class IMC:

	def __init__(self, weight, height):
		self.weight = weight
		self.height = height

	def calculate(self):
		return self.weight / self.height



if __name__ == '__main__':
	unittest.main()