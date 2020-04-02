# -- coding: utf-8 --
import os
import unittest
#存放报告的位置
report_dir='./test_report'

class readLastestRp():
    def Latest_Report(report_dir):
        #os.listdir()方法用于返回指定文件夹包含文件或文件名字列表
        lists=os.listdir(report_dir)
        #按照时间顺序对该目录文件夹下面的文件进行排序
        lists.sort(key=lambda fn:os.path.getatime(report_dir+'\\'+fn))
        file=os.path.join(report_dir,lists[-1])
        print("\033[1;33;0mreturn new file is%r\033[0m"%file)
        return  file
