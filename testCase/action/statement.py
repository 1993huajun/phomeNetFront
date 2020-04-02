# -- coding: utf-8 --
'''
\033[0m           默认字体正常显示，不高亮
\033[32;0m       红色字体正常显示
\033[1;32;0m  显示方式: 高亮    字体前景色：绿色  背景色：黑色
\033[0;31;46m  显示方式: 正常    字体前景色：红色  背景色：青色

1、打开网页提示
\033[1;31;40m       \033[0m     
2、读取文件
\033[1;33;0m       \033[0m    
3、执行方法
\033[1;35;0m       \033[0m    
       
'''
import openpyxl

workbook = openpyxl.load_workbook("DataSource\myfile.xlsx")
worksheet = workbook.worksheets[0]

# 在第一列之前插入一列
worksheet.insert_cols(1)  #

for index, row in enumerate(worksheet.rows):
    if index == 0:
        row[0].value = "编号"  # 每一行的一个row[0]就是第一列
    else:
        row[0].value = index
# 枚举出来是tuple类型，从0开始计数

workbook.save(filename="DataSource\myfile.xlsx")