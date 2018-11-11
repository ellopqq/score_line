#!/usr/bin/python
#coding=utf-8

import pdfkit

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None
}

path_wk = r'C:\Python27\wkhtmltox\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf = path_wk)
#pdfkit.from_url(url, r'D:\are you coding\pdf\taobao.pdf', configuration=config)

my_Son = u"杨宇哲真是个好孩子，有个好妈妈好爸爸!"
pdfkit.from_string(my_Son,'out.pdf', configuration=config, options=options)
my_wife = u"我有个好老婆"
pdfkit.from_string(my_wife,'out.pdf', configuration=config, options=options)