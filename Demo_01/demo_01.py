#!/usr/bin/python
#encoding=utf-8


'''
	Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。
	Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色语法结构。
	Python 是一种解释型语言： 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。
	Python 是交互式语言： 这意味着，您可以在一个Python提示符，直接互动执行写你的程序。
	Python 是面向对象语言: 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。
	Python 是初学者的语言：Python 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到 WWW 浏览器再到游戏。
'''
print("=======简单测试=====")
'''
    关键字：
		and	       exec	      not
		assert	   finally	  or
		break	   for	      pass
		class	   from	      print
		continue   global	  raise
		def	       if	      return
		del	       import     try
		elif	   in	      while
		else	   is	      with
		except	   lambda	  yield
'''

isCat = False
'''
	int(a) 把a转成整型，前提是a为整形字符串
'''


'''
isCat = int(raw_input("请输入是不是一只猫："))

if not(isCat):
	print("不是一只猫")    #前面有四个空格 但是不要直接打四个空格 使用 tab 键
else:
	print("是一只猫")
'''










'''
	Numbers（数字）   int  float long complex(复数 eg:3.14j )
	String（字符串）
	List（列表）
	Tuple（元组）
	Dictionary（字典）
'''


# Numbers
num_01 = 10  # int
num_02 = 0.5 # float
num_03 = complex(1,5)  #复数


# String
string_01   = "this is a string!"
string_01_a = string_01[0]    # t     如果为汉字就不一定了
string_01_b = string_01[5:7]  # is
string_01_c = string_01[8:]   # a string!
string_01_d = string_01*2     #this is a string!this is a string!
string_01_e = string_01 + " wakaka!"   # this is a string! wakaka!







#List
listA = ['runoob', 786, 2,23, 'john', 70.2]  #['runoob', 786, 2,23, 'john', 70.2]
listB = listA[1:3]    # [786, 2]
listC = listA[2:]     # [786, 2,23, 'john', 70.2]
listD = listB * 2     # [786, 2, 786, 2]
listE = listB + ["新加"] # [786, 2,"新加"]

listA_01 = listA[0]   # runoob
'''
for x in listE:
	print x
'''








# 字典
dictA = {}
dictA['one']   = "oneVlaue"         # {'one': 'oneVlaue'}
dictA['2']     = "2Value"           # {'2': '2Value', 'one': 'oneVlaue'}
dictA['third'] = "thirdValue"       # {'2': '2Value', 'third': 'thirdValue', 'one': 'oneVlaue'}

dictKeys   = dictA.keys()             # ['2', 'third', 'one']
dictValues = dictA.values()           # ['2Value', 'thirdValue', 'oneVlaue']
'''
for key in dictKeys:
	value = dictA[key]
	print("key: %s    value: %s"%(key, value))
'''









#元组
tupleA = ('runoob', 123, 23.3, 'john', 'wakaka')  #('runoob', 123, 23.3, 'john', 'wakaka')

tupleA_01 = tupleA[0]          # runoob
tupleB    = tupleA[1:3]        # (123, 23.3)
tupleC    = tupleA[2:]         # (23.3, 'john', 'wakaka')
tupleD    = tupleB * 2         # (123, 23.3, 123, 23.3)
tupleE    = tupleB + ('new', 23) # (123, 23.3, 'new', 23)

'''
for x in tupleD:
	print x
'''

tupleNew = ('new', 'a')
tupleF = tupleB + tupleNew

#  ========  
#  注：
#  元祖声明时， 元素必须大于一个！ 如果只包含一个，就按一个元素处理 eg:('we') <==> we 而不是('we')
#  ========  






# 数据转型
'''
		int(x [,base])         将x转换为一个整数
		long(x [,base] )       将x转换为一个长整数
		float(x)               将x转换到一个浮点数
		complex(real [,imag])  创建一个复数
		str(x)                 将对象 x 转换为字符串
		repr(x)                将对象 x 转换为表达式字符串
		eval(str)              用来计算在字符串中的有效Python表达式,并返回一个对象
		tuple(s)               将序列 s 转换为一个元组
		list(s)                将序列 s 转换为一个列表
		set(s)                 转换为可变集合
		dict(d)                创建一个字典。d 必须是一个序列 (key,value)元组。
		frozenset(s)           转换为不可变集合
		chr(x)                 将一个整数转换为一个字符
		unichr(x)              将一个整数转换为Unicode字符
		ord(x)                 将一个字符转换为它的整数值
		hex(x)                 将一个整数转换为一个十六进制字符串
		oct(x)                 将一个整数转换为一个八进制字符串
'''
num_04    = int('12')
string_02 = str(12)

print "num_04:", num_04 
print "string_02:",string_02



