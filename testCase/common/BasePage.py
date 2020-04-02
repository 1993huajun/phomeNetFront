#获取时间函数
from time import sleep

'''创建页面基础类'''
class BasePage():

    u_para = ""
    u_para1 = "/index.do"#保持子页面不变

    # 初始化
    def __init__(self,driver):
       self.base_url = "http://localhost"
       self.driver = driver
       self.index_handle = self.driver.current_window_handle
       self.timeout = 10

    # 定义打开不同的子页面方法
    # 下划线开头的_open()方法代表私有方法，不可直接调用，防止被随意修改
    def _open(self,u_para):
        url = self.base_url+u_para
        print("Test page is: %s" %url)
        self.driver.maximize_window()
        self.driver.get(url)
        sleep(1)
        # assert self.driver.current_url==url,"Did not land on %s" %url

    def _openNew(self,newurl):
        self.driver.maximize_window()
        self.driver.get(newurl)
        sleep(1)

    # 定义公开的open()方法，实现调用_pen(u_Para)方法
    def open(self):
        self._open(self.u_para)
    #因为页面里面涉及多个页面，需要对url重新定位，否则无法找到路径和元素
    def open_newUrl(self,newurl):
        self._openNew(newurl)

    '''封装元素定位的方法，注意这里使用到了通配符'''
    def find_element(self,*loc): # 定位的方式、定位的属性可变化
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def find_eleText(self,*loc):
        try:
            sleep(2)
            text= self.driver.find_element(*loc).text
            print("text is:%s" %text)
            return text
        except BaseException as msg:
            print(msg)
            return "notFound"





