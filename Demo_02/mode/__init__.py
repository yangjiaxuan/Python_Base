#!/usr/bin/python
#encoding=utf-8

__author__ = "yangjiaxuan"

"""
	文档注释：
		   这是声明 这是一个包 因为实在 mode 文件夹下，
		所以是声明 mode 是一个包。
"""

def test():
	print("执行了 test 函数！")

if __name__ == '__main__':
    print ('mode 作为主程序运行')
    test()
else:
	print ("mode 初始化")
