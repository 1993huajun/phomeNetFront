# -- coding: utf-8 --
from testCase.model import driverUnit,sreenshot
from testCase.module.myIndex.indexPage import indexPage
from time import sleep
from testCase.model.getuserInfo import getYaml
from testCase.module.userMgt.userMgtPage import userMgtPage
import unittest
from time import ctime

class indexMgt(driverUnit.myUnit):
    driver = driverUnit.myUnit.driver
    po = indexPage(driver)
    index_handle = driver.current_window_handle

    def test_00login(self):
        self.driver.delete_all_cookies()
        data = getYaml('userInfo.yaml')
        psd = data['loUser']['password']
        po1 = userMgtPage(self.driver)
        po1.login_action("ghj", psd)
        sleep(3)
        self.assertEqual(po1.type_getText(po1.loginPassAss_loc), "我的空间", "判断是否登录成功")
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_00login.png")  # 调用function里面的方法

    def test_01openDiggit(self):
        self.po.type_openLastUpdate()
        text=self.po.find_eleText(*self.po.diggit1_loc)
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_01openDiggit.png")
        self.assertEqual(text,"来顶一下",msg="判断是否从最近更新的链接进入详情")

    def test_02lastUpdateDiggit(self):
        text1 = self.po.find_eleText(*self.po.diggnum_loc)
        print("text1 is:%s"%text1)
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_02lastUpdateDiggit00.png")
        self.po.type_lastUpdate()
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_02lastUpdateDiggit01.png")
        text2 = self.po.find_eleText(*self.po.diggnum_loc)
        print("text2 is:%s" % text2)
        self.assertEqual(int(text1),int(text2) - 1,msg="判断是否顶一下成功")

    def test_03backToIndex(self):
        self.po.type_backToIndex()
        text=self.po.find_eleText(*self.po.indexFlag_loc)
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_03backToIndex.png")
        self.assertEqual(text, "最后更新", msg="判断是否回到了首页")

    @unittest.skip("")
    def test_04openDlUpdate(self):
        self.po.type_openDlUpdate()
        text = self.po.find_eleText(*self.po.OfficialWebsite_loc)
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_04openDlUpdate.png")
        self.assertEqual(text, "官方站", msg="判断是否从下载更新的链接进入详情")

    @unittest.skip("")
    def test_05openOfficialWebsite(self):
        text=self.po.type_openOfficialWebsite()
        self.assertEqual(text,"https://www.baidu.com/",msg="判断是否打开正确的官方网站")

    @unittest.skip("")
    def test_06openComment(self):
        self.po.type_openComment()
        text = self.po.find_eleText(*self.po.commentFlag_loc)
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_06openComment.png")
        self.assertEqual(text,"我也评两句",msg="判断是否进入发表评论页面")

    @unittest.skip("")
    def test_07comment(self):
        self.po.type_comment()
        text = self.po.type_checkComment()
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_07comment.png")
        self.assertEqual(text,"http://localhost/e/data/face/1.gif",msg="判断是否发表情评论成功")

    @unittest.skip("")
    def test_08commentReply(self):
        self.po.type_commentReply()
        text = self.po.type_checkCommentReply()
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_08commentReply01.png")
        self.assertEqual(text,"回复成功",msg="判断是否回复成功")

    @unittest.skip("")
    def test_09support(self):
        text1 = self.po.find_eleText(*self.po.supportNum_loc)
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_09support00.png")
        self.po.type_support()
        text2 = self.po.find_eleText(*self.po.supportNum_loc)
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_09support01.png")
        self.assertEqual(int(text1),int(text2)-1,msg="判断是否点击支持成功")

    @unittest.skip("")
    def test_10oppose(self):
        text1 = self.po.find_eleText(*self.po.opposeNum_loc)
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_10oppose00.png")
        self.po.type_oppose()
        text2 = self.po.find_eleText(*self.po.opposeNum_loc)
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_10oppose01.png")
        self.assertEqual(int(text1), int(text2) - 1, msg="判断是否点击反对成功")

    @unittest.skip("")
    def test_11commentToIndex(self):
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_11commentToIndex00.png")
        self.po.type_commentToIndex()
        text = self.po.find_eleText(*self.po.indexFlag_loc)
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_11commentToIndex01.png")
        self.assertEqual(text, "最后更新", msg="判断是否回到了首页")

    def test_12openFilmCen(self):
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_12openFilmCen00.png")
        self.po.type_openFilmCen()
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_12openFilmCen01.png")
        text = self.po.find_eleText(*self.po.filmCenFlag_loc)
        self.assertEqual(text,"动作片",msg="判断是否进入了影视频道")

    def test_13playMovie(self):
        length = self.po.type_playMovie()
        self.assertEqual(length,2,msg="判断是否在打开并播放视频")

    def test_14normalSearchNews(self):
        self.po.type_normalSearchNews()
        sreenshot.sreenshot.insert_img(self.driver,"myIndex_14normalSearchNews01.png")
        text = self.po.type_checkSearchNews()
        self.assertEqual(text,self.po.tempVar,msg="判断新闻是否可以普通搜索")

    def test_15advancedSearch(self):
        self.po.type_advancedSearch()
        text = self.po.type_checkSearchNews()
        sreenshot.sreenshot.insert_img(self.driver, "myIndex_15advancedSearch01.png")
        self.assertEqual(text, self.po.tempVar, msg="判断新闻是否可以高级搜索")

    def test_16loginOut(self):
        self.po.type_sysExit()
        self.driver.quit()
        print(self.po.get_excelList("friend.xlsx"))
        print(self.po.get_excelList("friendType.xlsx"))
        print(self.po.get_excelList("bookmarksType.xlsx"))
        print("测试结束时间：%r" % ctime())


if __name__ == '__main__':
    unittest.main()