#!/usr/bin/python
#coding=utf-8
#from reportlab.pdfgen import canvas
#https://www.cnblogs.com/hujq1029/p/7767980.html
#http://www.downcc.com/k/ttfziti/   ��������
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('song', "C:\score_learn\python27\source_code\python27\GB2312.ttf"))

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph,SimpleDocTemplate
from reportlab.lib import  colors

Style=getSampleStyleSheet()

bt = Style['Normal']     #�������ʽ
bt.fontName='song'    #ʹ�õ�����
bt.fontSize=14            #�ֺ�
bt.wordWrap = 'CJK'    #������֧���Զ����У�'CJK'������ģʽ���У�����Ӣ���л�ضϵ�������Ķ����ѣ��ɸ�Ϊ'Normal'
bt.firstLineIndent = 32  #������֧�ֵ�һ�п�ͷ�ո�
bt.leading = 20             #�������������о�

ct=Style['Normal']
# ct.fontName='song'
ct.fontSize=12
ct.alignment=1             #����

ct.textColor = colors.red

my_str = u"�������Ǹ��ñ������и��ðְֺ����裡"
t = Paragraph(my_str, bt)
pdf=SimpleDocTemplate('ppff.pdf')
pdf.multiBuild([t])
'''
def hello():
    c = canvas.Canvas("helloworld.pdf")
    c.drawString(100,100,"��ã�")
    c.showPage()
    c.save()
hello()
'''