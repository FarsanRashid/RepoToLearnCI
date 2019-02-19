import unittest
import math_class

class TestStringMethods(unittest.TestCase):
	def test_add(self):
		guru = math_class.math_guru()
		self.assertEqual(guru.add(1 , 2), 4)

if __name__ == '__main__':
	unittest.main()
