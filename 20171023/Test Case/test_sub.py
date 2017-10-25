import unittest
from  count import Count

class TestSub(unittest.TestCase):
    def setUp(self):
        print("Test TestSub!")

    def test_sub1(self):
        k = Count(5.0,3.0)
        sub = k.sub()
        self.assertEqual(sub,2.0)

    def test_sub2(self):
        k = Count(5, 3)
        sub = k.sub()
        self.assertEqual(sub, 2)

    def tearDown(self):
        print("Test end TestSub!!!")

if __name__ == "__main__":
    unittest.main()