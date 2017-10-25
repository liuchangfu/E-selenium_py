import unittest

class Test(unittest.TestCase):
    def setUp(self):
        number=input("Input your number:")
        self.number = int(number)

    def test_case(self):
        self.assertEqual(self.number,10,msg="You input is not 18")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()