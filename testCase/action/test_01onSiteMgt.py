# -- coding: utf-8 --
from testCase.model import driverUnit,sreenshot
from testCase.module.userMgt.onSiteMsgPage import onSiteMsgPage
from time import sleep
from testCase.model.getuserInfo import getYaml
from testCase.module.userMgt.userMgtPage import userMgtPage
import unittest

class test_userMgt(driverUnit.myUnit):
    driver = driverUnit.myUnit.driver
    po = onSiteMsgPage(driver)
    index_handle = driver.current_window_handle

    def test_00login(self):
        self.driver.delete_all_cookies()
        data = getYaml('userInfo.yaml')
        psd = data['loUser']['password']
        po1=userMgtPage(self.driver)
        po1.login_action("ghj", psd)
        sleep(3)
        self.assertEqual(po1.type_getText(po1.loginPassAss_loc), "我的空间", "判断是否登录成功")
        sreenshot.sreenshot.insert_img(self.driver, "onSiteMsg_00login.png")  # 调用function里面的方法
        po1.type_openVip()
        print(self.po.get_excelList("friend.xlsx"))
        print(self.po.get_excelList("friendType.xlsx"))
        print(self.po.get_excelList("bookmarksType.xlsx"))
        # self.po.mod_excel("friend.xlsx","")
        # self.po.mod_excel("friendType.xlsx","")
        # self.po.mod_excel("bookmarksType.xlsx","")
        # print(self.po.get_excelList("friend.xlsx"))
        # print(self.po.get_excelList("friendType.xlsx"))
        # print(self.po.get_excelList("bookmarksType.xlsx"))

    def test_01sendMsf(self):
        self.po.type_openOnSite()
        tuples = self.po.get_ranExcelText("friend.xlsx")
        row = tuples[0]
        text = tuples[1]
        self.po.type_sendMsg(row,text)
        sreenshot.sreenshot.insert_img(self.driver, "onSiteMsg_01sendMsf00.png")
        self.po.type_checkMsgList(self.po.tempVar)
        sreenshot.sreenshot.insert_img(self.driver, "onSiteMsg_01sendMsf01.png")
        self.assertEqual(self.po.assertTip,"发送成功","判断消息是否发送成功")
        #退出登录，并用测试账号登录
        self.po.type_sysExit()
        self.test_00login()

    '''
    这个
    方法
    需要
    修改
    '''
    def test_02catMsg(self):
        self.po.type_openOnSite()
        self.po.type_openMsgList()
        self.po.type_catMsg()
        sreenshot.sreenshot.insert_img(self.driver, "onSiteMsg_02catMsg.png")
        text=self.po.type_getText(self.po.forward_loc)
        self.assertEqual(text,"转发","判断点击标题是否进入查看消息内容")

    def test_03replyMsg(self):
        self.po.type_replyMsg()
        sreenshot.sreenshot.insert_img(self.driver, "onSiteMsg_03replyMsg.png")
        count=self.po.type_getMsgListCount()
        self.assertNotEqual(count,0,"判断是否回复成功")#假的判断

    def test_04back(self):
        text1=self.po.type_getText(self.po.titleText_loc)
        sreenshot.sreenshot.insert_img(self.driver, "onSiteMsg_04back00.png")
        self.po.type_back()
        sreenshot.sreenshot.insert_img(self.driver, "onSiteMsg_04back01.png")
        text2=self.po.type_getText(self.po.titleText_loc)
        self.assertEqual(text1,text2,"判断是否返回成功")

    def test_05forward(self):
        self.po.type_forward()
        sreenshot.sreenshot.insert_img(self.driver, "onSiteMsg_05forward.png")
        count = self.po.type_getMsgListCount()
        self.assertNotEqual(count,0,"判断是否转发成功")#假的判断

    def test_06delMsgInCat(self):
        count1=self.po.get_listCount(self.po.mid_loc)
        sreenshot.sreenshot.insert_img(self.driver, "onSiteMsg_06delMsgInCat00.png")
        self.po.type_catMsg()
        self.po.type_delMsg()
        sreenshot.sreenshot.insert_img(self.driver, "onSiteMsg_06delMsgInCat01.png")
        count2=self.po.get_listCount(self.po.mid_loc)
        self.assertEqual(count1,count2 + 1,"判断在查看消息里面消息是否删除成功")

    def test_07delMsg(self):
        count1 = self.po.get_listCount(self.po.mid_loc)
        sreenshot.sreenshot.insert_img(self.driver, "onSiteMsg_07delMsg00.png")
        self.po.type_delMsg()
        count2 = self.po.get_listCount(self.po.mid_loc)
        sreenshot.sreenshot.insert_img(self.driver, "onSiteMsg_07delMsg01.png")
        self.assertEqual(count1, count2 + 1, "判断消息是否删除成功")

    def test_08delMsgBatch(self):
        count1=self.po.get_listCount(self.po.mid_loc)
        sreenshot.sreenshot.insert_img(self.driver, "onSiteMsg_08delMsgBatch00.png")
        self.po.type_delMsgBatch()
        count2 = self.po.get_listCount(self.po.mid_loc)
        sreenshot.sreenshot.insert_img(self.driver, "onSiteMsg_08delMsgBatch01.png")
        self.assertEqual(count1, count2 + 1, "判断消息是否批量删除成功")

    def test_09loginOut(self):
        self.po.type_sysExit()

if __name__ == '__main__':
    unittest.main()