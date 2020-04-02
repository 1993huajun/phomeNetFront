# -- coding: utf-8 --
from testCase.common.commonPage import Common
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

class postPage(Common):
    #公共
    openPost_loc = (By.ID,"domenuinfoid")
    indexPage_loc = (By.PARTIAL_LINK_TEXT,"网站首页")
    #二级菜单
    newsMgt_loc = (By.PARTIAL_LINK_TEXT,"管理新闻")
    softwareMgt_loc = (By.PARTIAL_LINK_TEXT,"管理软件")
    picMgt_loc = (By.PARTIAL_LINK_TEXT,"管理图片")
    flashMgt_loc = (By.PARTIAL_LINK_TEXT,"管理FLASH")
    articleMgt_loc = (By.PARTIAL_LINK_TEXT,"管理文章")
    classifiedsMgt_loc = (By.PARTIAL_LINK_TEXT,"管理分类信息")
    #管理新闻
    classid_loc = (By.NAME,"classid")
    title_loc = (By.NAME,"title")
    ftitle_loc = (By.NAME,"ftitle")
    keyboard_loc = (By.NAME,"keyboard")
    titlepicfile_loc = (By.NAME,"titlepicfile")
    smalltext_loc = (By.NAME,"smalltext")
    writer_loc = (By.NAME,"writer")
    befrom_loc = (By.NAME,"befrom")
    newsContent_loc = (By.XPATH,"//form[@name='add']/div/div/div/div/iframe")
    sendText_loc = (By.CLASS_NAME,"cke_editable.cke_editable_themed.cke_contents_ltr.cke_show_borders")
    addnews_loc = (By.NAME,"addnews")
    everPost_loc = (By.PARTIAL_LINK_TEXT,"已发布")
    eleText1_loc = (By.XPATH, "//table[@class='tableborder' and @width='100%']/tbody/tr")#查列表数量
    eleFind_loc = (By.XPATH,"//table[@class='tableborder' and @width='100%']/tbody/tr[2]/td[1]/div/a[2]")
    saytext_loc = (By.NAME, "saytext")#新闻评论
    imageField_loc = (By.NAME,"imageField")#提交留言
    commCheck_loc = (By.XPATH,"//table[@class='title']/tbody/tr/td[2]/a")
    #管理软件
    softwriter_loc = (By.NAME,"softwriter")
    homepage_loc = (By.NAME,"homepage")
    demo_loc = (By.NAME,"demo")
    softfj_loc = (By.NAME,"softfj")
    check_loc = (By.NAME,"check")
    select_loc = (By.NAME,"select")
    select2_loc = (By.NAME,"select2")
    filesize_loc = (By.NAME,"filesize")
    downpathfile_loc = (By.NAME,"downpathfile")
    softsay_loc = (By.NAME,"softsay")
    addToBks_loc = (By.PARTIAL_LINK_TEXT,"加入收藏夹")
    cid_loc = (By.NAME, "cid")
    cidOp_loc = (By.XPATH, "//select[@name='cid']/option")
    #管理图片
    picsize_loc = (By.NAME,"picsize")
    picfbl_loc = (By.NAME,"picfbl")
    picfrom_loc = (By.NAME,"picfrom")
    picurlfile_loc = (By.NAME,"picurlfile")
    picsay_loc = (By.NAME,"picsay")
    #管理flash
    flashwriter_loc = (By.NAME,"flashwriter")
    email_loc = (By.NAME,"email")
    flashurlfile_loc = (By.NAME,"flashurlfile")
    flashsay_loc = (By.NAME,"flashsay")
    #管理分类信息
    mycontact_loc = (By.NAME,"mycontact")


    '''打开某个页面'''
    def type_openPost(self):
        try:
            print("\033[1;31;40m 展开投稿 \033[0m")
            sleep(1)
            self.find_element(*self.openPost_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openNewsMgt(self):
        try:
            print("\033[1;31;40m 打开管理新闻页面 \033[0m")
            self.find_element(*self.newsMgt_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openSoftwareMgt(self):
        try:
            print("\033[1;31;40m 打开管理软件页面 \033[0m")
            self.find_element(*self.softwareMgt_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openPicMgt(self):
        try:
            print("\033[1;31;40m 打开管理图片页面 \033[0m")
            self.find_element(*self.picMgt_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openFlashMgt(self):
        try:
            print("\033[1;31;40m 打开管理FLASH页面 \033[0m")
            self.find_element(*self.flashMgt_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openArticleMgt(self):
        try:
            print("\033[1;31;40m 打开管理文章页面 \033[0m")
            self.find_element(*self.articleMgt_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openClassifiedsMgt(self):
        try:
            print("\033[1;31;40m 打开管理分类信息页面 \033[0m")
            self.find_element(*self.classifiedsMgt_loc).click()
        except BaseException as msg:
            print(msg)

    '''公共方法'''
    def type_checkPost(self,target_loc,mess):
        try:
            print("\033[1;35;0m 正在检查%s是否发布成功...\033[0m"%mess)
            self.find_element(*self.indexPage_loc).click()
            self.find_element(*target_loc).click()
            self.tempVar=str(self.randoma)
            eleText_loc = (By.PARTIAL_LINK_TEXT,self.tempVar)
            text=self.find_eleText(*eleText_loc)
            return text
        except BaseException as msg:
            print(msg)

    def type_comSearch(self,mess):
        try:
            print("\033[1;35;0m 关键词查询%s...\033[0m"%mess)
            self.find_element(*self.keyboard_loc).send_keys(self.tempVar)
            self.find_element(*self.submit2_loc).click()
            sleep(1)
            length=self.get_listCount(self.eleText1_loc)#因为返回的length已经被减1了，所以这里返回减1即可，不需要减2
            return (length - 1)
        except BaseException as msg:
            print(msg)

    def type_checkOject(self):
        try:
            print("\033[1;35;0m 从列表点击标题进入页面查看对象详情...\033[0m" )
            self.find_element(*self.keyboard_loc).clear()
            self.find_element(*self.submit2_loc).click()
            sleep(1)
            self.find_element(*self.eleFind_loc).click()
            sleep(1)
        except BaseException as msg:
            print(msg)

    def type_comComments(self,mess,modulePic):
        try:
            print("\033[1;35;0m 正在评论%s...\033[0m"%mess)
            self.type_getAccount()
            self.find_element(*self.saytext_loc).send_keys(self.randoma)
            self.get_sreenshot().insert_img(self.driver, modulePic)
            self.find_element(*self.imageField_loc).click()
        except BaseException as msg:
            print(msg)

    def type_checkComments(self,modulePic):
        try:
            print("\033[1;35;0m 检查是否评论成功...\033[0m")
            self.find_element(*self.commCheck_loc).click()
            self.get_sreenshot().insert_img(self.driver,modulePic)
        except BaseException as msg:
            print(msg)

    def type_comMod(self,mess,modulePic):
        try:
            print("\033[1;35;0m 正在修改%s...\033[0m"%mess)
            self.find_element(*self.keyboard_loc).clear()
            self.find_element(*self.submit2_loc).click()
            self.get_sreenshot().insert_img(self.driver,modulePic)
            self.find_element(*self.mod_loc).click()
            self.find_element(*self.title_loc).clear()
            self.type_getAccount()
            self.find_element(*self.title_loc).send_keys(self.randoma)
            self.find_element(*self.addnews_loc).click()
            sleep(3)
            text=self.find_eleText(*self.eleFind_loc)
            return text
        except BaseException as msg:
            print(msg)

    def type_comDel(self,mess):
        try:
            print("\033[1;35;0m 正在删除%s...\033[0m" % mess)
            self.find_element(*self.del_loc).click()
            sleep(2)
            self.type_getAlert()
        except BaseException as msg:
            print(msg)

    #选择栏目
    def type_comSelBanner(self,index):
        try:
            print("\033[1;35;0m 正在选择栏目...\033[0m" )
            self.find_element(*self.submit_loc).click()
            select_ele = Select(self.find_element(*self.classid_loc))
            select_ele.select_by_index(index)  # 选中第二个(index+1)option
            self.find_element(*self.submit_loc).click()
        except BaseException as msg:
            print(msg)


    '''新增'''
    def type_newsRelease(self):
        try:
            print("\033[1;35;0m 正在发布新闻...\033[0m")
            self.type_comSelBanner(1)
            self.type_getAccount()
            self.find_element(*self.title_loc).send_keys(self.randoma)
            self.find_element(*self.ftitle_loc).send_keys(self.randoma)
            self.find_element(*self.keyboard_loc).send_keys(self.randoma)
            self.find_element(*self.titlepicfile_loc).send_keys(self.userpicfile_path)
            self.find_element(*self.smalltext_loc).send_keys(self.randoma)
            self.find_element(*self.writer_loc).send_keys(self.randoma)
            self.find_element(*self.befrom_loc).send_keys(self.randoma)
            '''进入iframe框架'''
            iframe=self.find_element(*self.newsContent_loc)
            self.driver.switch_to.frame(iframe)
            self.find_element(*self.sendText_loc).send_keys(self.randoma)
            self.driver.switch_to.default_content()
            self.find_element(*self.addnews_loc).click()

        except BaseException as msg:
            print(msg)

    def type_softwareRelease(self):
        try:
            print("\033[1;35;0m 正在发布软件...\033[0m")
            self.type_comSelBanner(1)
            self.type_getAccount()
            self.find_element(*self.title_loc).send_keys(self.randoma)
            self.find_element(*self.keyboard_loc).send_keys(self.randoma)
            self.find_element(*self.titlepicfile_loc).send_keys(self.userpicfile_path)
            self.find_element(*self.softwriter_loc).send_keys(self.randoma)
            self.find_element(*self.homepage_loc).send_keys("https://www.baidu.com")
            self.find_element(*self.demo_loc).send_keys("https://www.baidu.com")
            self.find_element(*self.softfj_loc).send_keys(self.randoma)
            self.find_element(*self.check_loc).click()
            select_ele = Select(self.find_element(*self.select2_loc))
            select_ele.select_by_index(2)#对应rar文件
            self.find_element(*self.filesize_loc).send_keys(self.randoma)
            select_ele1 = Select(self.find_element(*self.select_loc))
            select_ele1.select_by_index(2)  # 对应kb
            self.find_element(*self.downpathfile_loc).send_keys(self.softwareUpload_path)
            self.find_element(*self.softsay_loc).send_keys(self.randoma)
            self.find_element(*self.addnews_loc).click()
        except BaseException as msg:
            print(msg)

    def type_swAddToBookmarks(self):
        try:
            print("\033[1;35;0m 将软件地址加入收藏夹...\033[0m")
            self.find_element(*self.addToBks_loc).click()
            sleep(1)
            lists=self.get_ranExcelText("bookmarksType.xlsx")
            self.randoma=lists[0]
            self.tempVar=lists[1]
            eleSelect = Select(self.find_element(*self.cid_loc))
            eleSelect.select_by_index(self.randoma + 1)
            list2=[]
            tels=self.find_elements(*self.cidOp_loc)
            for i in tels:
                list2.append(i.text)
                print("i.text is :%r"%i.text)
            if self.tempVar in list2:
                self.assertTip="匹配"
                print(self.assertTip)
            sleep(0.5)
            self.find_element(*self.submit_loc).click()
            sleep(1)
        except BaseException as msg:
            print(msg)

    def type_picRelease(self):
        try:
            print("\033[1;35;0m 正在上传图片...\033[0m")
            self.type_comSelBanner(1)
            self.type_getAccount()
            self.find_element(*self.title_loc).send_keys(self.randoma)
            self.find_element(*self.keyboard_loc).send_keys(self.randoma)
            self.find_element(*self.filesize_loc).send_keys(self.randoma)
            select_ele1 = Select(self.find_element(*self.select_loc))
            select_ele1.select_by_index(2)  # 对应kb
            self.find_element(*self.picsize_loc).send_keys(self.randoma)
            self.find_element(*self.picfbl_loc).send_keys(self.randoma)
            self.find_element(*self.picfrom_loc).send_keys(self.randoma)
            self.find_element(*self.titlepicfile_loc).send_keys(self.userpicfile_path)
            self.find_element(*self.picurlfile_loc).send_keys(self.userpicfile_path)
            self.find_element(*self.picsay_loc).send_keys(self.randoma)
            self.find_element(*self.addnews_loc).click()
        except BaseException as msg:
            print(msg)

    def type_flashRelease(self):
        try:
            print("\033[1;35;0m 正在上传Flash...\033[0m")
            self.type_comSelBanner(1)
            self.type_getAccount()
            self.find_element(*self.title_loc).send_keys(self.randoma)
            self.find_element(*self.keyboard_loc).send_keys(self.randoma)
            self.find_element(*self.titlepicfile_loc).send_keys(self.userpicfile_path)
            self.find_element(*self.flashwriter_loc).send_keys(self.randoma)
            self.find_element(*self.email_loc).send_keys(self.randoma)
            self.find_element(*self.filesize_loc).send_keys(self.randoma)
            select_ele1 = Select(self.find_element(*self.select_loc))
            select_ele1.select_by_index(2)  # 对应kb
            self.find_element(*self.flashurlfile_loc).send_keys(self.flashUpload_path)
            self.find_element(*self.flashsay_loc).send_keys(self.randoma)
            self.find_element(*self.addnews_loc).click()
        except BaseException as msg:
            print(msg)

    def type_articleRelease(self):
        try:
            print("\033[1;35;0m 正在发布新文章...\033[0m")
            self.type_comSelBanner(1)
            self.type_getAccount()
            self.find_element(*self.title_loc).send_keys(self.randoma)
            self.find_element(*self.ftitle_loc).send_keys(self.randoma)
            self.find_element(*self.keyboard_loc).send_keys(self.randoma)
            self.find_element(*self.titlepicfile_loc).send_keys(self.userpicfile_path)
            self.find_element(*self.smalltext_loc).send_keys(self.randoma)
            self.find_element(*self.writer_loc).send_keys(self.randoma)
            self.find_element(*self.befrom_loc).send_keys(self.randoma)
            '''进入iframe框架'''
            iframe = self.find_element(*self.newsContent_loc)
            self.driver.switch_to.frame(iframe)
            self.find_element(*self.sendText_loc).send_keys(self.randoma)
            self.driver.switch_to.default_content()
            self.find_element(*self.addnews_loc).click()
        except BaseException as msg:
            print(msg)

    def type_classifiedRelease(self):
        try:
            print("\033[1;35;0m 正在发布分类信息...\033[0m")
            self.type_comSelBanner(2)
            self.type_getAccount()
            self.find_element(*self.title_loc).send_keys(self.randoma)
            self.find_element(*self.smalltext_loc).send_keys(self.randoma)
            self.find_element(*self.titlepicfile_loc).send_keys(self.userpicfile_path)
            self.find_element(*self.mycontact_loc).send_keys(self.randoma)
            self.find_element(*self.addnews_loc).click()
        except BaseException as msg:
            print(msg)