#!/usr/bin/python
#coding=utf-8
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table,TableStyle
from reportlab.lib.units import inch
from reportlab.lib import  colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import elements

pdfmetrics.registerFont(TTFont('song', r"C:\tools\ziti\GB2312.ttf"))
Style=getSampleStyleSheet()

def generate_p(name_p,elements_p):
    pdf = SimpleDocTemplate(name_p+'.pdf')
    pdf.build(elements_p)

generate_p(u'刘同娟 ', elements.elements_pdf)