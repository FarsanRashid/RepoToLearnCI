import unittest
import math_class

class TestStringMethods(unittest.TestCase):
	def test_add(self):
		guru = math_class.math_guru()
		self.assertEqual(guru.add(1 , 2), 3)
	def test_sub(self):
		guru = math_class.math_guru()
		self.assertEqual(guru.subtract(2 , 1), 1)
	def test_echo(self):
		guru = math_class.math_guru()
		self.assertEqual(guru.echo_name(), "math_guru")

if __name__ == '__main__':
	unittest.main()
