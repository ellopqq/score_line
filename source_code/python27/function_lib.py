#!/usr/bin/python
#coding=utf-8

def insert_space(num):
    init_space = '\0'
    i = 1
    while i<num:
        init_space = init_space + '\0'
        i = i + 1
    return init_space
