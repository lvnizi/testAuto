# -*- coding: utf-8 -*-

import HTMLTestRunner
import unittest
import os,time


listaa = "D:\\gitworkspace\\testAuto\\test_case"
def createsuite1():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(listaa,pattern='test_*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
            #testunit.addTests(test_case)
            print(testunit)
    return testunit

#now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
filename="D:\\gitworkspace\\reports\\result.html"
fp=open(filename,'w',encoding='utf-8')

runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'薪酬系统测试报告',
    description=u'用例执行情况：')

runner.run(createsuite1())

#关闭文件流，不关的话生成的报告是空的
fp.close()
