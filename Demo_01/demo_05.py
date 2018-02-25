#!/usr/bin/python
#encoding=utf-8


print "============= 开始测试 ============"

# String
var_1 = "hello world!"

var_1_1 = var_1[0]      # h
var_1_a = var_1[0:5]    # hello

var_1_1 += " === new === "  # h === new ===

var_1 =  "Hello" + var_1[5:len(var_1)] #  Hello world!  注："Hello"+(5, 10]









# 转义字符

"""

	\(在行尾时)	   续行符
	\\			   反斜杠符号
	\'			   单引号
	\"		       双引号
	\a			   响铃
	\b	     	   退格(Backspace)
	\e			   转义
	\000  		   空
	\n	  		   换行
	\v			   纵向制表符
	\t		       横向制表符
	\r			   回车
	\f			   换页
	\oyy		   八进制数，yy代表的字符，例如：\o12代表换行
	\ xyy		   十六进制数，yy代表的字符，例如：\x0a代表换行  注： 实际是没有空格的 只是为了在这里显示
	\other		   其它的字符以普通格式输出
"""

print "\"这是测试语句\"\a \\ \n 此处换行！"



# 字符串运算符
'''
	下面说明中实例变量 a 值为字符串 "Hello"，b 变量值为 "Python"：

	+	字符串连接	      a + b  ==> 'HelloPython'
	*	重复输出字符串	  a * 2  ==> 'HelloHello'
	[]	通过索引获取字符串中字符     a[1] ==> 'e'
	[ : ]	截取字符串中的一部分	[1:4] ==> 'ell'
	in	成员运算符 如果字符串中包含给定的字符返回 True        "H" in a ==> True 
	not in	成员运算符 - 如果字符串中不包含给定的字符返回 True   "M" not in a ==> True
	r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。
	    原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	
	    print r'\n' ==> \n  print R'\n' ==> \n
	%	格式字符串
'''

if 'a' in 'abc':
	print 'a 在 abc 中'
if 'd' not in 'abc':
	print 'd 不在 abc中'

print r'猜猜 \n 怎么打印！'     # \n 不再是转义字符  不在代表换行符
print R'上面\n竟然没换行！'





# 字符串格式化
'''
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
'''



# 格式化操作符辅助指令:   不懂什么意思
'''
	*	  定义宽度或者小数点精度
	-	  用做左对齐
	+	  在正数前面显示加号( + )
	<sp>  在正数前面显示空格
	#	  在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
	0	  显示的数字前面填充'0'而不是默认的空格
	%	  '%%'输出一个单一的'%'
	(var) 映射变量(字典参数)
	m.n.  m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
'''



# 三引号（triple quotes）
'''
	python中三引号可以将复杂的字符串进行复制:
	python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
	三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）。
'''


# Unicode 字符串
'''
	Python 中定义一个 Unicode 字符串和定义一个普通字符串一样简单：
	u'Hello World !'  ==> u'Hello World !'

	引号前小写的"u"表示这里创建的是一个 Unicode 字符串。如果你想加入一个特殊字符，可以使用 Python 的 Unicode-Escape 编码。如下例所示：
	u'Hello\u0020World !' ==> u'Hello World !'
	被替换的 \u0020 标识表示在给定位置插入编码值为 0x0020 的 Unicode 字符（空格符）。
'''


# 字符串内建函数
'''
	字符串方法是从python1.6到2.0慢慢加进来的——它们也被加到了Jython中。

	这些方法实现了string模块的大部分方法，如下表所示列出了目前字符串内建支持的方法，
	所有的方法都包含了对Unicode的支持，有一些甚至是专门用于Unicode的。
'''

string = "hello world!"
string = string.capitalize()  # 首字母大写 ： ==> Hello world!

#string = string.center(15)  # 返回一个原字符串居中,并使用空格填充至长度 15 的新字符串
                            # ==>|  Hello world!  |

count = string.count('l', 0, len(string)) # 返回 字符串‘l’ 在string中 范围（0~len）中出现的次数     ==> 3

#string = string.decode('UTF-8','strict')   # 以utf-8编码风格进行解码 string
string = string.encode('UTF-8',"strict")   # utf-8 编码  ==>  Hello world!  
#string = string.encode('base64', 'strict') # base64 编码 ==> ICBIZWxsbyB3b3JsZCEg

'''
	suffix -- 该参数可以是一个字符串或者是一个元素。
	start  -- 字符串中的开始位置。
	end    -- 字符中结束位置。
'''
suffix = "world!"
start  = 6
end    = 12

isTrue = string.endswith(suffix)  # 是否含有 suffix 后缀
isTrue = string.endswith(suffix, start)  # 是含有 suffix 后缀 并且开始位置为 6
isTrue = string.endswith(suffix, start, end) # 是含有 suffix 后缀 并且开始位置为 6 结束位置为 12


isTrue = string.find('hell', 0, len(string)) # 在 string 的[0~len)范围内是否包含 ‘hell’

string_a = "{} {}".format("hello", "world")       # 不指定位置， 直接按照先后顺序 ==> "hello world"
string_a = "{0} {1} {0}".format("hello", "world") # 指定位置    0 代表 'hello'  1 代表 "world" ==> "hello world hello"

index = string.index("o", 0, len(string)) # 在0~len范围内查找 "o" 的下标， 如果没有回报异常 

isTrue = string.isalnum() # 如果 string 至少有一个字符,且所有字符都是字母或数字则返回 True,否则返回 False

