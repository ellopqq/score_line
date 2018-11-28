#!/usr/bin/python
#coding=utf-8

import xlrd
import re
from input_analysis import major_category_info

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
        if re.search(major_category_info[0][0], data_string):
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
        

def analysis_data(data_list):
    for i in range(sheet_num):
        table = source_data_fd.sheet_by_index(i)
        nrows = table.nrows
        for j in range(nrows):
            target_data_list = []
            m_flag = major_analysis(table.cell(j, job_major_index).value)
            if m_flag != 0:
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


