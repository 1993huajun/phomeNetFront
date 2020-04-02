# -- coding: utf-8 --
from selenium.webdriver.common.by import By
from testCase.common.commonPage import Common
from testCase.model.getuserInfo import getYaml
from time import sleep
from ruamel import yaml
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''创建首页登录页面的类'''
class userMgtPage(Common):
    #u_para = "/news/" # 当调用open()方法时相当于构造的url="http://localhost/news/"

    # 设置定位器
    repassword_loc= (By.NAME,"repassword")
    submit3_loc = (By.NAME,"Submit3")
    email_loc = (By.NAME,"email")
    company_loc = (By.NAME,"company")
    truename_loc = (By.NAME,"truename")
    oicq_loc = (By.NAME,"oicq")
    msn_loc = (By.NAME,"msn")
    mycall_loc = (By.NAME,"mycall")
    fax_loc = (By.NAME,"fax")
    phone_loc = (By.NAME,"phone")
    homepage_loc = (By.NAME,"homepage")
    userpicfile_loc = (By.NAME,"userpicfile")
    address_loc = (By.NAME,"address")
    zip_loc = (By.NAME,"zip")
    saytext_loc = (By.NAME,"saytext")
    #注册
    register_loc = (By.NAME,"Submit2")
    option_loc = (By.XPATH,"//input[@value='3']")
    nextBtn_loc = (By.NAME,"button")
    #会员中心
    openVipAss_loc = (By.PARTIAL_LINK_TEXT, "站内消息")
    #修改资料
    editProfile_loc = (By.PARTIAL_LINK_TEXT, "修改资料")
    editSuc_loc=(By.PARTIAL_LINK_TEXT,"修改信息成功！")
    #会员中心-修改安全信息
    editPsd_loc = (By.PARTIAL_LINK_TEXT,"修改安全信息")
    oldpsd_loc = (By.ID,"oldpassword")
    #设置登录成功和失败的定位器
    loginPassAss_loc = (By.PARTIAL_LINK_TEXT,"我的空间")   # 登录成功后出现“我的空间”元素
    #收藏夹
    openBm_loc = (By.PARTIAL_LINK_TEXT,"收藏夹")
    addBmType_loc = (By.PARTIAL_LINK_TEXT,"管理分类")
    cname_loc = (By.ID,"cname")
    typeName_loc = (By.XPATH,"//table[@class='tableborder'][2]/tbody/tr[1]/td[2][contains(.,'分类名称')]")
    favaid_loc = (By.NAME,"favaid[]")
    submit4_loc = (By.XPATH,"//input[@name='Submit'][2]")
    eleText1_loc = (By.XPATH, "//table[@class='tableborder'][2]/tbody/tr[2]/td[2]/div/a")
    # cid1_loc = (By.XPATH,"//table[@class='tableborder'][2]/tbody/tr[3]/td/select")
    # cidOp1_loc = (By.XPATH, "//table[@class='tableborder'][2]/tbody/tr[3]/td/select/option")
    cid1_loc = (By.XPATH, "//select[@name='cid' and @style='']")
    cidOp1_loc = (By.XPATH, "//select[@name='cid' and @style='']/option")
    #收藏夹分类记录数
    eleTextMod_loc = (By.XPATH, "//table[@class='tableborder'][2]/tbody/tr/td[2]/div/input[3]")

    #好友列表
    openFriendList_loc = (By.PARTIAL_LINK_TEXT,"好友列表")
    addFriend_loc = (By.PARTIAL_LINK_TEXT,"添加好友")
    eleTextMod1_loc = (By.XPATH, "//table[@class='tableborder'][2]/tbody/tr/td[2]/div/input[4]")
    fname_loc = (By.NAME,"fname")
    fsay_loc = (By.NAME,"fsay")
    eleTextMod2_loc = (By.ID,"fsay[]")
    modLink_loc = (By.XPATH, "//table[@class='tableborder'][2]/tbody/tr[2]/td[4]/div/a[1]")
    delLink_loc = (By.XPATH, "//table[@class='tableborder'][2]/tbody/tr[2]/td[4]/div/a[2]")

    '''注册类'''
    # 普通会员注册
    def type_perRegisterT(self):
        try:
            print("\033[1;35;0m 普通会员注册...\033[0m")
            self.u_para=""
            self.open()
            self.find_element(*self.register_loc).click()
            sleep(1)
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[-1])
            self.find_element(*self.nextBtn_loc).click()
            #数据填充
            self.type_getAccount()
            self.type_username(self.randoma)
            #每次注册都会覆盖account.yaml中的account对应的文本值，同时确保用于添加好友时，账号是最新的
            data=getYaml('account.yaml')
            with open('F:\\Python\\phomeNetFront\\test_data\\yaml\\account.yaml', 'w', encoding="utf-8") as file:
                data['account']=self.randoma
                yaml.dump(data,file,Dumper=yaml.RoundTripDumper)
            self.type_setPerVip('0')
            self.type_submit()
        except BaseException as msg:
            print(msg)

    # 企业会员注册
    def type_comRegisterT(self):
        try:
            print("\033[1;35;0m 企业会员注册...\033[0m")
            self.u_para = ""
            self.open()
            self.find_element(*self.register_loc).click()
            sleep(1)
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[-1])
            self.find_element(*self.option_loc).click()
            self.find_element(*self.nextBtn_loc).click()
            #数据填充
            self.type_getAccount()
            self.type_username(self.randoma)
            self.type_setComVip('0')
            self.type_submit()
        except BaseException as msg:
            print(msg)


    '''打开页面'''


    '''修改类'''
    #修改资料
    def type_acc_editProfile(self):
        try:
            print("\033[1;35;0m 会员中心修改资料...\033[0m")
            self.find_element(*self.editProfile_loc).click()
            self.type_setPerVip('nopsd')
            self.find_element(*self.submit_loc).click()
        except BaseException as msg:
            print(msg)

    #新增或修改普通会员信息,动态变化的有两个，email和oicq
    def type_setPerVip(self,type):
        try:
            print("\033[1;35;0m update普通会员信息...\033[0m")
            data = getYaml('userInfo.yaml')
            print(data)
            if type != 'nopsd':
                self.type_password(data['reUserT']['password'])
                self.find_element(*self.repassword_loc).send_keys(data['reUserT']['repassword'])
                self.find_element(*self.email_loc).send_keys(str(self.randoma)+data['reUserT']['email'])
            self.find_element(*self.truename_loc).clear()
            self.find_element(*self.truename_loc).send_keys(data['reUserT']['truename'])
            self.find_element(*self.oicq_loc).clear()
            self.randoma=self.type_getAccount()
            self.find_element(*self.oicq_loc).send_keys(self.randoma)
            self.find_element(*self.msn_loc).clear()
            self.find_element(*self.msn_loc).send_keys(data['reUserT']['msn'])
            self.find_element(*self.mycall_loc).clear()
            self.find_element(*self.mycall_loc).send_keys(data['reUserT']['mycall'])
            self.find_element(*self.phone_loc).clear()
            self.find_element(*self.phone_loc).send_keys(data['reUserT']['phone'])
            self.find_element(*self.homepage_loc).clear()
            self.find_element(*self.homepage_loc).send_keys(data['reUserT']['homepage'])
            self.find_element(*self.userpicfile_loc).clear()
            self.find_element(*self.userpicfile_loc).send_keys(self.userpicfile_path)
            self.find_element(*self.address_loc).clear()
            self.find_element(*self.address_loc).send_keys(data['reUserT']['address'])
            self.find_element(*self.zip_loc).clear()
            self.find_element(*self.zip_loc).send_keys(data['reUserT']['zip'])
            self.find_element(*self.saytext_loc).clear()
            self.find_element(*self.saytext_loc).send_keys(data['reUserT']['saytext'])
            with open('F:\\Python\\phomeNetFront\\test_data\\yaml\\userInfo.yaml', 'w', encoding="utf-8") as file:
                data['reUserT']['oicq'] = self.randoma
                yaml.dump(data, file, Dumper=yaml.RoundTripDumper)
        except BaseException as msg:
            print(msg)

    #新增或修改企业会员信息
    def type_setComVip(self,type):
        try:
            print("\033[1;35;0m update企业会员信息...\033[0m")
            data = getYaml('userInfo.yaml')
            if type != 'nopsd':
                self.type_password(data['reComT']['password'])
                self.find_element(*self.repassword_loc).send_keys(data['reComT']['repassword'])
            self.find_element(*self.email_loc).send_keys(str(self.randoma) + data['reComT']['email'])
            self.find_element(*self.company_loc).send_keys(data['reComT']['company'])
            self.find_element(*self.truename_loc).send_keys(data['reComT']['truename'])
            self.find_element(*self.mycall_loc).send_keys(data['reComT']['mycall'])
            self.find_element(*self.oicq_loc).send_keys(data['reComT']['oicq'])
            self.find_element(*self.msn_loc).send_keys(data['reComT']['msn'])
            self.find_element(*self.fax_loc).send_keys(data['reComT']['fax'])
            self.find_element(*self.phone_loc).send_keys(data['reComT']['phone'])
            self.find_element(*self.homepage_loc).send_keys(data['reComT']['homepage'])
            self.find_element(*self.userpicfile_loc).send_keys(self.userpicfile_path)
            self.find_element(*self.address_loc).send_keys(data['reComT']['address'])
            self.find_element(*self.zip_loc).send_keys(data['reComT']['zip'])
            self.find_element(*self.saytext_loc).send_keys(data['reComT']['saytext'])
        except BaseException as msg:
            print(msg)

    def type_setPsd(self):
        try:
            print("\033[1;35;0m 修改密码...\033[0m")
            self.find_element(*self.editPsd_loc).click()
            print("randNo is :%d" %self.randoma)
            data=getYaml('userInfo.yaml')
            self.find_element(*self.oldpsd_loc).send_keys(data['loUser']['password'])
            sleep(1)
            self.find_element(*self.password_loc).send_keys(self.randoma)
            self.find_element(*self.repassword_loc).send_keys(self.randoma)
            sleep(1)
            self.find_element(*self.submit_loc).click()
            with open('F:\\Python\\phomeNetFront\\test_data\\yaml\\userInfo.yaml', 'w', encoding="utf-8") as file:
                data['loUser']['password'] = self.randoma
                data['loUser']['repassword'] = self.randoma
                yaml.dump(data, file, Dumper=yaml.RoundTripDumper)
        except BaseException as msg:
            print(msg)


    '''收藏夹'''
    def type_openBookmarks(self):
        try:
            print("\033[1;31;40m 打开收藏夹管理页面 \033[0m")
            sleep(1)
            self.find_element(*self.openBm_loc).click()
        except BaseException as msg:
            print(msg)

    def type_openBookmarksType(self):
        try:
            print("\033[1;31;40m 打开收藏夹分类管理页面 \033[0m")
            self.find_element(*self.addBmType_loc).click()
        except BaseException as msg:
            print(msg)

    def type_addBookmarksType(self):
        try:
            print("\033[1;35;0m 添加收藏夹分类...\033[0m")
            count1 = self.get_listCount(self.eleText_loc)
            self.type_getAccount()
            self.find_element(*self.cname_loc).send_keys(self.randoma)
            self.find_element(*self.submit_loc).click()
            self.append_excel("bookmarksType.xlsx", str(self.randoma))
            return count1
        except BaseException as msg:
            print(msg)

    def type_modBookmarksType(self):
        try:
            print("\033[1;35;0m 修改收藏夹分类...\033[0m")
            self.type_getAccount()
            self.find_element(*self.eleTextMod_loc).clear()
            self.find_element(*self.eleTextMod_loc).send_keys(self.randoma)
            self.find_element(*self.submit2_loc).click()
            sleep(1)
            text=self.find_element(*self.eleTextMod_loc).get_attribute('value')
            self.mod_excel("bookmarksType.xlsx", str(self.randoma))
            return text
        except BaseException as msg:
            print(msg)

    def type_delBookmarksType(self):
        try:
            print("\033[1;35;0m 删除收藏夹分类...\033[0m")
            self.find_element(*self.submit3_loc).click()
            self.type_getAlert()
            row = self.get_ExcelRow("bookmarksType.xlsx")
            self.del_excel("bookmarksType.xlsx", row)
        except BaseException as msg:
            print(msg)

    def type_delBookmarksInfo(self):
        try:
            print("\033[1;35;0m 删除收藏夹收藏的信息...\033[0m")
            self.find_element(*self.favaid_loc).click()
            sleep(1)
            element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.submit4_loc))
            self.driver.execute_script("arguments[0].click();",element)
            # self.find_element(*self.submit4_loc).click()
            sleep(1)
            self.type_getAlert()
        except BaseException as msg:
            print(msg)

    def type_transferBookmarksInfo(self):
        try:
            print("\033[1;35;0m 将信息转移到另一个收藏夹...\033[0m")
            self.find_element(*self.favaid_loc).click()
            tuples = self.get_ranExcelText("bookmarksType.xlsx")
            row = tuples[0]
            text = tuples[1]
            '''这里无法使用id、Xpath[@id='**']对select进行定位,用相对路径'''
            s=self.find_elements(*self.cid_loc)
            tels=s[1].find_elements(*self.cidOp_loc)
            # tels = self.find_elements(*self.cidOp1_loc)
            lists = []
            for i in tels:
                lists.append(i.text)
            print("list is :%r" % lists)
            if text in lists:
                print("text in lists")
                s[1].click()
                select_ele = Select(self.find_element(*self.cid1_loc))
                select_ele.select_by_index(row + 1)  # 选中从excel随机得到的分组
                self.get_sreenshot().insert_img(self.driver,"userMgt_11transferBookmarksInfo00.png")
                self.find_element(*self.submit_loc).click()
                self.type_getAlert()
                return (row + 1)
        except BaseException as msg:
            print(msg)

    def type_checkBmInfoTransfer(self,row):
        try:
            select_ele = Select(self.find_element(*self.cid_loc))
            select_ele.select_by_index(row)  #判断是否转移成功
        except BaseException as msg:
            print(msg)


    '''好友列表'''
    def type_openFriendList(self):
        try:
            print("\033[1;31;40m 打开好友列表管理页面 \033[0m")
            self.find_element(*self.openFriendList_loc).click()
        except BaseException as msg:
            print(msg)

    def type_addFriendType(self):
        try:
            self.find_element(*self.addBmType_loc).click()
            print("\033[1;35;0m 添加好友分类...\033[0m")
            count1 = self.get_listCount(self.eleText_loc)
            self.type_getAccount()
            self.find_element(*self.cname_loc).send_keys(self.randoma)
            self.find_element(*self.submit_loc).click()
            self.append_excel("friendType.xlsx",str(self.randoma))
            self.get_excelList("friendType.xlsx")
            sleep(3)
            return count1
        except BaseException as msg:
            print(msg)

    def type_modFriendType(self):
        try:
            print("\033[1;35;0m 修改好友分类...\033[0m")
            self.type_getAccount()
            self.find_element(*self.eleTextMod1_loc).clear()
            self.find_element(*self.eleTextMod1_loc).send_keys(self.randoma)
            self.find_element(*self.submit2_loc).click()
            sleep(1)
            text=self.find_element(*self.eleTextMod1_loc).get_attribute('value')
            self.mod_excel("friendType.xlsx",str(self.randoma))
            self.get_excelList("friendType.xlsx")
            return text
        except BaseException as msg:
            print(msg)

    def type_delFriendType(self):
        try:
            print("\033[1;35;0m 删除好友分类...\033[0m")
            self.find_element(*self.submit3_loc).click()
            self.type_getAlert()
            row=self.get_ExcelRow("friendType.xlsx")
            self.del_excel("friendType.xlsx",row)
        except BaseException as msg:
            print(msg)

    def type_addFriend(self):
        try:
            self.type_openFriendList()
            count1 = self.get_listCount(self.eleText_loc)
            self.find_element(*self.addFriend_loc).click()
            print("\033[1;35;0m 添加好友...\033[0m")
            data=getYaml("account.yaml")
            self.randoma=data['account']
            print("randma is :%s"%self.randoma)
            self.find_element(*self.fname_loc).send_keys(self.randoma)
            # 为好友选择分组
            tuples=()#用元组接收get_ranExcelText()返回的元组，第一个值是行数，第二个值是行数对应的文本值（分组）
            tuples=self.get_ranExcelText("friendType.xlsx")
            row=tuples[0]
            text=tuples[1]
            tels=self.find_elements(*self.cidOp_loc)
            lists = []
            for i in tels:
                lists.append(i.text)
            print("list is :%r" % lists)
            if text in lists:
                print("text in lists")
                self.find_element(*self.cid_loc).click()
                select_ele=Select(self.find_element(*self.cid_loc))
                select_ele.select_by_index(row+1)#选中从excel随机得到的分组

            self.find_element(*self.fsay_loc).send_keys(self.randoma)
            self.find_element(*self.submit_loc).click()
            self.append_excel("friend.xlsx",str(self.randoma))
            return count1
        except BaseException as msg:
            print(msg)

    def type_modFriend(self):
        try:
            print("\033[1;35;0m 修改好友分类...\033[0m")
            self.type_getAccount()
            self.find_element(*self.modLink_loc).click()
            self.find_element(*self.fsay_loc).clear()
            self.find_element(*self.fsay_loc).send_keys(self.randoma)
            self.find_element(*self.submit_loc).click()
            sleep(1)
            text=self.find_element(*self.eleTextMod2_loc).get_attribute('value')
            return text
        except BaseException as msg:
            print(msg)

    def type_delFriend(self):
        try:
            print("\033[1;35;0m 删除好友...\033[0m")
            self.find_element(*self.delLink_loc).click()
            self.type_getAlert()
            row=self.get_ExcelRow("friend.xlsx")
            self.del_excel("friend.xlsx",row)
        except BaseException as msg:
            print(msg)
