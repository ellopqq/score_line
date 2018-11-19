#!/usr/bin/python
#coding=utf-8
from function_lib import insert_space

pdf_input_info = {}
pdf_input_info['姓名'] = u'刘同娟 '
pdf_input_info['性别'] = u'女'
pdf_input_info['民族'] = u'汗'

pdf_name = u'        姓名，                        你好   \n   '+ pdf_input_info['姓名'] + insert_space(30) + '<br/>'
pdf_gender = u'性别： ' + pdf_input_info['性别'] + insert_space(10)
pdf_minzu = u'民族： '+ pdf_input_info['民族'] 
pdf_name_line = pdf_name + pdf_gender + pdf_minzu  
#text = '<para autoLeading="off" fontSize=9><br/><br/><br/><b><font face="simsun">当日授信信息表：</font></b><br/></para>' 
print(pdf_name_line)