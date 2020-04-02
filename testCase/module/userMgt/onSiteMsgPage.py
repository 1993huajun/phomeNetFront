# -- coding: utf-8 --
from testCase.common.commonPage import Common
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from testCase.module.userMgt.userMgtPage import userMgtPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class onSiteMsgPage(Common):
    #打开站内消息管理
    openOnsite_loc = (By.ID,"domenumsgid")
    openSendMsg_loc = (By.PARTIAL_LINK_TEXT,"发送消息")
    #发送消息
    title_loc = (By.NAME,"title")
    selFriend_loc = (By.PARTIAL_LINK_TEXT,"选择好友")
    fname_loc = (By.ID, "fname")
    fnameOp_loc = (By.XPATH, "//select[@id='fname']/option")
    textarea_loc = (By.ID,"textarea")
    #消息列表
    openMsgList_loc = (By.PARTIAL_LINK_TEXT, "消息列表")
    mid_loc = (By.NAME,"mid[]")
    titleText_loc = (By.XPATH,"//table[@class='tableborder'][2]/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[2]/a")
    senderText_loc = (By.XPATH, "//table[@class='tableborder'][2]/tbody/tr[2]/td[3]/div/a")
    reply_loc = (By.PARTIAL_LINK_TEXT,"回复")
    forward_loc = (By.PARTIAL_LINK_TEXT,"转发")
    chkall_loc = (By.NAME,"chkall")


    def type_openOnSite(self):
        try:
            print("\033[1;31;40m 打开站内消息 \033[0m")
            self.find_element(*self.openOnsite_loc).click()
        except BaseException as msg:
            print(msg)

    def type_sendMsg(self,row,text):
        try:
            self.find_element(*self.openSendMsg_loc).click()
            sleep(1)
            print("\033[1;35;0m 正在发送消息...\033[0m")
            self.type_getAccount()
            self.find_element(*self.title_loc).send_keys(self.randoma)#将随机数作为标题传入
            sleep(1)
            # 选择好友进行消息发送
            index_handle = self.driver.current_window_handle
            print("index_handle is:%r"%index_handle)
            self.find_element(*self.selFriend_loc).click()
            sleep(1)
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[1])
            print("handles is:%r"%handles)

            self.tempVar=text#将得到的好友账号传入tempVar
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.fnameOp_loc))
            tels = self.find_elements(*self.fnameOp_loc)
            lists = []
            for i in tels:
                lists.append(i.text)
            print("list is :%r" % lists)
            if text in lists:
                print("text in lists")
                sleep(0.5)
                select_ele = Select(self.find_element(*self.fname_loc))
                select_ele.select_by_index(row)  # 选中从excel随机得到的好友账号
            sleep(0.2)
            self.find_element(*self.submit_loc).click()

            sleep(1)
            self.driver.switch_to.window(self.index_handle)
            self.find_element(*self.textarea_loc).send_keys(self.randoma)
            sleep(1)
            self.find_element(*self.submit_loc).click()
            sleep(2)
        except BaseException as msg:
            print(msg)

    def type_openMsgList(self):
        try:
            print("\033[1;31;40m 打开消息列表管理页面 \033[0m")
            self.find_element(*self.openMsgList_loc).click()
            sleep(0.5)
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.senderText_loc))
            self.tempVar = self.find_element(*self.senderText_loc).text
            print("tempVar is:%s" % self.tempVar)
        except BaseException as msg:
            print(msg)
            self.driver.refresh()
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.senderText_loc))
            self.tempVar = self.find_element(*self.senderText_loc).text
            print("tempVar is:%s" % self.tempVar)

    def type_getMsgListCount(self):
        try:
            print("\033[1;35;0m 正在获取列表记录数...\033[0m")
            lists=self.find_elements(*self.mid_loc)
            return len(lists)
        except BaseException as msg:
            print(msg)

    #检查发送的消息是否在接收方的消息列表里面
    def type_checkMsgList(self,username):
        try:
            print("\033[1;35;0m 正在检查发送的消息是否出现在接收方消息列表上...\033[0m")
            po1=userMgtPage(self.driver)
            po1.type_sysExit()
            po1.login_action(username,"123456")
            sleep(0.5)
            po1.type_openVip()
            self.type_openOnSite()
            self.type_openMsgList()
            lists=[]
            tels=self.find_elements(*self.titleText_loc)
            print("tels is :%r"%tels)
            print("randma is :%d"%self.randoma)
            for i in tels:
                print("i.text is:%r"%i.text)
                lists.append(i.text)
            if str(self.randoma) in lists:
                print("发送成功")
                self.assertTip="发送成功"
            for i in range(3):
                self.type_sendMsg(0,'ghj')
            sleep(1)
            self.find_element(*self.chkall_loc).click()
            sleep(0.5)
            self.find_element(*self.submit2_loc).click()
            self.type_getAlert()
            return self.assertTip
        except BaseException as msg:
            print(msg)

    def type_catMsg(self):
        try:
            print("\033[1;35;0m 点击标题进入查看消息内容...\033[0m")
            self.find_element(*self.titleText_loc).click()
            sleep(1)
        except BaseException as msg:
            print(msg)

    def type_replyMsg(self):
        try:
            print("\033[1;35;0m 回复消息...\033[0m")
            self.find_element(*self.reply_loc).click()
            self.type_getAccount()
            self.find_element(*self.textarea_loc).clear()
            self.find_element(*self.textarea_loc).send_keys(self.randoma)
            self.find_element(*self.submit_loc).click()
        except BaseException as msg:
            print(msg)

    def type_back(self):
        try:
            print("\033[1;35;0m 返回到消息列表管理界面...\033[0m")
            self.type_catMsg()
            self.find_element(*self.back_loc).click()
        except BaseException as msg:
            print(msg)

    def type_forward(self):
        try:
            print("\033[1;35;0m 消息转发中...\033[0m")
            self.type_catMsg()
            self.find_element(*self.forward_loc).click()
            self.find_element(*self.selFriend_loc).click()
            sleep(2)
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[-1])
            print("handles is:%r" % handles)
            tuples = self.get_ranExcelText("friend.xlsx")
            row = tuples[0]
            text = tuples[1]
            self.tempVar = text  # 将得到的好友账号传入tempVar
            tels = self.find_elements(*self.fnameOp_loc)
            lists = []
            for i in tels:
                lists.append(i.text)
            print("list is :%r" % lists)
            if text in lists:
                print("text in lists")
                select_ele = Select(self.find_element(*self.fname_loc))
                select_ele.select_by_index(row)  # 选中从excel随机得到的好友账号
            self.find_element(*self.submit_loc).click()

            self.driver.switch_to.window(self.index_handle)
            self.find_element(*self.textarea_loc).clear()
            self.find_element(*self.textarea_loc).send_keys(self.tempVar)
            self.find_element(*self.submit_loc).click()

        except BaseException as msg:
            print(msg)

    def type_delMsg(self):
        try:
            print("\033[1;35;0m 正在删除消息...\033[0m")
            self.find_element(*self.del_loc).click()
            sleep(0.5)
            self.type_getAlert()
        except BaseException as msg:
            print(msg)

    def type_delMsgBatch(self):
        try:
            print("\033[1;35;0m 正在批量删除消息...\033[0m")
            self.find_element(*self.mid_loc).click()
            self.find_element(*self.submit2_loc).click()
            self.type_getAlert()
        except BaseException as msg:
            print(msg)