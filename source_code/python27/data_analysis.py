#!/usr/bin/python
#coding=utf-8

import xlrd
import re
from input_analysis import major_category_info
from pdf_input import pdf_input_info

job_area_index = 20
job_department_index = 1
job_division_index = 2
job_stage_index = 4
job_major_index = 12
job_edu_index = 13
job_num_index = 11

Major_Enable = 1

job_major_test = u'生物医学工程'

#source_data_fd = xlrd.open_workbook(r'C:\score_learn\python27\database\2019guokao.xls')
source_data_fd = xlrd.open_workbook(r'C:\Users\ellopqq\eclipse-workspace\score_line\database\2019guokao.xls')
processed_data_fd = xlrd.open_workbook(r'C:\Users\ellopqq\eclipse-workspace\score_line\source_code\python27\major_info.xls')
sheet_num = len(source_data_fd.sheet_names())
#sheet_num = 1

def table_elements_process(t_elements):
    elements_processed = []
    i = 0
    while i<8:
        ele_len = len(t_elements[i])
        ele_list = list(t_elements[i])
        if i == 0:
            ele_num = 4
        elif i == 4:
            ele_num = 12
        elif i == 5:
            ele_num = 5
        else:
            ele_num = 8
        
        if ele_len < ele_num+1:
            elements_processed.append(t_elements[i])
        else:           
            ele_pos = ele_num
            while ele_len >= ele_num+1:
                ele_list.insert(ele_pos, '\n')
                ele_len = ele_len - ele_num
                ele_pos = ele_pos + ele_num + 1
            elements_processed.append(''.join(ele_list))
        i = i + 1
    return elements_processed

def major_analysis(data_string):
    major_flag = 0
    len_major = len(major_category_info)
    if len_major > 0:
        if re.search(u'[、]+' + major_category_info[0][0] + u'[、]+', data_string):
            major_flag = 1
            return major_flag
        for i in range(len(major_category_info[1])):
            if re.search(major_category_info[1][i], data_string):
                major_flag = 2
                return major_flag
        for i in range(len(major_category_info[2])):
            if re.search(major_category_info[2][i], data_string):
                major_flag = 3
                return major_flag
    if re.search(u'不限', data_string):
        major_flag = 4
        return major_flag
    return major_flag
        
def edu_analysis(edu_value):
    edu_flag = 0
    if pdf_input_info['education'] == u'硕士研究生' :
        if u'仅限硕士研究生' == edu_value:
            edu_flag = 1
        elif edu_value == u'硕士研究生及以上' :
            edu_flag = 2
        elif edu_value == u'本科或硕士研究生' :
            edu_flag = 3
        elif edu_value == u'本科及以上' :
            edu_flag = 4
        elif edu_value == u'大专及以上' :
            edu_flag = 5
        else:
            edu_flag = 0
    elif pdf_input_info['education'] == u'本科' :
        if edu_value == u'仅限本科' :
            edu_flag = 1
        elif edu_value == u'大专或本科' :
            edu_flag = 2        
        elif edu_value == u'本科或硕士研究生' :
            edu_flag = 3
        elif edu_value == u'本科及以上' :
            edu_flag = 4
        elif edu_value == u'大专及以上' :
            edu_flag = 5
        else:
            edu_flag = 0
    elif pdf_input_info['education'] == u'大专' :
        if edu_value == u'仅限大专' :
            edu_flag = 1
        elif edu_value == u'大专或本科' :
            edu_flag = 2        
        elif edu_value == u'大专及以上' :
            edu_flag = 3
        else:
            edu_flag = 0
    elif pdf_input_info['education'] == u'博士研究生' :
        if edu_value == u'仅限博士研究生' :
            edu_flag = 1
        elif edu_value == u'硕士研究生及以上' :
            edu_flag = 2        
        elif edu_value == u'本科及以上' :
            edu_flag = 3
        elif edu_value == u'大专及以上' :
            edu_flag = 4
        else:
            edu_flag = 0
    
    return edu_flag        
            
def analysis_data(data_list):
    judge_list = []
    for i in range(sheet_num):
        table = source_data_fd.sheet_by_index(i)
        nrows = table.nrows
        processed_table = processed_data_fd.sheet_by_index(i)
        for j in range(nrows):
            target_data_list = []
            m_flag = major_analysis(processed_table.cell(j, job_major_index).value)
            edu_flag = edu_analysis(table.cell(j, job_edu_index).value)
            total_flag = m_flag*edu_flag
            if total_flag != 0:
                judge_list.append([total_flag, i, j])
            '''
            if m_flag*edu_flag == 1:
                target_data_list.append(table.cell(j, job_area_index).value)
                target_data_list.append(table.cell(j, job_department_index).value)
                target_data_list.append(table.cell(j, job_division_index).value)
                target_data_list.append(table.cell(j, job_stage_index).value)
                target_data_list.append(table.cell(j, job_major_index).value)
                target_data_list.append(table.cell(j, job_edu_index).value)
                target_data_list.append(table.cell(j, job_num_index).value)
                target_data_list.append(u'高')
                data_list.append(table_elements_process(target_data_list))
            else:
                continue
            '''
    judge_list = sorted(judge_list)
    table_list = []
    for i in range(sheet_num):
        table_list.append(source_data_fd.sheet_by_index(i))
    
    count = 0
    for list_index in judge_list:
        count = count + 1
        target_data_list = []
        target_data_list.append(table_list[list_index[1]].cell(list_index[2], job_area_index).value)
        target_data_list.append(table_list[list_index[1]].cell(list_index[2], job_department_index).value)
        target_data_list.append(table_list[list_index[1]].cell(list_index[2], job_division_index).value)
        target_data_list.append(table_list[list_index[1]].cell(list_index[2], job_stage_index).value)
        target_data_list.append(table_list[list_index[1]].cell(list_index[2], job_major_index).value)
        target_data_list.append(table_list[list_index[1]].cell(list_index[2], job_edu_index).value)
        target_data_list.append(table_list[list_index[1]].cell(list_index[2], job_num_index).value)
        target_data_list.append(str(list_index[0]))
        data_list.append(table_elements_process(target_data_list))
        if count>20:
            break
        
    return data_list

'''
print(major_analysis(u'不限'))
print(major_analysis(u'工学'))
print(major_analysis(u'理学'))
print(major_analysis(u'医学'))
print(major_analysis(u'基础医学类'))
print(major_analysis(u'生物医学工程类'))
print(major_analysis(u'生物科学类'))
print(major_analysis(u'生物医学工程'))
print(major_analysis(u'生物工程类'))
'''


