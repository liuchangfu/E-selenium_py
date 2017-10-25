import unittest

class Mytest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print("test aaa")
    @unittest.skipIf(3 > 2,"当条件为真时，跳过测试")
    def test_skip_if(self):
        print("test bbb")
    @unittest.skipUnless(3 > 2,"当条件为真时，执行测试")
    def test_skip_unless(self):
        print("test ccc")
    @unittest.expectedFailure
    def test_expetcted_failure(self):
        self.assertEqual(2,2)


if __name__ == "__main__":
    unittest.main()