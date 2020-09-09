import unittest

def subtraction(n1,n2):
    return n1-n2


# DO NOT TOUCH THE BELOW CODE
class TestSubtraction(unittest.TestCase):

    def test_01(self):
        self.assertEqual(subtraction(20,5), 15)

    def test_02(self):
        self.assertEqual(subtraction(10,-5), 15)

    def test_03(self):
        self.assertEqual(subtraction(0,10), -10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
