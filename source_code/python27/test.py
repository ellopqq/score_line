#!/usr/bin/python
#coding=utf-8
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
