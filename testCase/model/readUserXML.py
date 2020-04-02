# -- coding: utf-8 --
from xml.dom import minidom
from time import ctime

class readUserXML():
    def test_readUserInfo(self):
        print("\033[1;33;0m 开始读user_psd.xml%s\033[0m"%ctime())
        dom=minidom.parse('F:\\Python\\dslO2O\\test_data\\user_psd.xml')
        root = dom.documentElement

        remarks=root.getElementsByTagName('remark')
        usernames=root.getElementsByTagName('username')
        passwords=root.getElementsByTagName('password')

        array =[['' for col in range(2)] for row in range(4)]
        array1 =[['' for col in range(2)] for row in range(4)]
        for i in range(4):
            for j in range(2):
                array[i][0] = usernames[i].firstChild.data
            array[i][j]=passwords[i].firstChild.data
        print("\033[1;33;0m 结束读取user_info.xml%s\033[0m" % ctime())
        return array




