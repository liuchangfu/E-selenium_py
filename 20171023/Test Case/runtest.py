# from count import Count
# import unittest
# import test_add
# import test_sub
#
# #构造测试集
# suite = unittest.TestSuite()
# #构造test_add测试集
# suite.addTest(test_add.TestCount("test_add1"))
# suite.addTest(test_add.TestCount("test_add2"))
# #构造test_sub测试集
# suite.addTest(test_sub.TestSub("test_sub1"))
# suite.addTest(test_sub.TestSub("test_sub2"))
#
# #执行测试
# if __name__ == "__main__":
#     runner = unittest.TextTestRunner()
#     runner.run(suite)

import unittest
import HTMLTestRunner
import time

#指定测试用例为当前文件夹下的Test Case目录
test_dir = "E:\\selenium_py\\20171023\\Test Case\\"
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__=="__main__":
    runner= unittest.TextTestRunner()
    runner.run(discover)
