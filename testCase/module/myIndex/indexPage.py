# -- coding: utf-8 --
from testCase.common.commonPage import Common
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from testCase.module.userMgt.onSiteMsgPage import onSiteMsgPage
from testCase.module.userMgt.userMgtPage import userMgtPage
from testCase.model.getuserInfo import getYaml
import random

class indexPage(Common):
    lastUpdate_loc = (By.XPATH,"//table[@class='box']/tbody/tr/td/ul/li/a")
    diggnum_loc = (By.ID,"diggnum")
    diggit1_loc = (By.XPATH,"//td[@class='diggit']/a")
    diggit2_loc = (By.PARTIAL_LINK_TEXT,"返回首页")
    OfficialWebsite_loc = (By.PARTIAL_LINK_TEXT,"官方站")
    indexFlag_loc = (By.XPATH,"//td[@class='sider']/table/tbody/tr/td/strong")
    comment_loc = (By.PARTIAL_LINK_TEXT,"发表评论")
    commentFlag_loc = (By.CLASS_NAME,"you")
    retext_loc = (By.XPATH,"//table[@class='retext']/tbody/tr[2]/td/div/a")
    saytext_loc = (By.NAME,"saytext")
    imageField_loc = (By.NAME,"imageField")
    checkText_loc = (By.XPATH,"//td[@class='text']/img")
    checkReply_loc = (By.XPATH,"//td[@class='text']")
    reply_loc = (By.PARTIAL_LINK_TEXT,"回复")
    support_loc = (By.PARTIAL_LINK_TEXT,"支持")
    oppose_loc = (By.PARTIAL_LINK_TEXT,"反对")
    supportNum_loc = (By.XPATH,"//div[@class='re']/span")
    opposeNum_loc = (By.XPATH,"//div[@class='re']/span[2]")
    indexText_loc = (By.PARTIAL_LINK_TEXT,"网站首页")
    filmCenFlag_loc = (By.XPATH,"//table[@class='title']/tbody/tr/td/strong")
    playMovie_loc = (By.XPATH,"//table[@class='box']/tbody/tr/td/table/tbody/tr[11]/td[2]/a")
    keyboard_loc = (By.NAME,"keyboard")
    selector_loc = (By.NAME,"tbname")
    seleOp_loc = (By.XPATH,"//select[@class='tbname']/option")
    searchBt_loc = (By.CLASS_NAME,"inputSub")
    targetText_loc = (By.CLASS_NAME,"l")
    starttime_loc = (By.NAME,"starttime")
    endtime_loc = (By.NAME,"endtime")
    classid_loc = (By.NAME,"classid")
    submit3_loc = (By.NAME,"Submit22")

    def type_openLastUpdate(self):
        try:
            print("\033[1;31;40m 打开最近更新的详情页 \033[0m")
            self.find_element(*self.lastUpdate_loc).click()
        except BaseException as msg:
            print(msg)

    def type_lastUpdate(self):
        try:
            print("\033[1;35;0m 正在点击顶一下...\033[0m")
            self.find_element(*self.diggit1_loc).click()
            self.type_getAlert()
        except BaseException as msg:
            print(msg)

    def type_backToIndex(self):
        try:
            print("\033[1;35;0m 返回到首页...\033[0m")
            self.find_element(*self.diggit2_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openDlUpdate(self):
        try:
            print("\033[1;31;40m 打开下载更新的详情页 \033[0m")
            row = self.get_ExcelRow("software.xlsx")
            text = self.get_ExcelText("software.xlsx",row - 1)
            downloadUpdate_loc = (By.PARTIAL_LINK_TEXT,str(text))
            self.find_element(*downloadUpdate_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openOfficialWebsite(self):
        try:
            print("\033[1;31;40m 打开下载更新的详情页链接的官方网站 \033[0m")
            self.find_element(*self.OfficialWebsite_loc).click()
            self.type_getLastHandle()
            sleep(2)
            text=self.driver.current_url
            self.get_sreenshot().insert_img(self.driver,"myIndex_05openOfficialWebsite.png")
            self.type_closeHandle()
            return text
        except BaseException as msg:
            print(msg)

    def type_openComment(self):
        try:
            print("\033[1;31;40m 打开发表评论页面 \033[0m")
            self.find_element(*self.comment_loc).click()
        except BaseException as msg:
            print(msg)

    def type_comment(self):
        try:
            print("\033[1;35;0m 正在发表评论...\033[0m")
            #只发表情
            self.find_element(*self.retext_loc).click()
            self.find_element(*self.imageField_loc).click()
            sleep(3)
        except BaseException as msg:
            print(msg)

    def type_checkComment(self):
        try:
            print("\033[1;35;0m 正在检查评论是否发表成功...\033[0m")
            text = self.find_element(*self.checkText_loc).get_attribute('src')
            return text
        except BaseException as msg:
            print(msg)

    def type_commentReply(self):
        try:
            print("\033[1;35;0m 正在回复评论...\033[0m")
            self.find_element(*self.reply_loc).click()
            self.type_getAccount()
            self.find_element(*self.saytext_loc).send_keys(self.randoma)
            self.get_sreenshot().insert_img(self.driver,"myIndex_08commentReply00.png")
            self.find_element(*self.imageField_loc).click()
            sleep(3)
        except BaseException as msg:
            print(msg)

    def type_checkCommentReply(self):
        try:
            print("\033[1;35;0m 正在检查回复是否成功...\033[0m")
            text = self.find_eleText(*self.checkReply_loc)
            if str(self.randoma) in text:
                self.assertTip = "回复成功"
            return self.assertTip
        except BaseException as msg:
            print(msg)

    def type_support(self):
        try:
            print("\033[1;35;0m 正在点击支持...\033[0m")
            self.find_element(*self.support_loc).click()
            self.type_getAlert()
        except BaseException as msg:
            print(msg)

    def type_oppose(self):
        try:
            self.type_comment()
            print("\033[1;35;0m 正在点击反对...\033[0m")
            self.find_element(*self.oppose_loc).click()
            self.type_getAlert()
        except BaseException as msg:
            print(msg)

    def type_commentToIndex(self):
        try:
            print("\033[1;35;0m 正在返回到首页...\033[0m")
            self.find_element(*self.indexText_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openFilmCen(self):
        try:
            print("\033[1;31;40m 正在打开影视频道 \033[0m")
            self.find_element(*self.filmCen_loc).click()
        except BaseException as msg:
            print(msg)

    def type_playMovie(self):
        try:
            print("\033[1;35;0m 正在播放影视视频...\033[0m")
            self.find_element(*self.lastUpdate_loc).click()
            self.find_element(*self.playMovie_loc).click()
            sleep(1)
            handles = self.driver.window_handles
            length = len(handles)
            self.driver.switch_to.window(handles[-1])
            self.get_sreenshot().insert_img(self.driver,"myIndex_13playMovie.png")
            self.type_closeHandle()
            self.find_element(*self.indexText_loc).click()
            return length
        except BaseException as msg:
            print(msg)

    def type_normalSearchNews(self):
        try:
            print("\033[1;35;0m 正在执行普通搜索...\033[0m")
            tuples=self.get_ranExcelText("news.xlsx")
            self.tempVar = tuples[1]
            self.find_element(*self.keyboard_loc).send_keys(self.tempVar)
            self.get_sreenshot().insert_img(self.driver,"myIndex_14normalSearchNews00.png")
            self.find_element(*self.searchBt_loc).click()
        except BaseException as msg:
            print(msg)

    def type_checkSearchNews(self):
        try:
            print("\033[1;35;0m 正在检查搜索结果...\033[0m")
            return self.find_eleText(*self.targetText_loc)
        except BaseException as msg:
            print(msg)

    # def type_normalSearchDownload(self):
    #     try:
    #         print("")
    #     except BaseException as msg:
    #         print(msg)

    def type_advancedSearch(self):
        try:
            print("\033[1;35;0m 正在执行高级搜索...\033[0m")
            self.find_element(*self.submit_loc).click()
            select_ele=Select(self.find_element(*self.classid_loc))
            select_ele.select_by_index(2)
            tuples=self.get_ranExcelText("news.xlsx")
            self.tempVar = tuples[1]
            self.find_element(*self.keyboard_loc).send_keys(self.tempVar)
            self.get_sreenshot().insert_img(self.driver, "myIndex_15advancedSearch00.png")
            self.find_element(*self.submit3_loc).click()
        except BaseException as msg:
            print(msg)

