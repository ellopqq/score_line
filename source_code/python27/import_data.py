#!/usr/bin/python
#coding=utf-8

import xlrd
#import xlwt

print(u"人这一生")
print(u"           选择往往比努力更重要\n")

#data = xlrd.open_workbook(r'C:\Users\ellopqq\eclipse-workspace\score_line\database\2019guokao.xls')
data = xlrd.open_workbook(r'C:\score_learn\python27\database\2019guokao.xls')

table = data.sheet_by_index(0)   #read first sheet
nrows = table.nrows
ncols = table.ncols
flag = 0
for i in range(nrows):
    oneRow = table.row_values(i)    #read a row, begin from 0
    for j in range(ncols):
        if oneRow[j] == u"工作地点":
            print(u"专业一栏出现第在%d行%d列" % (i,j))
            flag = 1
            break
    if flag == 1:
        break
    
row_search = i
col_search = j 
target_col = table.col_values(col_search)    

for i in range(ncols):
    if target_col[i] == u"英语" or target_col[i] == u"哲学类":
        print("目标在%d行" % i) 
    
print(u"一共有%d行" % nrows)
print(u"一共有%d列" % ncols)

print(table.cell(3,2).value)
