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

if __name__ =="__main__":
    unittest.main()

# # 构造测试集
# suite = unittest.TestSuite()
# suite.addTest(TestCount("test_add1"))
# suite.addTest(TestCount("test_add2"))
# suite.addTest(TestSub("test_sub1"))
# suite.addTest(TestSub("test_sub2"))
# #执行测试
# runner = unittest.TextTestRunner()
# runner.run(suite)
