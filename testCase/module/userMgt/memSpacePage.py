# -- coding: utf-8 --
from testCase.common.commonPage import Common
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from testCase.module.userMgt.onSiteMsgPage import onSiteMsgPage
from testCase.module.userMgt.userMgtPage import userMgtPage
from testCase.model.getuserInfo import getYaml
import random

class memSpacePage(Common):
    #公共
    memSpace_loc = (By.ID,"domenuspaceid")
    #打开某个模块
    previewSpaceMgt_loc = (By.PARTIAL_LINK_TEXT,"预览空间")
    setSpaceMgt_loc = (By.PARTIAL_LINK_TEXT,"设置空间")
    selTemplateMgt_loc = (By.PARTIAL_LINK_TEXT,"选择模板")
    mgbookMgt_loc = (By.PARTIAL_LINK_TEXT,"管理留言")
    feedbackMgt_loc = (By.PARTIAL_LINK_TEXT,"管理反馈")
    #预览空间
    spaceIndex_loc = (By.XPATH,"//font[@id='mhome']/strong")
    mod1_loc = (By.ID,"mod1")#新闻
    mod2_loc = (By.ID,"mod2")#软件
    mod3_loc = (By.ID,"mod3")#图片
    mod4_loc = (By.ID,"mod4")#flash
    mod7_loc = (By.ID,"mod7")#文章
    mod8_loc = (By.ID,"mod8")#分类信息
    muserinfo_loc = (By.ID,"muserinfo")#个人资料
    mgbook_loc = (By.ID,"mgbook")#留言板
    mfeedback_loc = (By.ID,"mfeedback")#反馈信息
    addNews_loc = (By.PARTIAL_LINK_TEXT,"增加新闻")
    addSoftware_loc = (By.PARTIAL_LINK_TEXT,"增加软件")
    addPic_loc = (By.PARTIAL_LINK_TEXT,"增加图片")
    addFlash_loc = (By.PARTIAL_LINK_TEXT,"增加FLASH")
    addArticle_loc = (By.PARTIAL_LINK_TEXT,"增加文章")
    addClassified_loc = (By.PARTIAL_LINK_TEXT,"增加分类信息")
    uname_loc = (By.NAME,"uname")
    isprivate_loc = (By.NAME,"isprivate")
    gbtext_loc = (By.NAME,"gbtext")
    eleText1_loc = (By.XPATH,"//table[@class='tableborder']/tbody/tr[2]/td")
    eleText2_loc = (By.XPATH, "//td[@valign='middle']/table/tbody/tr[1]/td[2]/font/strong")
    feedbackText_loc = (By.XPATH, "//b[contains(.,'在线反馈')]")
    name_loc = (By.NAME,"name")
    company_loc = (By.NAME,"company")
    email_loc = (By.NAME,"email")
    phone_loc = (By.NAME,"phone")
    fax_loc = (By.NAME,"fax")
    address_loc = (By.NAME,"address")
    zip_loc = (By.NAME,"zip")
    title_loc = (By.NAME,"title")
    ftext_loc = (By.NAME,"ftext")
    '''个人介绍包含在b标签里面，无法用PARTIAL_LINK_TEXT进行定位'''
    showUserInfo_loc = (By.XPATH,"//b[contains(.,'公司介绍')]")
    addMgbook_loc = (By.PARTIAL_LINK_TEXT,"管理留言")
    backToVip_loc = (By.PARTIAL_LINK_TEXT,"管理面板")
    #设置空间
    setSpaceText_loc = (By.XPATH, "//td[@height='25' and contains(.,'设置空间')]")
    spacename_loc = (By.NAME,"spacename")
    spacegg_loc = (By.NAME,"spacegg")
    #管理反馈
    feedbackMgtText_loc = (By.XPATH,"//table[@class='tableborder']/tbody/tr[2]/td[2]/div/a")
    feedbackMgtText1_loc = (By.XPATH, "//table[@class='tableborder']/tbody/tr[2]/td[2]/div/a[2]")
    checkTitle_loc = (By.XPATH,"//table[@class='tableborder']/tbody/tr[11]/td[2]")
    eleText3_loc = (By.XPATH, "//table[@class='tableborder']/tbody/tr")
    #管理留言
    messReply_loc = (By.PARTIAL_LINK_TEXT,"消息回复")
    selFriend_loc = (By.PARTIAL_LINK_TEXT, "选择好友")
    fname_loc = (By.ID, "fname")
    fnameOp_loc = (By.XPATH, "//select[@id='fname']/option")
    titleText_loc = (By.XPATH, "//table[@class='tableborder'][2]/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[2]/a")
    msgtext_loc = (By.NAME,"msgtext")
    reply_loc = (By.LINK_TEXT, "回复")
    retext_loc = (By.NAME,"retext")
    # replyText_loc = (By.XPATH,"//font[@color='#FF0000']")
    replyText_loc = (By.XPATH,"//table[@class='tableborder']/tbody/tr[2]/td[2]/table[2]/tbody/tr/td")
    eleText4_loc = (By.NAME,"gid[]")
    #选择模板
    selTemplate_loc = (By.XPATH,"//a[contains(.,'选定')]")

    '''打开某个页面'''
    def type_openMemSpace(self):
        try:
            print("\033[1;31;40m 展开会员空间 \033[0m")
            self.find_element(*self.memSpace_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openPreviewSpace(self):
        try:
            print("\033[1;31;40m 打开预览空间 \033[0m")
            sleep(1)
            self.find_element(*self.previewSpaceMgt_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openSetSpace(self):
        try:
            print("\033[1;31;40m 打开设置空间 \033[0m")
            self.find_element(*self.setSpaceMgt_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openSelTemplate(self):
        try:
            print("\033[1;31;40m 打开选择模板 \033[0m")
            self.find_element(*self.selTemplateMgt_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openMgbookMgt(self):
        try:
            print("\033[1;31;40m 打开留言管理 \033[0m")
            self.find_element(*self.mgbookMgt_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openFeedbackMgt(self):
        try:
            print("\033[1;31;40m 打开管理反馈 \033[0m")
            self.find_element(*self.feedbackMgt_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openNews(self):
        try:
            print("\033[1;31;40m 打开新闻 \033[0m")
            self.find_element(*self.mod1_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openSoftware(self):
        try:
            print("\033[1;31;40m 打开软件 \033[0m")
            self.find_element(*self.mod2_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openPic(self):
        try:
            print("\033[1;31;40m 打开图片 \033[0m")
            self.find_element(*self.mod3_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openFlash(self):
        try:
            print("\033[1;31;40m 打开Flash \033[0m")
            self.find_element(*self.mod4_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openArticle(self):
        try:
            print("\033[1;31;40m 打开文章 \033[0m")
            self.find_element(*self.mod7_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openClassified(self):
        try:
            print("\033[1;31;40m 打开分类信息 \033[0m")
            self.find_element(*self.mod8_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openUserInfo(self):
        try:
            print("\033[1;31;40m 打开个人资料 \033[0m")
            self.find_element(*self.muserinfo_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openMgbook(self):
        try:
            print("\033[1;31;40m 打开留言板 \033[0m")
            self.find_element(*self.mgbook_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openFeedback(self):
        try:
            print("\033[1;31;40m 打开反馈信息 \033[0m")
            self.find_element(*self.mfeedback_loc).click()
        except BaseException as msg:
            print(msg)

    def type_backTomemSpace(self):
        try:
            print("\033[1;31;40m 返回到会员中心 \033[0m")
            self.find_element(*self.backToVip_loc).click()
            self.type_openMemSpace()
        except BaseException as msg:
            print(msg)

    '''预览空间'''
    def type_addMgbook(self):
        try:
            print("\033[1;35;0m 正在新增留言...\033[0m")
            tuples=self.get_ranExcelText("friend.xlsx")
            row=tuples[0]
            self.tempVar=tuples[1]
            self.find_element(*self.uname_loc).clear()
            self.find_element(*self.uname_loc).send_keys(self.tempVar)
            self.find_element(*self.gbtext_loc).send_keys(self.tempVar)
            self.get_sreenshot().insert_img(self.driver,"memSpace_11addMgbook00.png")
            self.find_element(*self.submit_loc).click()
        except BaseException as msg:
            print(msg)

    def type_checkMgbookExist(self):
        try:
            print("\033[1;35;0m 正在检查留言是否发布成功...\033[0m")
            sleep(3)
            return self.find_eleText(*self.eleText1_loc)
        except BaseException as msg:
            print(msg)

    def type_addfeedback(self):
        try:
            print("\033[1;35;0m 正在新增反馈信息...\033[0m")
            self.type_getAccount()
            self.find_element(*self.name_loc).send_keys(self.randoma)
            self.find_element(*self.company_loc).send_keys(self.randoma)
            self.find_element(*self.email_loc).send_keys(self.randoma)
            self.find_element(*self.phone_loc).send_keys(self.randoma)
            self.find_element(*self.fax_loc).send_keys(self.randoma)
            self.find_element(*self.address_loc).send_keys(self.randoma)
            self.find_element(*self.zip_loc).send_keys(self.randoma)
            self.find_element(*self.title_loc).send_keys(self.randoma)
            self.find_element(*self.ftext_loc).send_keys(self.randoma)
            self.get_sreenshot().insert_img(self.driver,"memSpace_13addFeedback00.png")
            self.find_element(*self.submit_loc).click()
        except BaseException as msg:
            print(msg)

    def type_checkFeedbackExist(self):
        try:
            print("\033[1;35;0m 正在检查反馈是否新增成功...\033[0m")
            self.type_backTomemSpace()
            self.type_openFeedbackMgt()
            text = self.find_eleText(*self.feedbackMgtText_loc)
            return text
        except BaseException as msg:
            print(msg)


    '''设置空间'''
    def type_setSpace(self):
        try:
            print("\033[1;35;0m 正在设置空间信息...\033[0m")
            self.type_getAccount()
            self.find_element(*self.spacename_loc).clear()
            self.find_element(*self.spacename_loc).send_keys(self.randoma)
            self.find_element(*self.spacegg_loc).clear()
            self.find_element(*self.spacegg_loc).send_keys(self.randoma)
            self.find_element(*self.submit_loc).click()
            self.type_openPreviewSpace()
        except BaseException as msg:
            print(msg)

    def type_checkSpace(self):
        try:
            print("\033[1;35;0m 正在检查空间设置信息...\033[0m")
            return self.find_eleText(*self.eleText2_loc)
        except BaseException as msg:
            print(msg)

    '''管理反馈'''
    def type_checkTitle(self):
        try:
            print("\033[1;35;0m 正在检查title是否能够打开反馈的详情...\033[0m")
            self.find_element(*self.feedbackMgtText_loc).click()
            sleep(1)
            self.type_getLastHandle()
            text=self.find_eleText(*self.checkTitle_loc)
            self.get_sreenshot().insert_img(self.driver,"memSpace_14checkTitle01.png")
            self.type_closeHandle()
            return text
        except BaseException as msg:
            print(msg)

    def checkUser(self):
        try:
            print("\033[1;35;0m 正在检查user是否能够打开反馈的用户空间...\033[0m")
            self.find_element(*self.feedbackMgtText1_loc).click()
            sleep(1)
            self.type_getLastHandle()
            text = self.find_eleText(*self.showUserInfo_loc)
            self.get_sreenshot().insert_img(self.driver, "memSpace_15checkFbUser01.png")
            self.type_closeHandle()
            return text
        except BaseException as msg:
            print(msg)

    def type_delFeedback(self):
        try:
            print("\033[1;35;0m 正在删除反馈...\033[0m")
            self.find_element(*self.del_loc).click()
            sleep(1)
            self.type_getAlert()
            sleep(2)
        except BaseException as msg:
            print(msg)

    '''管理留言'''
    #选择好友进行消息回复
    def type_replyMgbookBySelFriend(self):
        try:
            print("\033[1;35;0m 正在选择好友进行消息回复...\033[0m")
            sleep(0.5)
            self.find_element(*self.messReply_loc).click()
            sleep(1)
            secHandle=self.type_getLastHandle()
            print("sechandle is :%r"%secHandle)
            self.type_getAccount()
            self.find_element(*self.title_loc).send_keys(self.randoma)  # 将随机数作为标题传入
            sleep(1)
            # 选择好友进行消息发送
            self.find_element(*self.selFriend_loc).click()
            sleep(1)
            thidHandle=self.type_getLastHandle()
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
            sleep(1)
            self.find_element(*self.submit_loc).click()
            print("sechandle is :%r" %secHandle)
            self.driver.switch_to.window(secHandle)
            self.find_element(*self.msgtext_loc).send_keys(self.randoma)
            self.get_sreenshot().insert_img(self.driver,"memSpace_18messReply00.png")
            self.find_element(*self.submit_loc).click()
            return self.tempVar
        except BaseException as msg:
            print(msg)

    #检查发送的消息是否在接收方的消息列表里面
    def type_checkMsgList(self,username):
        try:
            print("\033[1;35;0m 正在检查发送的消息是否出现在接收方消息列表上...\033[0m")
            po1=onSiteMsgPage(self.driver)
            po1.type_sysExit()
            sleep(3)
            po1.login_action(username,"123456")
            po1.type_openVip()
            po1.type_openOnSite()
            po1.type_openMsgList()
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
            self.get_sreenshot().insert_img(self.driver, "memSpace_18messReply01.png")
            self.type_closeHandle()
            self.driver.refresh()
            self.type_sysExit()
            data = getYaml('userInfo.yaml')
            psd = data['loUser']['password']
            po = memSpacePage(self.driver)
            po.login_action("ghj", psd)
            self.type_openVip()
            self.type_openMemSpace()
            self.type_openMgbookMgt()
            return self.assertTip
        except BaseException as msg:
            print(msg)

    #回复
    def type_replyMgbook(self):
        try:
            print("\033[1;35;0m 正在回复留言...\033[0m")
            self.type_getAccount()
            self.find_element(*self.reply_loc).click()
            self.type_getLastHandle()
            self.find_element(*self.retext_loc).clear()
            self.find_element(*self.retext_loc).send_keys(self.randoma)
            self.get_sreenshot().insert_img(self.driver,"memSpace_19reply00.png")
            self.find_element(*self.submit_loc).click()
            self.type_closeHandle()
            self.driver.refresh()
        except BaseException as msg:
            print(msg)

    def checkReplyList(self):
        try:
            print("\033[1;35;0m 正在检查回复留言是否成功...\033[0m")
            text=self.find_eleText(*self.replyText_loc)
            return text
        except BaseException as msg:
            print(msg)

    def type_delMgbook(self):
        try:
            print("\033[1;35;0m 正在删除留言...\033[0m")
            self.find_element(*self.del_loc).click()
            sleep(2)
            self.type_getAlert()
        except BaseException as msg:
            print(msg)

    def type_selTemplate(self):
        try:
            print("\033[1;35;0m 正在选择模板...\033[0m")
            s=self.find_elements(*self.selTemplate_loc)
            s[1].click()
        except BaseException as msg:
            print(msg)

