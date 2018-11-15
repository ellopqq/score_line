#!/usr/bin/python
#coding=utf-8
#from reportlab.pdfgen import canvas
#https://www.cnblogs.com/hujq1029/p/7767980.html
#http://www.downcc.com/k/ttfziti/   字体下载
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

#pdfmetrics.registerFont(TTFont('song', r"C:\score_learn\python27\source_code\python27\GB2312.ttf"))
pdfmetrics.registerFont(TTFont('song', r"C:\tools\ziti\GB2312.ttf"))

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph,SimpleDocTemplate
from reportlab.lib import  colors

Style=getSampleStyleSheet()

bt = Style['Normal']     #字体的样式
bt.fontName='song'    #使用的字体
bt.fontSize=10            #字号
bt.wordWrap = 'CJK'    #该属性支持自动换行,CJK是中文模式下换行，用于英文会截断单词造成阅读困难，可以改成'Noraml'
bt.firstLineIndent = 2  #该属性支持第一行开头空格
bt.leading = 20             #该属性是设置行距

ct=Style['Normal']
# ct.fontName='song'
ct.fontSize=12
ct.alignment=0             #居中

ct.textColor = colors.red

my_str = u'''人这一生，选择往往比努力更重要！'''
my_str1 = u"哈哈，恭喜，你成功了一半"
t = Paragraph(my_str, bt)
t1 = Paragraph(my_str1, bt)
pdf=SimpleDocTemplate('ppff.pdf')
pdf.multiBuild([t,t1])

