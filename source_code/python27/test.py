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
source_data_fd = xlrd.open_workbook(r'C:\score_learn\python27\database\2019guokao.xls')
table = source_data_fd.sheet_by_index(0)
test_string = table.cell(3, 12).value

ele_list = list(test_string)
ele_list.insert(len(ele_list), u'、')
ele_list.insert(0, u'、')
test_string = ''.join(ele_list)
print(test_string)
#string = u'abcd、efgh、ijk'
target_string = u'哲学'
#u'[、]+' + target_string + u'[、]+' + u'|'+ u'^' + target_string + u'[、]+'
#u'[、]+' + target_string + u'[、]+' + u'|'+ u'^' + target_string + u'[、]+' +  u'|' + u'[、]+' + target_string + u'$'
pattern = re.compile(u'[、]+' + target_string + u'[、]+')
pattern1 = re.compile(u'^' + target_string + u'[、]+')
pattern2 = re.compile(u'[、]+' + target_string + u'$')
if pattern.search(test_string):
    print('match')
else:
    print('failed')
    





