#!/usr/bin/python
#encoding=utf-8


print '================= 开始测试 ==================='

"""
函数
	********* 不带参 函数 **********
"""
def func_01():
	'这是函数的解释文档语句 在终端输入 help(函数名) 即可出现！'
	print '测试一：这是一个不带参数的函数'

#调用
func_01()





"""
	********* 带参数 函数 **********
"""
def func_02(string):
	print string

#调用
func_02('测试二：带参数函数')





"""
	********** 带返回值 ************
"""
def  add_01(param_01, param_02):
	sum = param_01 + param_02
	return sum

#调用
sum = add_01(10, 20)
print "测试三：10+20=:",sum

param_01 = 20
param_02 = 10
# 可以指定函数参数 不一定非要按照原来的顺序写 此处传参顺序 就与 函数参数顺序不同
sum = add_01(param_02 = param_02, param_01 = param_01)
print("测试四：%d+%d=%d"%(param_01,param_02,sum))


"""
	*********** 参数 缺醒值 *********
"""
# 这里可以之传入一个参数 param_01  因为 param_02 含有默认值
def add_02(param_01, param_02=10):
	sum = param_01 + param_02
	return sum

sum = add_02(param_01=10)
print "测试五：这里只传入了一个参数10，两一个参数是默认10 10+10=",sum

"""
	*********** 参数个数 不定 *********
"""
def add_03(*params):
	sum = 0
	for param in params:
		sum += param
	return sum

print ("测试六： 参数不定长：1+2+3+4+5=%d"%add_03(1,2,3,4,5))


"""
	匿名函数
	python 使用 lambda 来创建匿名函数。
	lambda只是一个表达式，函数体比def简单很多。
	lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
	lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
	虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
	
	语法
	lambda函数的语法只包含一个语句，如下：
	lambda [arg1 [,arg2,.....argn]]:expression
"""

# 函数声明
sumFucn = lambda param_01, param_02: param_01 + param_02

print "测试七：匿名函数 10+20=",sumFucn(10,20)








"""
	变量作用域
	    一个程序的所有的变量并不是在哪个位置都可以访问的。访问权限决定于这个变量是在哪里赋值的。
	变量的作用域决定了在哪一部分程序你可以访问哪个特定的变量名称。两种最基本的变量作用域如下：
		全局变量 局部变量

	全局变量和局部变量
	    定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
	    局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，
    所有在函数内声明的变量名称都将被加入到作用域中。如下实例：
"""
total = 0; # 这是一个全局变量

def sum( arg1, arg2 ):
   #返回2个参数的和."
   total = arg1 + arg2; # total在这里是局部变量.
   print "函数内是局部变量 : ", total
   return total;
 
#调用sum函数
sum( 10, 20 );
print "函数外是全局变量 : ", total # 此处函数内部无法访问








