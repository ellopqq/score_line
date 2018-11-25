#!/usr/bin/python
#coding=utf-8

import xlrd

job_area_index = 20
job_department_index = 1
job_division_index = 2
job_stage_index = 4
job_major_index = 12
job_edu_index = 13
job_num_index = 11



Major_Enable = 1

source_data_fd = xlrd.open_workbook(r'C:\score_learn\python27\database\2019guokao.xls')
sheet_num = len(source_data_fd.sheet_names())
#sheet_num = 1

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

def major_analysis(data_string):
    major_flag = 0
    if data_string == u'不限':
        major_flag = 1
    return major_flag
        

def analysis_data(data_list):
    for i in range(sheet_num):
        table = source_data_fd.sheet_by_index(i)
        nrows = table.nrows
        for j in range(nrows):
            target_data_list = []
            m_flag = major_analysis(table.cell(j, job_major_index).value)
            if m_flag == 1:
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

