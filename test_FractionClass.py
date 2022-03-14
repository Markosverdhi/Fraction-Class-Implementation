import unittest
from FractionClass import Fraction

#Creates an instance to test
TesterFrac = Fraction(3,4)
class TestFractionClass(unittest.TestCase):

	def test_show(self):
		self.assertEqual(TesterFrac.__str__(), '3/4')
	def test__str__(self):
		self.assertEqual(TesterFrac.__str__(), '3/4')
	def test__eq__(self):
		self.assertTrue(TesterFrac.__eq__(Fraction(3,4)))
	def test__add__(self):
		self.assertEqual(TesterFrac.__add__(Fraction(1,5)), 19/20)
	def test_get_num(self):
		self.assertEqual(TesterFrac.get_num(), 3)
	def test_get_den(self):
		self.assertEqual(TesterFrac.get_den(), 4)
	def test__sub__(self):
		self.assertEqual(TesterFrac.__sub__(Fraction(1,4)),Fraction(1,2))
	def test__mul__(self):
		self.assertEqual(TesterFrac.__mul__(Fraction(1,2)),Fraction(3,8))
	def test__truediv__(self):
		self.assertEqual(TesterFrac.__truediv__(Fraction(1,2)),Fraction(3,2))
	def test__gt__(self):
		self.assertTrue(TesterFrac.__gt__(Fraction(1,5)))
	def test__ge__(self):
		self.assertTrue(TesterFrac.__ge__(Fraction(1,5)))
	def test__lt__(self):
		self.assertFalse(TesterFrac.__lt__(Fraction(1,5)))
	def test__le__(self):
		self.assertFalse(TesterFrac.__le__(Fraction(1,5)))
	def test__ne__(self):
		self.assertTrue(TesterFrac.__ne__(Fraction(1,5)))
	def test__radd__(self):
		self.assertEqual(TesterFrac.__add__(Fraction(1,5)),Fraction(19,20))
	def test__repr__(self):
		self.assertEqual(TesterFrac.__repr__(), "Fraction(3,4)")
	def test__iadd__(self):
		self.assertEqual(TesterFrac.__iadd__(Fraction(1,5), 'CompSci'), Fraction(19,20))

if __name__ == '__main__':
	unittest.main()
