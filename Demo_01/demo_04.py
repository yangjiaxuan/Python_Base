#!/usr/bin/python
#encoding=utf-8

print "========== 开始测试 ==========="

# Number 
'''
    Python Number 数据类型用于存储数值。
	数据类型是不允许改变的,这就意味着如果改变 Number 数据类型的值，将重新分配内存空间。
'''

var1 = 1
var2 = 10

# 可以使用del语句删除一些 Number 对象引用。
'''
del var1, var2
print var1   会报错 说 val1 没有定义
'''


# 类型转化
'''
	int(x [,base ])         将x转换为一个整数  
	long(x [,base ])        将x转换为一个长整数  
	float(x )               将x转换到一个浮点数  
	complex(real [,imag ])  创建一个复数  
	str(x )                 将对象 x 转换为字符串  
	repr(x )                将对象 x 转换为表达式字符串  
	eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象  
	tuple(s )               将序列 s 转换为一个元组  
	list(s )                将序列 s 转换为一个列表  
	chr(x )                 将一个整数转换为一个字符  
	unichr(x )              将一个整数转换为Unicode字符  
	ord(x )                 将一个字符转换为它的整数值  
	hex(x )                 将一个整数转换为一个十六进制字符串  
	oct(x )                 将一个整数转换为一个八进制字符串  
'''



# 数学函数
'''
	abs(x)	    返回数字的绝对值，如abs(-10) 返回 10
	ceil(x)	    返回数字的上入整数，如math.ceil(4.1) 返回 5
	cmp(x, y)	如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
	exp(x)	    返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
	fabs(x)  	返回数字的绝对值，如math.fabs(-10) 返回10.0
	floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
	log(x)	    如math.log(math.e)返回1.0,math.log(100,10)返回2.0
	log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
	max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
	min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
	modf(x)	        返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
	pow(x, y)	    x**y 运算后的值。
	round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
	sqrt(x)	        返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j
'''


# 随机函数
'''
	choice(seq)	    从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
	randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
	random()	    随机生成下一个实数，它在[0,1)范围内。
	seed([x])	    改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
	shuffle(lst)	将序列的所有元素随机排序
	uniform(x, y)	随机生成一个实数，它在[x,y]范围内。
'''

# 需要导入工具
import random

choice_n = random.choice([1,2,4,5,6,7,8])  # 从数组中随机挑选一个元素
choice_s = random.choice("Python")       # 从字符串中随机挑选一个字母
choice_r = random.choice(range(10))    # 从范围 0~10 随机挑选一个数

randrange_s = random.randrange(10, 200, 2)  # 随机生成一个 x, 满足 10 < 10 + 2*x < 200 

random_s = random.random  # 随机生成的一个实数，它在[0,1)范围内。


shuffle_s = [1, 2 , 3, 4, 5, 6]
random.shuffle(shuffle_s)     # 随机打乱数组顺序

uniform_s = random.uniform(7, 14) # 在 7~14 之间随机生成一个数字


# 三角函数
'''
	acos(x)	    返回x的反余弦弧度值。
	asin(x)	    返回x的反正弦弧度值。
	atan(x)	    返回x的反正切弧度值。
	atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
	cos(x)	    返回x的弧度的余弦值。
	hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
	sin(x)	    返回的x弧度的正弦值。
	tan(x)	    返回x弧度的正切值。
	degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
	radians(x)	将角度转换为弧度
'''
import math

sin_s = math.sin(1)
print "sin_s:",sin_s



# 常量
'''
    pi  : 圆周率 3.1415926...
    e   : 数学常量 e , 及自然常数 2.7...

'''





