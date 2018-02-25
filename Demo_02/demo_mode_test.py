#!/usr/bin/python
#encoding=utf-8

print ("============= 开始测试 ===========")

# 需要放在同一个文件夹下， 导入之后运行会生成一个 .pyc 文件 

import demo_mode  #导入所有函数
	#注：
	#调用函数时 使用这种方式 <<<< 模块名.函数名(参数) >>>> 如下：
demo_mode.modeTest_01(10)



"""
	From…import 语句
	Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：
	from modname import name1[, name2[, ... nameN]]

	例如，要导入模块 fib 的 fibonacci 函数，使用如下语句：
	from fib import fibonacci

	注：
	调用时 直接使用函数调用即可  <<<< 函数名(参数) >>>>
"""


from demo_mode import modeTest_01
modeTest_01(10)

from demo_mode import add
sum = add(1,3,4)
print("测试二：sum:%d"%sum)


def test_01():

	# 此处sum是在函数中，是局部变量，要想让sum访问 外部变量 sum 就需要用 global 来修饰 sum
	global sum  # 这种写法就可以访问外部的 sum 
	if sum == 0:
		sum = 10
	





"""
	*********** dir() ***********
	dir()：函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
"""


import demo_mode

path = dir(demo_mode)
print (path)    # ['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'add', 'modeTest_01']
# 在这里，特殊字符串变量__name__指向模块的名字，__file__指向该模块的导入文件名。





"""
	globals() 和 locals() 函数
	根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。
	如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。
	如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。
	两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。

	reload() 函数
	当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
	因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块。语法如下：
	reload(module_name)
	在这里，module_name要直接放模块的名字，而不是一个字符串形式。比如想重载 hello 模块，如下：
	reload(hello)

"""



"""
	Python中的包
	    包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。
	    简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。__int__.py
    用于标识当前文件夹是一个包。
	    考虑一个在 package_runoob 目录下的 runoob1.py、runoob2.py、__init__.py 文件，test.py 
    为测试调用包的代码，目录结构如下：
	test.py
	package_runoob
		|-- __init__.py
		|-- runoob1.py
		|-- runoob2.py 

	源代码如下：

	<<< package_runoob/runoob1.py >>>
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		def runoob1():
		   print "I'm in runoob1"


	<<< package_runoob/runoob2.py >>>
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		def runoob2():
		   print "I'm in runoob2"



	现在，在 package_runoob 目录下创建 __init__.py：

	<<< package_runoob/__init__.py >>>
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		if __name__ == '__main__':
		    print '作为主程序运行'
		else:
		    print 'package_runoob 初始化'


	然后我们在 package_runoob 同级目录下创建 test.py 来调用 package_runoob 包

	<< test.py >>>
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		# 导入 Phone 包
		from package_runoob.runoob1 import runoob1
		from package_runoob.runoob2 import runoob2
		 
		runoob1()
		runoob2()

	以上实例输出结果：
	package_runoob 初始化
	I'm in runoob1
	I'm in runoob2
	如上，为了举例，我们只在每个文件里放置了一个函数，但其实你可以放置许多函数。你也可以在这些文件
	里定义Python的类，然后为这些类建一个包。
"""

"""
 为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，
	这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。
	在Python中，一个.py文件就称之为一个模块（Module）。

	    如果不同的人编写的模块名相同怎么办？为了避免模块名冲突，Python又
	引入了按目录来组织模块的方法，称为包（Package）。

		举个例子，一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的
	文件就是一个名字叫xyz的模块。
	    假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过
	包来组织模块，避免冲突。方法是选择一个顶层包名。现在，abc.py模块的名字
	就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。
"""
from mode import mode_01
from mode import mode_02

# ------ 我是 mode_01 runFunc ------
mode_01.runFunc_01()
# ------ 我是 mode_02 runFunc ------
mode_02.runFunc_02()






print(" =================== 安装第三方模块 start =================")
"""
	   在Python中，安装第三方模块，是通过包管理工具pip完成的。
	   如果你正在使用Mac或Linux，安装pip本身这个步骤就可以跳过了。
	   一般来说，第三方库都会在Python官方的pypi.python.org网站注册，
	要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，
	比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：
	   pip install Pillow

	   Pillow 处理图片的工具	

	注意：Mac或Linux上有可能并存Python 3.x和Python 2.x，
	     因此对应的pip命令是pip3。
	     pip3 install Pillow
"""
from PIL import Image

img = Image.open("/Users/yangxu/Desktop/image/1.2.png")
print(img.format, img.size, img.mode) # PNG (108, 108) RGB

img.thumbnail((20,20))
img.save("thumbnail.jpg","JPEG")


"""
		其他常用的第三方库还有MySQL的驱动：mysql-connector-python，
	用于科学计算的NumPy库：numpy，用于生成文本的模板工具Jinja2，等等。

		当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py
	文件，如果找不到就会报错。

		默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和
	第三方模块，搜索路径存放在sys模块的path变量中：
"""
import sys

sys_path = sys.path
print("----------|-------- sys_path:",sys_path)
"""
	sys_path: 
	[
		'/Users/yangxu/Desktop/Python/2017-04-25', 
		'/usr/local/Cellar/python3/3.6.1/Frameworks
			/Python.framework/Versions/3.6/lib/python36.zip', 
		'/usr/local/Cellar/python3/3.6.1/Frameworks
			/Python.framework/Versions/3.6/lib/python3.6', 
		'/usr/local/Cellar/python3/3.6.1/Frameworks
			/Python.framework/Versions/3.6/lib/python3.6/
			lib-dynload', 
		'/usr/local/lib/python3.6/site-packages'
	] 
"""

"""
	如果我们要添加自己的搜索目录，有两种方法：
		1、直接修改sys.path，添加要搜索的目录：
			这种方法是在运行时修改，运行结束后失效。
			>>> import sys
			>>> sys.path.append('/Users/michael/my_py_scripts')
		2、设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块
	搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜
	索路径，Python自己本身的搜索路径不受影响。

"""



