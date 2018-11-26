#!/usr/bin/python
#coding=utf-8

import re
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


test = u'正则表达式'
if re.search(u'表达式', test):
    print('ok')
else:
    print('failed')
    
a_dict = {u'司法助理': u'法律务实类', u'法律文秘': u'法律务实类', u'司法警务': u'法律务实类'}


a_dict1 = {u'法律务实类': u'法律大类'}

key = a_dict[u'法律文秘']
print(key)

key1 = a_dict1[key]
print(key1)




