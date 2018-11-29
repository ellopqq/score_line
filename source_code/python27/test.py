#!/usr/bin/python
#coding=utf-8

import re
import xlrd
'''
from reportlab.pdfgen import canvas  
from reportlab.lib.units import cm  

c = canvas.Canvas("hello.pdf")  
c.drawString(9*cm, 22*cm, 'name: liutonhjuan     ' + 'gender: female')  
c.showPage()  
c.save()
'''
    
    
# Sample platypus document
# From the FAQ at reportlab.org/oss/rl-toolkit/faq/#1.1
'''
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_settings import defaultPageSize
from reportlab.lib.units import inch
    
def go():
    doc = SimpleDocTemplate("phello.pdf")
    Story = [Spacer(1,2*inch)]
    Style=getSampleStyleSheet()
    style = Style["Normal"]
    for i in range(100):
        bogustext = ("Paragraph number %s.        " % i) * 2
        p = Paragraph(bogustext, style)
        Story.append(p)
        Story.append(Spacer(1,0.2*inch))
    doc.build(Story)
    
if __name__ == "__main__":
    go()
'''


'''
test = u'正则表达式'
if re.search(u'表达式', test):
    print('ok')
else:
    print('failed')
'''
#source_data_fd = xlrd.open_workbook(r'C:\score_learn\python27\database\2019guokao.xls')
source_data_fd = xlrd.open_workbook(r'C:\Users\ellopqq\eclipse-workspace\score_line\database\2019guokao.xls')
#source_data_fd = xlrd.open_workbook(r'C:\Users\ellopqq\eclipse-workspace\score_line\source_code\python27\major_info.xls')
sheet_num = len(source_data_fd.sheet_names())
'''
for i in range(sheet_num):
    table = source_data_fd.sheet_by_index(i)
    nrows = table.nrows
    for j in range(2,nrows):
        t_value = table.cell(j, 13).value
        if t_value == u'仅限本科' or t_value == u'本科及以上'  or t_value == u'仅限硕士研究生' or t_value == u'硕士研究生及以上' or t_value == u'本科或硕士研究生':           
            continue
        elif t_value == u'大专或本科' or t_value == u'大专及以上'  or t_value == u'仅限博士研究生' :
            continue
        elif t_value == u'仅限大专' :
            continue
        else:
            print(t_value)    
           
'''
'''
for i in range(sheet_num):
    table = source_data_fd.sheet_by_index(i)
    nrows = table.nrows
    for j in range(2,nrows):
        t_value = table.cell(j, 12).value
        if  re.search(u'[、：；（）()，。/]+', t_value):           
            continue
        else:
            print(t_value)  
'''
test1 = [[1,2,3],[2,3,4],[1,3,4],[3,4,5]]
print(sorted(test1))

target_string = u'哲学'
#u'[、]+' + target_string + u'[、]+' + u'|'+ u'^' + target_string + u'[、]+'
#u'[、]+' + target_string + u'[、]+' + u'|'+ u'^' + target_string + u'[、]+' +  u'|' + u'[、]+' + target_string + u'$'
pattern = re.compile(u'[、]+' + target_string + u'[、]+')
pattern1 = re.compile(u'^' + target_string + u'[、]+')
pattern2 = re.compile(u'[、]+' + target_string + u'$')

def string_test():
    get_string = u'本科专业：会计学、财务管理；研究生专业：会计学'   
    a_list = re.split(u'[：、；]', get_string)
    for i in a_list:
        print(i)
    list_len = len(a_list)
    ben_pos = 0
    for i in a_list:
        if i == u'本科专业':
            break;
        ben_pos = ben_pos + 1

    suo_pos = 0
    for i in a_list:
        if i == u'研究生专业':
            break;
        suo_pos = suo_pos + 1
    print(ben_pos)
    print(suo_pos)
    new_list = []
    for i in range(ben_pos+1,suo_pos):
        if i == ben_pos+1:
            new_list.append(u'、' + a_list[i] + u'1、')
        else:
            new_list.append(a_list[i] + u'1、')
    for i in range(suo_pos+1, list_len):
        new_list.append(a_list[i] + u'2、')

    for i in new_list:
        print(i)
    print(''.join(new_list))



''' 
new_string = get_string.replace(u'本科', '')
print new_string
#get_string = u'runoob,runoob,runoob'
a_list = re.split(u'[：；]|本科专业|研究生专业|本科|研究生', get_string)
print a_list
for i in a_list:
    print(i)
'''    



