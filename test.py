#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ========================================== #
# 字符串和编码练习题
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
# before = 72
# after = 85

# persent = (after - before) / before * 100
# print('%2.1f%%' % persent)

# ========================================== #
# list和tuple
# 请用索引取出下面list的指定元素：
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# # 打印Apple:
# print(L[0][0])
# # 打印Python:
# print(L[1][1])
# # 打印Lisa:
# print(L[2][2])

# ========================================== #
# 条件判断
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

# height = 1.75
# weight = 80.5
# BMI = weight / (height * height)

# if BMI < 18.5:
#     print('过轻')
# elif BMI < 25:
#     print('正常')
# elif BMI < 28:
#     print('过重')
# elif BMI < 32:
#     print('肥胖')
# else:
#     print('严重肥胖')

# ========================================== #
# 循环
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print('Hello, %s' % name)

# ========================================== #
# 调用函数
# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
# n1 = 255
# n2 = 1000
# hn1 = hex(n1)
# hn2 = hex(n2)
# print(hn1, type(hn1))
# print(hn2, type(hn2))

# ========================================== #
# 定义函数
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0 的两个解。
# import math


# def quadratic(a, b, c):
#     if (b * b - 4 * a * c) > 0:
#         n = math.sqrt(b * b - 4 * a * c)
#         x1 = (-b + n) / (2 * a)
#         x2 = (-b - n) / (2 * a)
#         print('方程的根为%s,%s' % (x1, x2))
#     elif (b * b - 4 * a * c) == 0:
#         x = -b / (2 * a)
#         print('方程根为%s' % x)
#     else:
#         print('此方程无实根')

# quadratic(2, 3, 1)

# ========================================== #
# 列表生成式
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
# L1 = ['Hello', 'World', 18, 'Apple', None]

# L2 = [s.lower() for s in L1 if isinstance(s, str)]

# print L2

# ========================================== #
# 生成器
# 把杨辉三角每一行看做一个list，试写一个generator，不断输出下一行的list：

# def triangles():
#     N = [1]
#     while True:
#         yield N
#         N.append(0)
#         print('--N', N)
#         for i, n in enumerate(N):
#             temp = N[i - 1] + N[i]
#             print('--i , N[i], N[i-1]', i, N[i], N[i - 1])
#         N = [N[i - 1] + N[i] for i in range(len(N))]

# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break

# ========================================== #
# map/reduce
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。

# def normalize(name):
#     return name[0].upper() + name[1:].lower()

# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积

# from functools import reduce


# def prod(L):
#     def multiply(x, y):
#         return x * y
#     return reduce(multiply, L)

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456

# from functools import reduce


# def str2float(s):
#     s1 = s.split('.')[0]
#     s2 = s.split('.')[1]

#     def char2num(s):
# return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
# '8': 8, '9': 9}[s]

# return reduce(lambda x, y: x * 10 + y, map(char2num, s1 + s2)) /
# 10.0**len(s2)

# print('str2float(\'123.456\') = %.3f' % str2float('123.456'))

# ========================================== #
# filter
# 素数
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n


# def _not_divisible(n):
#     return lambda x: x % n > 0


# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)

# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909，请利用filter()滤掉非回数：
# def is_palindrome(n):
#     return str(n)[::-1] == str(n)

# output = filter(is_palindrome, range(1, 1000))
# print(list(output))

# ========================================== #
# sorted
# 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
# def by_name(t):
#     return t[0]


# def by_score(t):
#     return t[1]

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# L1 = sorted(L, key=by_name)
# print(L1)

# L2 = sorted(L, key=by_score)
# print(L2)
