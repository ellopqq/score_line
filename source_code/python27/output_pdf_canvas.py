#!/usr/bin/python
#coding=utf-8
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch 

#pdfmetrics.registerFont(TTFont('song', r"C:\score_learn\python27\source_code\python27\GB2312.ttf"))
pdfmetrics.registerFont(TTFont('song', r"C:\tools\ziti\GB2312.ttf"))

def hello():
    my_str1 = u"你好"
    my_str2 = u"世界"
    c = canvas.Canvas("helloworld.pdf")
    c.setFont('song',10)
    textobject = c.beginText()
    textobject.setTextOrigin(inch,11*inch)
    textobject.textLines(my_str1) 
    textobject.textLines(my_str2) 
    c.drawText(textobject)
    c.showPage()
    c.save()
hello()