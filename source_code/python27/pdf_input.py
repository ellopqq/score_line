#!/usr/bin/python
#coding=utf-8
from function_lib import insert_space
NAME_INSERT_SPACE = 8
POLI_INSERT_SPACE = 5

pdf_input_info = {}
pdf_input_info['name'] = u'刘同娟'
pdf_input_info['gender'] = u'女'
pdf_input_info['nationality'] = u'汗'
pdf_input_info['birth'] = '1986-11-12'
pdf_input_info['political_status'] = u'中共党员'
pdf_input_info['political_status_time'] = '2012-09'
pdf_input_info['education'] = u'硕士研究生'
pdf_input_info['bachelor'] = u'硕士'
pdf_input_info['major'] = u'生物医学工程'
pdf_input_info['working_years'] = u'四年'
pdf_input_info['domicile'] = u'江苏省南京市江宁区'
pdf_input_info['is_san'] = u'否'
pdf_input_info['is_west'] = u'否'
pdf_input_info['is_village'] = u'是'
pdf_input_info['application_area'] = u'江苏省南京市'
pdf_input_info['certificate'] = u'英语六级'

def pdf_head_insert_space():    
    return insert_space(3)

def pdf_name_insert_space(p_name): 
    name_len = len(p_name)   
    if 1< name_len < 5:
        return insert_space(NAME_INSERT_SPACE-name_len)      

def pdf_political_insert_space(p_political): 
    political_len = len(p_political)   
    if 1< political_len < 5:
        return insert_space(POLI_INSERT_SPACE-political_len)     
    
       
#'<br>': 强制换行
pdf_name = u'姓\0\0名： '+ pdf_input_info['name'] + pdf_name_insert_space(pdf_input_info['name'])
pdf_gender = u'性\0\0别： ' + pdf_input_info['gender'] + insert_space(7)
pdf_minzu = u'民\0\0族： '+ pdf_input_info['nationality'] 
pdf_name_line = pdf_name + pdf_gender + pdf_minzu  

pdf_birth = u'出生年月： '+ pdf_input_info['birth'] + insert_space(3)
pdf_political = u'政治面貌： '+ pdf_input_info['political_status'] + pdf_name_insert_space(pdf_input_info['political_status'])
#pdf_political_time = u'入党（团）时间： '+ pdf_input_info['political_status_time']
pdf_education = u'最高学历： '+ pdf_input_info['education']
pdf_birth_line = pdf_birth + pdf_political + pdf_education

pdf_bachelor = u'学\0\0位： '+ pdf_input_info['bachelor'] + pdf_name_insert_space(pdf_input_info['bachelor'])
pdf_work = u'工作年限： '+ pdf_input_info['working_years'] + pdf_name_insert_space(pdf_input_info['working_years'])
pdf_major = u'专\0\0业： '+ pdf_input_info['major']
pdf_education_line = pdf_bachelor + pdf_work + pdf_major

pdf_san = u'三支一扶计划： '+ pdf_input_info['is_san'] + insert_space(5)
pdf_west = u'大学生志愿服务西部计划：'+ pdf_input_info['is_west']
pdf_village = u'大学生村官： '+ pdf_input_info['is_village'] + insert_space(6)
pdf_san_line = pdf_san + pdf_village + pdf_west

pdf_domicile_line = u'户籍所在地\0： '+ pdf_input_info['domicile']

pdf_area_line = u'报名地区\0\0： '+ pdf_input_info['application_area']

pdf_certificate_line = u'所获证书\0\0： '+ pdf_input_info['certificate']















