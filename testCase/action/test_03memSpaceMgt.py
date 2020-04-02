# -- coding: utf-8 --
from testCase.model import driverUnit,sreenshot
from testCase.module.userMgt.memSpacePage import memSpacePage
from time import sleep
from testCase.model.getuserInfo import getYaml
from testCase.module.userMgt.userMgtPage import userMgtPage
import unittest

class memSpaceMgt(driverUnit.myUnit):
    driver = driverUnit.myUnit.driver
    po = memSpacePage(driver)
    index_handle = driverUnit.myUnit.driver.current_window_handle

    def test_00login(self):
        self.driver.delete_all_cookies()
        data = getYaml('userInfo.yaml')
        psd = data['loUser']['password']
        po1 = userMgtPage(self.driver)
        po1.login_action("ghj", psd)
        sleep(3)
        self.assertEqual(po1.type_getText(po1.loginPassAss_loc), "我的空间", "判断是否登录成功")
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_00login.png")  # 调用function里面的方法
        po1.type_openVip()

    def test_01openSetSpace(self):
        self.po.type_openMemSpace()
        self.po.type_openSetSpace()
        text=self.po.find_eleText(*self.po.setSpaceText_loc)
        self.assertEqual(text,"设置空间",msg="判断是否进入设置空间")
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_01openSetSpace.png")

    def test_02setSpace(self):
        self.po.type_openMemSpace()
        self.po.type_setSpace()
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_02addSetSpace.png")
        text=self.po.type_checkSpace()
        self.assertEqual(text,str(self.po.randoma),msg="判断是否设置空间成功")

    def test_03openNews(self):
        self.po.type_openNews()
        text=self.po.find_eleText(*self.po.addNews_loc)
        sreenshot.sreenshot.insert_img(self.driver,"memSpace_03openNews.png")
        self.assertEqual(text,"增加新闻",msg="判断是否打开新闻")

    def test_04openSoftware(self):
        self.po.type_openSoftware()
        text=self.po.find_eleText(*self.po.addSoftware_loc)
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_04openSoftware.png")
        self.assertEqual(text, "增加软件", msg="判断是否打开软件")

    def test_05openPic(self):
        self.po.type_openPic()
        text=self.po.find_eleText(*self.po.addPic_loc)
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_05openPic.png")
        self.assertEqual(text, "增加图片", msg="判断是否打开图片")

    def test_06openFlash(self):
        self.po.type_openFlash()
        text=self.po.find_eleText(*self.po.addFlash_loc)
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_06openFlash.png")
        self.assertEqual(text, "增加FLASH", msg="判断是否打开flash")

    def test_07openArticle(self):
        self.po.type_openArticle()
        text=self.po.find_eleText(*self.po.addArticle_loc)
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_07openArticle.png")
        self.assertEqual(text, "增加文章", msg="判断是否打开文章")

    def test_08openClassified(self):
        self.po.type_openClassified()
        text=self.po.find_eleText(*self.po.addClassified_loc)
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_08openClassified.png")
        self.assertEqual(text, "增加分类信息", msg="判断是否打开分类信息")

    def test_09openUserInfo(self):
        self.po.type_openUserInfo()
        text=self.po.find_eleText(*self.po.showUserInfo_loc)
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_09openUserInfo.png")
        self.assertEqual(text, "公司介绍", msg="判断是否打开个人资料")

    def test_10openMgbook(self):
        self.po.type_openMgbook()
        text=self.po.find_eleText(*self.po.addMgbook_loc)
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_10openMgbook.png")
        self.assertEqual(text, "管理留言", msg="判断是否打开留言")

    def test_11addMgbook(self):
        self.po.type_addMgbook()
        text = self.po.type_checkMgbookExist()
        self.assertEqual(text,self.po.tempVar,msg="判断留言是否成功发布")
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_11addMgbook01.png")
    #
    def test_12openFeedback(self):
        self.po.type_openFeedback()
        text = self.po.find_eleText(*self.po.feedbackText_loc)
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_12openFeedback.png")
        self.assertEqual(text, "在线反馈", msg="判断是否打开反馈信息")

    def test_13addFeedback(self):
        self.po.type_addfeedback()
        text = self.po.type_checkFeedbackExist()
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_13addFeedback01.png")
        self.assertEqual(text,str(self.po.randoma),msg="判断是否增加反馈信息成功")

    def test_14checkFbTitle(self):
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_14checkFbTitle00.png")
        text = self.po.type_checkTitle()
        self.assertEqual(text,str(self.po.randoma),msg="判断是否打开反馈的详情")

    def test_15checkFbUser(self):
        sreenshot.sreenshot.insert_img(self.driver,"memSpace_15checkFbUser00.png")
        text = self.po.checkUser()
        self.assertEqual(text,"公司介绍",msg="判断是否能够打开反馈的用户空间")

    def test_16delFeedBack(self):
        count1 = self.po.get_listCount(self.po.eleText3_loc)
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_16delFeedBack00.png")
        self.po.type_delFeedback()
        count2 = self.po.get_listCount(self.po.eleText3_loc)
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_16delFeedBack01.png")
        self.assertEqual(count1,count2 + 1,msg="判断是否删除反馈成功")

    def test_17openMgbookMgt(self):
        self.po.type_openMgbookMgt()
        text=self.po.find_eleText(*self.po.messReply_loc)
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_17openMgbookMgt.png")
        self.assertEqual(text,"消息回复",msg="判断是否打开了管理留言页面")

    def test_18messReply(self):
        text=self.po.type_replyMgbookBySelFriend()
        self.po.type_checkMsgList(text)
        self.assertEqual(self.po.assertTip,"发送成功","判断消息回复是否成功")

    def test_19reply(self):
        self.po.type_replyMgbook()
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_19reply01.png")
        text=self.po.checkReplyList()
        self.assertEqual(text,"回复: "+str(self.po.randoma),msg="判断是否回复成功")

    def test_20delMgbook(self):
        count1 = self.po.get_listCount(self.po.eleText4_loc)
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_20delMgbook.png")
        self.po.type_delMgbook()
        count2 = self.po.get_listCount(self.po.eleText4_loc)
        self.assertEqual(count1,count2 + 1,msg="判断是否删除留言")

    def test_21openSelTemplate(self):
        self.po.type_openSelTemplate()
        text=self.po.find_eleText(*self.po.selTemplate_loc)
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_21openSelTemplate.png")
        self.assertEqual(text,"选定",msg="判断是否打开了选择模板页面")

    def test_22SelTemplate(self):
        self.po.type_selTemplate()
        sreenshot.sreenshot.insert_img(self.driver, "memSpace_22SelTemplate.png")

    def test_23loginOut(self):
        self.po.type_sysExit()
        print(self.po.get_excelList("friend.xlsx"))
        print(self.po.get_excelList("friendType.xlsx"))
        print(self.po.get_excelList("bookmarksType.xlsx"))


if __name__ == '__main__':
    unittest.main()