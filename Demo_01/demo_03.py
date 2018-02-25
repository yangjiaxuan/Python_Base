#!/usr/bin/python
#encoding=utf-8



'''
	条件语句：

	Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。
'''
print "========== 开始测试 ========="

'''
    if 判断条件1:
	    执行语句1……
	elif 判断条件2:
	    执行语句2……
	elif 判断条件3:
	    执行语句3……
	else:
	    执行语句4……
'''

'''
a = raw_input("请输入一个数字：")
a = int(a)
'''

'''
if a == 0:
	print "是一个 0"
elif a < 10:
	print "小于 10"
elif a < 100:
	print "大于等于 10 小于 100"
else:
	print "大于等于 100"
'''



'''
if a >= 0 and a < 10:
	print "大于等于0 小于 10"
else:
	print "大于等于 10"
'''


"""
if a == 10 or a == 20:
	print " 10 或者 20"
"""


'''
if not(a):
	print "是 0"
else:
	print "不是 0"
'''






# 循环语句

# 1 while 循环
'''
numbers = [12, 37, 5 ,42, 8, 3]
even = []
odd  = []
while len(numbers) > 0:
	number = numbers.pop()
	if number % 2 == 0:
		even.append(number)
	else :
		odd.append(number)

print "number:",number     # number: 12   并没有释放
print "numbers",numbers    # numbers:[]
print "even:",even         # even: [8, 42, 12]
print "odd:",odd           # odd: [3, 5, 37]
'''

# while ... else  else中的执行体在 不满足 while执行条件时执行
'''
num = 10
while num > 0:
	print num
	num -= 1 # 没有 "--"
else:
	print "循环结束"
'''





# for 循环
'''
string = "python"
for x in string:
	print "当前字母: ",x
'''

'''
List = ["banana", "apple", "mango"]
for x in List:
	print "水果名(List): ",x
'''

ListA = [1, 2, 3, 4, 5, 6]

# 使用序列索引迭代    for ... else（原则同 while ... else ） 在for 循环结束后执行 else 中的执行体
'''
for index in range(len(ListA)):
	print "数字： ", ListA[index]
else:
	print "for 循环结束"
'''







# 循环嵌套
'''
nums = [23, 34, 3, 45, 20, 50, 54, 9, 30]

print "排序之前：",nums

for index_i in xrange(0,len(nums)-2):
	for index_j in xrange(index_i+1,len(nums)-1):
		if nums[index_i] < nums[index_j]:
			num = nums[index_i]
			nums[index_i] = nums[index_j]
			nums[index_j] = num


print "排序之后：",nums
'''

# break continue
'''
for x in "python":
	if x is "h":
		break    #continue 同样用法
	print "打印字符：", x
'''


#pass 语句
'''
   Python pass是空语句，是为了保持程序结构的完整性。
		  pass 不做任何事情，一般用做占位语句。
'''
'''
for letter in 'Python':
	if letter == 'h':
		pass
		print "这是 pass 块"
	print "当前字母：", letter
'''
