isTrue = string.isalpha() # 如果 string 至少有一个字符,且所有字符都是字母则返回 True,否则返回 False

'''
	string.isdecimal() :
	如果 string 只包含十进制数字则返回 True 否则返回 False.
	这种方法只存在于unicode对象。
	定义一个十进制字符串，只需要在字符串前添加 'u' 前缀即可。
'''
#isTrue = string.isdecimal()


"""
	string.isdigit(): 

	*** 检测字符串中是否 只 包含数字 ***

	如果 string 只包含数字则返回 True 否则返回 False.
"""
isTrue = string.isdigit()

"""
	string.islower():

	*** 检测字符串中是否包含字母，并且这些字母都是 小写字母 ***

	如果 string 中包含至少一个区分大小写的字符，
	并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
"""
isTrue = string.islower() # 

"""
	string.isupper() :

	*** 检测字符串中是否包含字母，并且这些字母都是 大写字母 ***

	如果 string 中包含至少一个区分大小写的字符，
	并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
"""
isTrue = string.isupper() # 

"""
	string.isnumeric()
	如果 string 中只包含数字字符，则返回 True，否则返回 False
	这种方法是只针对unicode对象。
"""
# isTrue = string.isnumeric()

"""
	string.isspace():

	*** 检测字符串中是否 只包含空格 ***

	如果 string 中只包含空格，则返回 True，否则返回 False.
"""
isTrue = string.isspace() # 

"""
	string.istitle():
	*** 检测字符串中是不是单词都是以大写开始 其他字母都是小写 ***

	如果 string 是标题化的(见 title())则返回 True，否则返回 False
"""
isTrue = string.istitle()


"""
	string.join(str1, str2 ...);
	*** 字符串拼接 ***

	str1, str2... 中间以 string 作为连接符 进行拼接
"""
str_1 = "-"
new_str_1 = str_1.join(("a", "b", "c"))  # a-b-c

"""
	string.ljust(width):

	返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
"""
string = string.ljust(12) 

"""
	string.lower():

	转换 string 中所有大写字符为小写.
"""
string = string.lower()   

"""
	string.lstrip():

	截掉 string 左边的空格
"""
string = string.lstrip()  

"""
	maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，
	第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
	注：两个字符串的长度必须相同，为一一对应的关系。
"""
intab  = 'aeiou'
outtab = '12345'
# 不知道为什么用不了
#trantab = string.maketrans(intab, outtab) # 把字符串中的 a e i o u 分别用 1 2 3 4 5 代替
#string  = string.translate(trantab) #用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

maxW = max(string)   # 返回字符串 string 中最大的字母。
minW = min(string)   # 返回字符串 string 中最小的字母。

'''
   分割：
   有点像 find()和 split()的结合体,
   从 str 出现的第一个位置起,把字符串 
   string 分成一个3元素的元组 
   (string_pre_str,str,string_post_str),
   如果 string 中不包含str 则 string_pre_str == string.

   下面 tuple_a 的内容是 ('http', '://', 'www.w3cschool.cc/')
'''
string = "http://www.w3cschool.cc/"
tuple_a = string.partition("://") 

string = "hahaha"
string = string.replace("h", "w",  3) # 把string 中 h 换成 w 替换次数不超过 3次
'''
	类似于  find()，不过是从右边开始.
	返回字符串第一次出现的位置(从右向左查询)，
	如果没有匹配项则返回-1。

	str = "this is really a string example....wow!!!";
	print str.rfind(substr);        # ==> 5
	print str.rfind(substr, 0, 10); # ==> 5
 
	print str.find(substr);         # ==> 2
	print str.find(substr, 0, 10);  # ==> 2
'''
index = string.rfind("o", 0, len(string) ) # 类似于 find()函数，不过是从右边开始查找.

'''
	类似于 index()，不过是从右边开始.
	如果没有匹配项则返回-1, 报异常。
'''
index  = string.rindex( "w", 0, len(string)) #

string = string.rjust(15) # 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串

tuple_a = string.rpartition("o") #类似于 partition()函数,不过是从右边开始查找.

string = string.rstrip() # 删除 string 字符串末尾的空格.

"""
    string.split(str, num) :
	以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串
"""
tuple_a = string.split("o", string.count("o")) 

"""
	string.splitlines(keepends):
	按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，
	如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

	str1 = 'ab c\n\nde fg\rkl\r\n'
	print str1.splitlines();          # ==>['ab c', '', 'de fg', 'kl']

	str2 = 'ab c\n\nde fg\rkl\r\n'
	print str2.splitlines(True)       # ==> ['ab c\n', '\n', 'de fg\r', 'kl\r\n']  

"""
tuple_a = string.splitlines(True) 

isTrue = string.startswith("obj", 0,len(string)) # 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.

"""
    string.strip(chars)
	chars -- 移除字符串头尾指定的字符

	str = "0000000this is string example....wow!!!0000000";
	print str.strip( '0' );   # ==> this is string example....wow!!!
"""
string = string.strip("") # 在 string 上执行 lstrip()和 rstrip() 即删除前后空格

string = string.swapcase() # 翻转 string 中的大小写

string = string.title() #返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())

string = string.translate("a"*256, "a") #根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 第二个 参数中

string = string.upper() #转换 string 中的小写字母为大写

string = string.zfill(15) #返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0

"""
	isdecimal():
	方法检查字符串是否只包含十进制字符。
	这种方法只存在于unicode对象。
"""
#isTrue = string.isdecimal() 















