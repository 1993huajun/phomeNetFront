# -- coding: utf-8 --
import time
import unittest
from BSTestRunner import BSTestRunner

from testCase.model import sendSmtpEmail, readLastestRp

if __name__ == '__main__':
    test_dir = "./testCase/action/"
    report_dir = "./test_report/"
    # 指定执行test_01login.py文件，test_01login.py主要是调用具体的函数执行测试用例
    '''注意：若需要调用该方法时，需要将所有action里面的login()方法注释掉，仅保留第一个执行的'''
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")

    # 创建文件
    now = time.strftime("%y-%m-%d %H_%M_%S")
    report_name = report_dir + now + "_result.html"
    print("Start writting report...")
    with open(report_name, 'wb') as f:#w：写；b:二进制打开文件
        runner = BSTestRunner(stream=f, title="Test Report", description="帝国CMS普通会员前台UI自动化测试报告")
        runner.run(discover)
    f.close()


