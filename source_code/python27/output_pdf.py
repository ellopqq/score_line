#!/usr/bin/python
#coding=utf-8
#from reportlab.pdfgen import canvas
#https://www.cnblogs.com/hujq1029/p/7767980.html
#http://www.downcc.com/k/ttfziti/   字体下载
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('song', "C:\score_learn\python27\source_code\python27\GB2312.ttf"))

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph,SimpleDocTemplate
from reportlab.lib import  colors

Style=getSampleStyleSheet()

bt = Style['Normal']     #字体的样式
bt.fontName='song'    #使用的字体
bt.fontSize=14            #字号
bt.wordWrap = 'CJK'    #该属性支持自动换行，'CJK'是中文模式换行，用于英文中会截断单词造成阅读困难，可改为'Normal'
bt.firstLineIndent = 32  #该属性支持第一行开头空格
bt.leading = 20             #该属性是设置行距

ct=Style['Normal']
# ct.fontName='song'
ct.fontSize=12
ct.alignment=1             #居中

ct.textColor = colors.red

my_str = u"杨宇哲是个好宝宝，有个好爸爸好妈妈！"
t = Paragraph(my_str, bt)
pdf=SimpleDocTemplate('ppff.pdf')
pdf.multiBuild([t])
'''
def hello():
    c = canvas.Canvas("helloworld.pdf")
    c.drawString(100,100,"你好！")
    c.showPage()
    c.save()
hello()
'''