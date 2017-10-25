import unittest
import HTMLTestRunner
import time

#指定测试用例为当前文件夹下的Test Case目录


if __name__=="__main__":
    test_dir = "E:\\selenium_py\\20171024\\"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="baidu*.py")
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    filename = test_dir+now+"_result.html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况')
    runner.run(discover)
    fp.close()