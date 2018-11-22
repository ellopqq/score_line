#!/usr/bin/python
#coding=utf-8
from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate, Table,TableStyle
from reportlab.lib.units import inch
from reportlab.lib import  colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from function_lib import insert_space
from pdf_input import pdf_name_line, pdf_birth_line,pdf_education_line
from pdf_input import pdf_area_line, pdf_certificate_line,pdf_san_line,pdf_domicile_line
from pdf_table import table_job

elements_pdf = []
pdfmetrics.registerFont(TTFont('song', r"C:\tools\ziti\GB2312.ttf"))
Style=getSampleStyleSheet()

Style.add(ParagraphStyle(name='pdf_Title',
                              fontName='song',
                              fontSize=12,
                              alignment=1,
                              leading=12)
               )

Style.add(ParagraphStyle(name='pdf_Begin',
                              fontName='song',
                              fontSize=10,
                              alignment=0,
                              textColor = colors.red,
                              leading=12)
               )

Style.add(ParagraphStyle(name='pdf_Info',
                              fontName='song',
                              fontSize=13,
                              alignment=0, 
                              textColor = colors.blue,
                              backColor = colors.lightgrey,
#                             backColor = colors.lawngreen,
                              wordWrap = 'CJK',                     
                              leading=15)
               )

Style.add(ParagraphStyle(name='pdf_Body',
                              fontName='song',
                              fontSize=10,
                              alignment=0, 
                              wordWrap = 'CJK',                     
                              leading=12)
               )

pdf_Title = u"上岸报考分析报告"
pdf_Begin = u"人这一生，选择往往比努力更重要！"
pdf_infor = u'基本信息'

elements_pdf.append(Paragraph(pdf_Title,Style['pdf_Title']))
elements_pdf.append(Spacer(0,20))
elements_pdf.append(Paragraph(pdf_Begin,Style['pdf_Begin']))
elements_pdf.append(Spacer(0,7))
elements_pdf.append(Paragraph(pdf_infor,Style['pdf_Info']))
elements_pdf.append(Spacer(0,7))
elements_pdf.append(Paragraph(pdf_name_line,Style['pdf_Body']))
elements_pdf.append(Spacer(0,7))
elements_pdf.append(Paragraph(pdf_birth_line,Style['pdf_Body']))
elements_pdf.append(Spacer(0,7))
elements_pdf.append(Paragraph(pdf_education_line,Style['pdf_Body']))
elements_pdf.append(Spacer(0,7))
elements_pdf.append(Paragraph(pdf_san_line,Style['pdf_Body']))
elements_pdf.append(Spacer(0,7))
elements_pdf.append(Paragraph(pdf_domicile_line,Style['pdf_Body']))
elements_pdf.append(Spacer(0,7))
elements_pdf.append(Paragraph(pdf_area_line,Style['pdf_Body']))
elements_pdf.append(Spacer(0,7))
elements_pdf.append(Paragraph(pdf_certificate_line,Style['pdf_Body']))
elements_pdf.append(Spacer(0,7))
elements_pdf.append(table_job)



