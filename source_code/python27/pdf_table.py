#!/usr/bin/python
#coding=utf-8
#https://www.reportlab.com/docs/reportlab-userguide.pdf
#http://zwsearch.huatu.com/search_el/searchzwk.php?act=grtj&page=1&param=1f6QvXMlLe8t8rpXI434%2B8s6i3me5tSDXqYMuXvKQPDYaoceX%2FbBV8U4kaXb0lvBJpvtLjSpMtrGjfyiUmV2kYCa%2FufAJGvozBV7vL%2F1ELPBzlzaM47IgZIKFWALCEkDkxmbH1nVC%2FTeROq1Gz4DLvXbOobplySxideHfg9TXa3Jw%2BYXtjg

from reportlab.platypus import Paragraph, SimpleDocTemplate, Table,TableStyle
from reportlab.lib.units import inch
from reportlab.lib import  colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('song', r"C:\tools\ziti\GB2312.ttf"))

def table_model(data):   
    style = [
        ('FONTNAME', (0, 0), (-1, -1), 'song'),  # ����
        ('FONTSIZE', (0, 0), (-1, 0), 8),  # �����С
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
#    component_table = Table(data, 1*[0.3*inch,0.4*inch, 0.5*inch, 0.6*inch, 0.7*inch], 1*[0.3*inch],style=style)
    component_table = Table(data, 5*[1.3*inch], 1*[0.2*inch],style=style)
    return component_table

job_area = u'���ɹ�'
job_department =  u'����ͳ�ƾ����ɹŵ����ܶ�'
job_division = u'����ͳ�ƾ����ɹŵ����ܶ�'
job_stage = u'�����ص����ҵ����ҿ�Ա��1��'
job_major = u'����ѧ�࣬ͳ��ѧ��'
job_edu = u'���ޱ���'
job_num = u'1'
job_suitability = u'��'
data= [[u'����',u'����',u'����˾��',u'ְλ����',u'רҵҪ��', u'ѧ��', u'�п�����', u'ƥ���'],
       [u'���ɹ�', u'����ͳ�ƾ����ɹŵ����ܶ�', u'����ͳ�ƾ����ɹŵ����ܶ�', u'�����ص����ҵ����ҿ�Ա��1��', u'����ѧ�࣬ͳ��ѧ��', u'���ޱ���', u'1']
      ]
table_job = table_model(data)
#pdf = SimpleDocTemplate('ppf.pdf')
#pdf.multiBuild([z])
