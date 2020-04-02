# -- coding: utf-8 --
import os
from selenium import webdriver

class sreenshot():
    def insert_img(driver,filename):
        func_path = os.path.dirname(__file__)   # 获取当前脚本所在目录的绝对路径
        print(func_path)

        base_dir = os.path.dirname(func_path)   # 获取当前脚本的上一级目录的绝对路径
        print(base_dir)

        base_dir = str(base_dir)    # 以字符串方式来处理
        base_dir = base_dir.replace('\\','/')   # 将'\\'替换为'/'
        print(base_dir)
        base = base_dir.split("/testCase")[0]   # 将base_dir的绝对路径以"/Website"做拆分点形成列表，分为2个元素部分
        print(base)

        filepath = base+"/test_report/screenshot/"+filename   # filename以自定义名称作为参数
        print('这是截图保存路径：%s'%filepath)
        driver.get_screenshot_as_file(filepath) # 保存截图文件到指定的路径

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com")
    sreenshot.insert_img(driver,"111.png")
    driver.quit()