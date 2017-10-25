import unittest
from  count import Count

class TestCount(unittest.TestCase):
    def setUp(self):
        print("Test TestCount!!!")

    def test_add1(self):
        j = Count(2,3)
        add = j.add()
        self.assertEqual(add,5)

    def test_add2(self):
        j = Count(2.0,3.0)
        add = j.add()
        self.assertEqual(add,5)

    def tearDown(self):
        print("Test end TestCount!!")

if __name__ == "__main__":
    unittest.main()
