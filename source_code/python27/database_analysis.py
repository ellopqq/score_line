#!/usr/bin/python
#coding=utf-8

import re
import xlrd
import xlwt

def find_target_row_conlumn(target_string, table):
    target_row_col = []
    nrows = table.nrows
    cols = table.ncols
    for i in range(nrows):
        for j in range(cols):
            if target_string == table.cell(i,j).value:
                target_row_col.append(i)
                target_row_col.append(j)
                return target_row_col
    return target_row_col         

def muti_catlog_analysis(muti_value):
    element_list = re.split(u'[：、；]', muti_value)
    list_len = len(element_list)
    ben_pos = 0
    for i in element_list:
        if i == u'本科专业' or i == u'本科':
            break;
        ben_pos = ben_pos + 1

    suo_pos = 0
    for i in element_list:
        if i == u'研究生专业' or i == u'研究生':
            break;
        suo_pos = suo_pos + 1
    new_element_list = []
    for i in range(ben_pos+1,suo_pos):
        if i == ben_pos+1:
            new_element_list.append(u'、' + element_list[i] + u'1、')
        else:
            new_element_list.append(element_list[i] + u'1、')
    for i in range(suo_pos+1, list_len):
        new_element_list.append(element_list[i] + u'2、')
    return ''.join(new_element_list)
'''
def normal_data_analysis(data_value):
    data_list = data_value.split(u'、')
    data_list.insert(len(data_list), u'、')
    data_list.insert(0, u'、')
    return ''.join(data_list)
 '''
   
def major_analysis_database(data_value):
    if re.search(u'本科', data_value):
        return muti_catlog_analysis(data_value)
    elif re.search(u'（', data_value):
        return data_value
    else:
        return u'、'+ data_value + u'、'
        
                
workbook = xlwt.Workbook(encoding = 'utf-8')
source_data_fd = xlrd.open_workbook(r'C:\project\io_file\database\2019guokao.xls')
sheet_name_list = source_data_fd.sheet_names()
for i in sheet_name_list:
    worksheet = workbook.add_sheet(i)
    table = source_data_fd.sheet_by_name(i)
    nrows = table.nrows
    cols = table.ncols    
    row_col = find_target_row_conlumn(u'专业', table)
    for j in range(row_col[0], nrows):
        get_string = major_analysis_database(table.cell(j, row_col[1]).value)            
        worksheet.write(j, row_col[1], label = get_string)
    
workbook.save(r'C:\project\io_file\database\major_info.xls')



