#!/usr/bin/python
#coding=utf-8
#https://www.reportlab.com/docs/reportlab-userguide.pdf
#http://zwsearch.huatu.com/search_el/searchzwk.php?act=grtj&page=1&param=1f6QvXMlLe8t8rpXI434%2B8s6i3me5tSDXqYMuXvKQPDYaoceX%2FbBV8U4kaXb0lvBJpvtLjSpMtrGjfyiUmV2kYCa%2FufAJGvozBV7vL%2F1ELPBzlzaM47IgZIKFWALCEkDkxmbH1nVC%2FTeROq1Gz4DLvXbOobplySxideHfg9TXa3Jw%2BYXtjg

from reportlab.platypus import Paragraph, SimpleDocTemplate, Table,TableStyle
from reportlab.lib.units import inch
from reportlab.lib import  colors

def table_model():
    data= [['00', '01', '02', '03', '04'],
           ['10', '11', '12', '13', '14'],
           ['20', '21', '22', '23', '24'],
           ['30', '31', '32', '33', '34']]
    style = [
        ('ALIGN',(1,1),(-2,-2),'RIGHT'),
        ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
        ('VALIGN',(0,0),(0,-1),'TOP'),
        ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
        ('ALIGN',(0,-1),(-1,-1),'CENTER'),
        ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
        ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black)
    ]
    component_table = Table(data, 5*[0.3*inch,0.4*inch, 0.5*inch, 0.6*inch, 0.7*inch], 4*[0.4*inch],style=style)

    return component_table


z = table_model()
pdf = SimpleDocTemplate('ppf.pdf')
pdf.multiBuild([z])
