# -- coding: utf-8 --
from testCase.model import driverUnit,sreenshot
import unittest
from testCase.model.preDelPic import preDelPic
from testCase.module.userMgt.userMgtPage import userMgtPage
from time import sleep
from testCase.model.getuserInfo import getYaml
from time import ctime

class test_userMgt(driverUnit.myUnit):
    driver=driverUnit.myUnit.driver
    po = userMgtPage(driver)
    index_handle = driver.current_window_handle

    #普通会员注册
    def test_00PerRegister(self):
        print("测试开始时间：%r" % ctime())
        # 删除上一次自动化时产生的截图
        preDelPic()
        self.driver.delete_all_cookies()
        po1=userMgtPage(self.driver)
        po1.type_perRegisterT()
        sreenshot.sreenshot.insert_img(self.driver, "userMgt_00PerRegister.png")
        self.assertEqual(po1.type_getText(po1.loginPassAss_loc), "我的空间", "判断普通会员是否注册成功")
        sleep(1)
        self.driver.close()
        self.driver.switch_to.window(self.index_handle)
        self.driver.refresh()
        self.po.type_sysExit()

    # #企业会员注册
    def test_01ComRegister(self):
        po1 = userMgtPage(self.driver)
        po1.type_comRegisterT()
        sreenshot.sreenshot.insert_img(self.driver, "userMgt_01ComRegister.png")
        self.assertEqual(po1.type_getText(po1.loginPassAss_loc), "我的空间", "判断企业会员是否注册成功")
        self.driver.close()
        self.driver.switch_to.window(self.index_handle)
        self.driver.refresh()     #要退出登录，避免注册影响到登录用例的执行
        self.po.type_sysExit()

    #登录
    def test_02login(self):
        #调用函数获取xml账号密码
        self.driver.delete_all_cookies()
        data = getYaml('userInfo.yaml')
        psd = data['loUser']['password']
        self.po.login_action("ghj",psd)
        sleep(3)
        self.assertEqual(self.po.type_getText(self.po.loginPassAss_loc), "我的空间","判断是否登录成功")
        sreenshot.sreenshot.insert_img(self.driver, "userMgt_02login.png")  # 调用function里面的方法

    #进入会员中心
    def test_03openVip(self):
        self.po.type_openVip()
        self.assertEqual(self.po.type_getText(self.po.openVipAss_loc), "站内消息", "判断是否进入了会员中心")
        sreenshot.sreenshot.insert_img(self.driver,"userMgt_03openVip.png")

    # #修改资料
    def test_04editProfile(self):
        self.po.type_acc_editProfile()
        sreenshot.sreenshot.insert_img(self.driver, "userMgt_04editProfile.png")
        data = getYaml('userInfo.yaml')
        text=data['reUserT']['oicq']
        self.assertEqual(text,self.po.randoma,msg="判断是否修改成功")

    #修改密码
    @unittest.skipIf(po.skipFlag_less > 0,"跳过，避免每次手工登录都修改密码")
    def test_05setPsd(self):
        print("\033[1;35;0m 会员中心修改密码...\033[0m")
        self.po.randoma = self.po.type_getAccount()
        self.po.type_setPsd()
        sreenshot.sreenshot.insert_img(self.driver, "userMgt_05setPsd00.png")
        data = getYaml('userInfo.yaml')
        text=data['loUser']['password']
        self.assertEqual(text,self.po.randoma,msg="判断是否修改成功")
        sreenshot.sreenshot.insert_img(self.driver,"userMgt_05setPsd01.png")

    def test_06openBookmarks(self):
        self.po.type_openBookmarks()
        text=self.po.type_getText(self.po.addBmType_loc)
        if "管理分类" in self.driver.page_source:
            print("管理分类在页面元素里面")
        self.assertEqual(text,"管理分类",msg="判断是否进入收藏夹管理页面")
        sreenshot.sreenshot.insert_img(self.driver, "userMgt_06openBookmarks.png")

    def test_07openBookmarksType(self):
        self.po.type_openBookmarksType()

    def test_08addBookmarks(self):
        count1=self.po.type_addBookmarksType()
        count2=self.po.get_listCount(self.po.eleText_loc)
        if str(self.po.randoma) in self.driver.page_source:
            print("已经添加了收藏夹分类")
        self.assertEqual(count1,(count2 - 1),msg="判断收藏夹分类是否新增成功")
        sreenshot.sreenshot.insert_img(self.driver, "userMgt_08Bookmarks.png")

    def test_09modBookmarks(self):
       text=self.po.type_modBookmarksType()
       self.assertEqual(text,str(self.po.randoma),msg="判断收藏夹分类是否修改成功")
       sreenshot.sreenshot.insert_img(self.driver,"userMgt_09modBookmarks.png")

    def test_10delBookmarks(self):
        count1=self.po.get_listCount(self.po.eleText_loc)
        self.po.type_delBookmarksType()
        sreenshot.sreenshot.insert_img(self.driver,"userMgt_10delBookmarks.png")
        count2=self.po.get_listCount(self.po.eleText_loc)
        self.assertEqual(count1,(count2 + 1),msg="判断收藏夹分类是否删除成功")
        self.po.type_openBookmarks()

    def test_11transferBookmarksInfo(self):
        row=self.po.type_transferBookmarksInfo()
        text1 = self.po.find_eleText(*self.po.eleText1_loc)
        print("text1 is:%r"%text1)
        self.po.type_checkBmInfoTransfer(row)
        text2 = self.po.find_eleText(*self.po.eleText1_loc)
        print("text2 is:%r" %text2)
        self.assertEqual(text1,text2,msg="判断收藏信息是否转移到新的收藏夹")
        sreenshot.sreenshot.insert_img(self.driver,"userMgt_11transferBookmarksInfo01.png")

    def test_12delBookmarksInfo(self):
        self.po.type_checkBmInfoTransfer(0)
        count1=self.po.get_listCount(self.po.eleText_loc)
        sreenshot.sreenshot.insert_img(self.driver, "userMgt_12delBookmarksInfo00.png")
        self.po.type_delBookmarksInfo()
        count2=self.po.get_listCount(self.po.eleText_loc)
        sreenshot.sreenshot.insert_img(self.driver, "userMgt_12delBookmarksInfo01.png")
        self.assertEqual(count1,count2 + 1,msg="判断是否删除了收藏夹里面的收藏信息")

    def test_13openFriendList(self):
        self.po.type_openFriendList()
        sreenshot.sreenshot.insert_img(self.driver,"userMgt_13openFriendList.png")

    def test_14addFriendType(self):
        count1 = self.po.type_addFriendType()
        count2=self.po.get_listCount(self.po.eleText_loc)
        self.assertEqual(count1,(count2 - 1),msg="判断好友分类是否新增成功")
        sreenshot.sreenshot.insert_img(self.driver, "userMgt_14addFriendType.png")

    def test_15modFriendType(self):
        text=self.po.type_modFriendType()
        self.assertEqual(text,str(self.po.randoma),msg="判断收藏夹分类是否修改成功")
        sreenshot.sreenshot.insert_img(self.driver,"userMgt_15modFriendType.png")

    def test_16delFriendType(self):
        count1 = self.po.get_listCount(self.po.eleText_loc)
        self.po.type_delFriendType()
        sreenshot.sreenshot.insert_img(self.driver,"userMgt_16delFriendType.png")
        count2=self.po.get_listCount(self.po.eleText_loc)
        self.assertEqual(count1,(count2 + 1),msg="判断好友分类是否删除成功")

    def test_17addFriend(self):
        count1=self.po.type_addFriend()
        sreenshot.sreenshot.insert_img(self.driver, "userMgt_17addFriend.png")
        count2=self.po.get_listCount(self.po.eleText_loc)
        self.assertEqual(count1,(count2 - 1),msg="判断是否添加好友成功")

    def test_18modFriend(self):
        text = self.po.type_modFriend()
        sreenshot.sreenshot.insert_img(self.driver, "userMgt_18modFriend.png")
        self.assertEqual(text,str(self.po.randoma),msg="判断好友备注是否修改成功")

    def test_19delFriend(self):
        count1 = self.po.get_listCount(self.po.eleText_loc)
        self.po.type_delFriend()
        sreenshot.sreenshot.insert_img(self.driver,"userMgt_19delFriendType.png")
        count2=self.po.get_listCount(self.po.eleText_loc)
        self.assertEqual(count1,(count2 + 1),msg="判断好友是否删除成功")

    def test_20loginOut(self):
        self.po.type_sysExit()


if __name__ == '__main__':
    unittest.main()