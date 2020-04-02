# -- coding: utf-8 --
from testCase.model import driverUnit,sreenshot
from testCase.module.userMgt.postPage import postPage
from time import sleep
from testCase.model.getuserInfo import getYaml
from testCase.module.userMgt.userMgtPage import userMgtPage
import unittest

class postMgt(driverUnit.myUnit):
    driver = driverUnit.myUnit.driver
    po = postPage(driver)
    index_handle = driver.current_window_handle

    def test_00login(self):
        self.driver.delete_all_cookies()
        data = getYaml('userInfo.yaml')
        psd = data['loUser']['password']
        po1 = userMgtPage(self.driver)
        po1.login_action("ghj", psd)
        sleep(3)
        self.assertEqual(po1.type_getText(po1.loginPassAss_loc), "我的空间", "判断是否登录成功")
        sreenshot.sreenshot.insert_img(self.driver, "post_00login.png")  # 调用function里面的方法
        po1.type_openVip()

    def test_01openNewsMgt(self):
        self.po.type_openPost()
        self.po.type_openNewsMgt()
        text = self.po.find_eleText(*self.po.everPost_loc)
        sreenshot.sreenshot.insert_img(self.driver, "post_01openNewsMgt.png")  # 调用function里面的方法
        self.assertEqual(text,"已发布",msg="判断是否打开了管理新闻页面")

    def test_02newsRelease(self):
        self.po.type_newsRelease()
        text=self.po.type_checkPost(self.po.newsCen_loc,"新闻")
        sreenshot.sreenshot.insert_img(self.driver, "post_02newsRelease.png")
        self.assertEqual(text,str(self.po.randoma),msg="判断新闻是否发布成功")
        self.po.type_openVip()
        self.po.type_openPost()
        self.po.type_openNewsMgt()

    def test_03newsSearch(self):
        length=self.po.type_comSearch("新闻")
        sreenshot.sreenshot.insert_img(self.driver, "post_03newsSearch.png")
        self.assertEqual(length,1,msg="判断是否查询出新发布的新闻")

    def test_04newsComments(self):#无法通过元素定位找到评论内容
        self.po.type_checkOject()
        self.po.type_getLastHandle()
        self.po.type_comComments("新闻","post_04newsComments00.png")
        self.po.type_checkComments("post_04newsComments01.png")
        self.po.type_closeHandle()

    def test_05newsMod(self):
        text=self.po.type_comMod("新闻","post_05newsMod00.png")
        sreenshot.sreenshot.insert_img(self.driver,"post_05newsMod01.png")
        self.assertEqual(text,str(self.po.randoma),msg="判断新闻标题是否修改成功")

    def test_06newsDel(self):
        count1 = self.po.get_listCount(self.po.eleText1_loc)
        sreenshot.sreenshot.insert_img(self.driver, "post_06newsDel00.png")
        self.po.type_comDel("新闻")
        count2 = self.po.get_listCount(self.po.eleText1_loc)
        self.assertEqual(count1,(count2 + 1),msg="判断新闻是否删除成功")
        sreenshot.sreenshot.insert_img(self.driver, "post_06newsDel01.png")

    def test_07openSoftwareMgt(self):
        self.po.type_openSoftwareMgt()
        text = self.po.find_eleText(*self.po.everPost_loc)
        sreenshot.sreenshot.insert_img(self.driver, "post_07openSoftwareMgt.png")  # 调用function里面的方法
        self.assertEqual(text, "已发布", msg="判断是否打开了管理软件页面")

    def test_08softwareRelease(self):
        self.po.type_softwareRelease()
        text = self.po.type_checkPost(self.po.downLoadCen_loc,"软件")
        self.driver.refresh()
        sreenshot.sreenshot.insert_img(self.driver, "post_08softwareRelease.png")
        self.assertEqual(text, str(self.po.randoma), msg="判断软件是否上传成功")
        self.po.type_openVip()
        self.po.type_openPost()
        self.po.type_openSoftwareMgt()

    def test_09softwareSearch(self):
        length=self.po.type_comSearch("软件")
        sreenshot.sreenshot.insert_img(self.driver, "post_09newsSearch.png")
        self.assertEqual(length,1,msg="判断是否查询出新上传的软件信息")

    def test_10swAddToBookmarks(self):
        self.po.type_checkOject()
        self.po.type_getLastHandle()
        self.po.type_swAddToBookmarks()
        sreenshot.sreenshot.insert_img(self.driver,"post_10swAddToBookmarks.png")
        self.assertEqual(self.po.assertTip,"匹配",msg="判断从excel获取的分类是否在收藏夹列表里面")

    def test_11softwareComments(self):
        self.po.type_comComments("软件", "post_11softwareComments00.png")
        self.po.type_checkComments("post_11softwareComments01.png")
        self.po.type_closeHandle()

    def test_12softwareMod(self):
        text=self.po.type_comMod("软件","post_12softwareMod00.png")
        sreenshot.sreenshot.insert_img(self.driver,"post_12softwareMod01.png")
        self.assertEqual(text,str(self.po.randoma),msg="判断软件名称是否修改成功")

    def test_13softwareDel(self):
        count1 = self.po.get_listCount(self.po.eleText1_loc)
        sreenshot.sreenshot.insert_img(self.driver, "post_13softwareDel00.png")
        self.po.type_comDel("软件")
        count2 = self.po.get_listCount(self.po.eleText1_loc)
        self.assertEqual(count1,(count2 + 1),msg="判断软件是否删除成功")
        sreenshot.sreenshot.insert_img(self.driver, "post_13softwareDel01.png")

    # 添加测试数据，保证测试数据不中断
    @unittest.skip("跳过")
    def test_13zrepeat(self):
        for i in range(3):
            self.test_08softwareRelease()
            self.test_10swAddToBookmarks()
            self.test_11softwareComments()

    def test_14openPicMgt(self):
        self.po.type_openPicMgt()
        text = self.po.find_eleText(*self.po.everPost_loc)
        sreenshot.sreenshot.insert_img(self.driver, "post_14openPicMgt.png")  # 调用function里面的方法
        self.assertEqual(text, "已发布", msg="判断是否打开了管理图片页面")

    def test_15picRelease(self):
        self.po.type_picRelease()
        text = self.po.type_checkPost(self.po.picCen_loc, "图片")
        self.driver.refresh()
        sreenshot.sreenshot.insert_img(self.driver, "post_15picRelease.png")
        self.assertEqual(text, str(self.po.randoma), msg="判断图片是否上传成功")
        self.po.type_openVip()
        self.po.type_openPost()
        self.po.type_openPicMgt()

    def test_16picComments(self):
        self.po.type_checkOject()
        self.po.type_getLastHandle()
        self.po.type_comComments("图片", "post_16picComments00.png")
        self.po.type_checkComments("post_16picComments01.png")
        self.po.type_closeHandle()

    def test_16picSearch(self):
        length=self.po.type_comSearch("图片")
        sreenshot.sreenshot.insert_img(self.driver, "post_16picSearch.png")
        self.assertEqual(length,1,msg="判断是否查询出新上传的图片信息")

    def test_17picMod(self):
        text=self.po.type_comMod("图片","post_17picMod00.png")
        sreenshot.sreenshot.insert_img(self.driver,"post_17picMod01.png")
        self.assertEqual(text,str(self.po.randoma),msg="判断图片名称是否修改成功")

    def test_18picDel(self):
        count1 = self.po.get_listCount(self.po.eleText1_loc)
        sreenshot.sreenshot.insert_img(self.driver, "post_18picDel00.png")
        self.po.type_comDel("图片")
        count2 = self.po.get_listCount(self.po.eleText1_loc)
        self.assertEqual(count1,(count2 + 1),msg="判断图片是否删除成功")
        sreenshot.sreenshot.insert_img(self.driver, "post_18picDel01.png")

    def test_19openFlashMgt(self):
        self.po.type_openFlashMgt()
        text = self.po.find_eleText(*self.po.everPost_loc)
        sreenshot.sreenshot.insert_img(self.driver, "post_19openFlashMgt.png")  # 调用function里面的方法
        self.assertEqual(text, "已发布", msg="判断是否打开了管理FLASH页面")

    def test_20flashRelease(self):
        self.po.type_flashRelease()
        text = self.po.type_checkPost(self.po.flashCen_loc, "flash")
        self.driver.refresh()
        sreenshot.sreenshot.insert_img(self.driver, "post_20flashRelease.png")
        self.assertEqual(text, str(self.po.randoma), msg="判断FLASH是否上传成功")
        self.po.type_openVip()
        self.po.type_openPost()
        self.po.type_openFlashMgt()

    def test_21flashSearch(self):
        length=self.po.type_comSearch("flash")
        sreenshot.sreenshot.insert_img(self.driver, "post_21flashSearch.png")
        self.assertEqual(length,1,msg="判断是否查询出新上传的flash")

    def test_22flashComments(self):
        self.po.type_checkOject()
        self.po.type_getLastHandle()
        self.po.type_comComments("flash", "post_22flashComments00.png")
        self.po.type_checkComments("post_22flashComments01.png")
        self.po.type_closeHandle()

    def test_23flashMod(self):
        text=self.po.type_comMod("flash","post_23flashMod00.png")
        sreenshot.sreenshot.insert_img(self.driver,"post_23flashMod01.png")
        self.assertEqual(text,str(self.po.randoma),msg="判断flash名称是否修改成功")

    def test_24flashDel(self):
        count1 = self.po.get_listCount(self.po.eleText1_loc)
        sreenshot.sreenshot.insert_img(self.driver, "post_24flashDel00.png")
        self.po.type_comDel("flash")
        count2 = self.po.get_listCount(self.po.eleText1_loc)
        self.assertEqual(count1,(count2 + 1),msg="判断flash是否删除成功")
        sreenshot.sreenshot.insert_img(self.driver, "post_24flashDel01.png")

    def test_25openArticleMgt(self):
        self.po.type_openArticleMgt()
        text = self.po.find_eleText(*self.po.everPost_loc)
        sreenshot.sreenshot.insert_img(self.driver, "post_25openArticleMgt.png")  # 调用function里面的方法
        self.assertEqual(text, "已发布", msg="判断是否打开了管理文章页面")

    def test_26articleRelease(self):
        self.po.type_articleRelease()
        text = self.po.type_checkPost(self.po.articleCen_loc, "文章")
        self.driver.refresh()
        sreenshot.sreenshot.insert_img(self.driver, "post_26articleRelease.png")
        self.assertEqual(text, str(self.po.randoma), msg="判断文章是否发布成功")
        self.po.type_openVip()
        self.po.type_openPost()
        self.po.type_openArticleMgt()

    def test_27articleSearch(self):
        length=self.po.type_comSearch("文章")
        sreenshot.sreenshot.insert_img(self.driver, "post_27articleSearch.png")
        self.assertEqual(length,1,msg="判断是否查询出新发布的文章")

    def test_28artcleComments(self):
        self.po.type_checkOject()
        self.po.type_getLastHandle()
        self.po.type_comComments("文章", "post_28articleComments00.png")
        self.po.type_checkComments("post_28articleComments01.png")
        self.po.type_closeHandle()

    def test_29articleMod(self):
        text = self.po.type_comMod("文章", "post_29articleMod00.png")
        sreenshot.sreenshot.insert_img(self.driver, "post_29articleMod01.png")
        self.assertEqual(text, str(self.po.randoma), msg="判断文章标题是否修改成功")

    def test_30articleDel(self):
        count1 = self.po.get_listCount(self.po.eleText1_loc)
        sreenshot.sreenshot.insert_img(self.driver, "post_30articleDel00.png")
        self.po.type_comDel("文章")
        count2 = self.po.get_listCount(self.po.eleText1_loc)
        self.assertEqual(count1, (count2 + 1), msg="判断文章是否删除成功")
        sreenshot.sreenshot.insert_img(self.driver, "post_30articleDel01.png")

    def test_31openClassifiedsMgt(self):
        self.po.type_openClassifiedsMgt()
        text = self.po.find_eleText(*self.po.everPost_loc)
        sreenshot.sreenshot.insert_img(self.driver, "post_31openClassifiedsMgt.png")  # 调用function里面的方法
        self.assertEqual(text, "已发布", msg="判断是否打开了管理分类信息页面")

    def test_32classifiedRelease(self):
        self.po.type_classifiedRelease()
        text = self.po.type_checkPost(self.po.clsInfoCen_loc, "分类信息")
        self.driver.refresh()
        sreenshot.sreenshot.insert_img(self.driver, "post_32classifiedRelease.png")
        self.assertEqual(text, str(self.po.randoma), msg="判断文章是否发布成功")
        self.po.type_openVip()
        self.po.type_openPost()
        self.po.type_openClassifiedsMgt()

    def test_33classifiedSearch(self):
        length = self.po.type_comSearch("分类信息")
        sreenshot.sreenshot.insert_img(self.driver, "post_33classifiedSearch.png")
        self.assertEqual(length, 1, msg="判断是否查询出新发布的分类信息")

    def test_34classifiedComments(self):
        self.po.type_checkOject()
        self.po.type_getLastHandle()
        self.po.type_comComments("分类信息", "post_34classifiedComments00.png")
        self.po.type_checkComments("post_34classifiedComments01.png")
        self.po.type_closeHandle()

    def test_35classifiedMod(self):
        text = self.po.type_comMod("分类信息", "post_35classifiedMod00.png")
        sreenshot.sreenshot.insert_img(self.driver, "post_35classifiedMod01.png")
        self.assertEqual(text, str(self.po.randoma), msg="判断分类信息名称是否修改成功")

    def test_36classifiedDel(self):
        count1 = self.po.get_listCount(self.po.eleText1_loc)
        sreenshot.sreenshot.insert_img(self.driver, "post_36classifiedDel.png")
        self.po.type_comDel("分类信息")
        count2 = self.po.get_listCount(self.po.eleText1_loc)
        self.assertEqual(count1, (count2 + 1), msg="判断分类信息是否删除成功")
        sreenshot.sreenshot.insert_img(self.driver, "post_36classifiedDel01.png")

    def test_37loginOut(self):
        self.po.type_sysExit()
        print(self.po.get_excelList("friend.xlsx"))
        print(self.po.get_excelList("friendType.xlsx"))
        print(self.po.get_excelList("bookmarksType.xlsx"))

if __name__ == '__main__':
    unittest.main()
