#!/usr/bin/python
#encoding=utf-8


def modeTest_01(arg_01):
	print ("模块测试: modeTest_01 函数",arg_01)


def add(arg_01=0, *args):
	sum = arg_01
	for arg in args:
		sum += arg
	return sum
	


