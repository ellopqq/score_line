#!/usr/bin/python
#coding=utf-8

#http://zw.huatu.com/zhuanyeku/
#http://zw.offcn.com/gj/zhuanye/
import xlrd
import re

from pdf_input import pdf_input_info


def get_major_category():
    major_category = []
    get_major_cate1 = []
    get_major_cate2 = []
    flag = 0
    #major_fd = xlrd.open_workbook(r'C:\Users\ellopqq\eclipse-workspace\score_line\database\guokao_major.xlsx')
    major_fd = xlrd.open_workbook(r'C:\score_learn\python27\database\guokao_major.xlsx')
    major_table = major_fd.sheet_by_index(0)
    major_nrows = major_table.nrows
    if re.search(u'研究生', pdf_input_info['education']):
        major_column = 2
    elif pdf_input_info['education'] == u'本科':
        major_column = 3
    elif pdf_input_info['education'] == u'专科':
        major_column = 4
    else:
        major_column = 0
    for i in range(1, major_nrows):
        if re.search(pdf_input_info['major'], major_table.cell(i, major_column).value):
            flag = 1
            big_category_loop = i
            while big_category_loop > 0:
                if major_table.cell(big_category_loop, 0).value:
                    break;
                else:
                    big_category_loop = big_category_loop - 1
            get_major_cate1.append(major_table.cell(i, 1).value)
            get_major_cate2.append(major_table.cell(big_category_loop, 0).value)
           
    if flag == 1:
        major_category = [[pdf_input_info['major']],get_major_cate1, get_major_cate2] 
                                                       
    return major_category

major_category_info = get_major_category()

'''
a_re = get_major_category()
print(a_re[2][0])
print(a_re[2][1])
print(a_re[2][2])
'''

