#!/usr/bin/python
#coding=utf-8
#https://www.reportlab.com/docs/reportlab-userguide.pdf
#http://zwsearch.huatu.com/search_el/searchzwk.php?act=grtj&page=1&param=1f6QvXMlLe8t8rpXI434%2B8s6i3me5tSDXqYMuXvKQPDYaoceX%2FbBV8U4kaXb0lvBJpvtLjSpMtrGjfyiUmV2kYCa%2FufAJGvozBV7vL%2F1ELPBzlzaM47IgZIKFWALCEkDkxmbH1nVC%2FTeROq1Gz4DLvXbOobplySxideHfg9TXa3Jw%2BYXtjg

from reportlab.platypus import Paragraph, SimpleDocTemplate, Table,TableStyle
from reportlab.lib.units import inch
from reportlab.lib import  colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from data_analysis import analysis_data

pdfmetrics.registerFont(TTFont('song', r"C:\tools\ziti\GB2312.ttf"))

def table_model(data):       
    column1_width = 0.55*inch
    column2_width = 0.95*inch
    column3_width = 0.95*inch
    column4_width = 0.95*inch
    column5_width = 1.46*inch
    column6_width = 0.6*inch
    column7_width = 0.4*inch
    column8_width = 0.4*inch
    column_width = [column1_width,column2_width,column3_width,column4_width,column5_width,column6_width,column7_width,column8_width]
    style = [
        ('FONTNAME', (0, 0), (-1, -1), 'song'),  # 字体
        ('FONTSIZE', (0, 0), (-1, 0), 10),  # 字体大小
        ('ALIGN',(0,0),(-1,-1),'CENTER'),       
        ('TEXTCOLOR',(0,0),(-1,0),colors.red),
        ('FONTSIZE', (0, 1), (-1, -1), 8),  # 字体大小
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black)
    ]
#    component_table = Table(data, 1*[0.3*inch,0.4*inch, 0.5*inch, 0.6*inch, 0.7*inch], 1*[0.3*inch],style=style)
    component_table = Table(data, column_width,style=style)
    return component_table

job_area = u'内蒙古'
job_department =  u'国家统计局内蒙古调查总队'
job_division = u'国家统计局内蒙古调查总队'
job_stage = u'达拉特调查队业务科室科员（1）'
job_major = u'生物医学工程'
job_edu = u'本科及以上'
job_num = u'1'
job_suitability = u'高'
'''
def table_elements_process(t_elements):
    elements_processed = []
    i = 0
    while i<8:
        ele_len = len(t_elements[i])
        ele_list = list(t_elements[i])
        if i == 4:
            ele_num = 12
        else:
            ele_num = 8
        
        if ele_len < ele_num+1:
            elements_processed.append(t_elements[i])
        else:           
            ele_pos = ele_num
            count = 0
            while ele_len >= ele_num+1:
                ele_list.insert(ele_pos, '\n')
                ele_len = ele_len - ele_num
                count = count + 1
                ele_pos = ele_pos + ele_num + count
            elements_processed.append(''.join(ele_list))
        i = i + 1
    return elements_processed
'''
#data1 = [job_area, job_department, job_division,job_stage, job_major, job_edu, job_num, job_suitability]                           
        
#data= [[u'地区',u'部门',u'用人司局',u'职位名称',u'专业要求', u'学历', u'招考\n人数', u'匹配度'],
#       table_elements_process(data1)
#      ]
target_data= [[u'地区',u'部门',u'用人司局',u'职位名称',u'专业要求', u'学历', u'招考\n人数', u'匹配度']]
table_job = table_model(analysis_data(target_data))

