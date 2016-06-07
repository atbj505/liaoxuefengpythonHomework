#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)

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

# ========================================== #
# 使用@property
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
# class Screen(object):

#     def __init__(self):
#         super(Screen, self).__init__()

#     @property
#     def width(self):
#         return self._width

#     @width.setter
#     def width(self, width):
#         self._width = width

#     @property
#     def height(self):
#         return self._height

#     @height.setter
#     def height(self, height):
#         self._height = height

#     @property
#     def resolution(self):
#         return self._width * self._height


# s = Screen()
# s.width = 1024
# s.height = 768
# print(s.resolution)
# assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

# ========================================== #
# 枚举类
# from enum import Enum, unique


# @unique
# class WeekDay(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6

# print(WeekDay.Sun)
# print(WeekDay.Sun.value)

# for name, value in WeekDay.__members__.items():
#     print(name, value)

# ========================================== #
# 调试
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

# ========================================== #
# 文档测试
# 对函数fact(n)编写doctest并执行：
# def fact(n):
#     '''
#      >>> fact(1)
#      1
#      >>> fact(3)
#      6
#      >>> fact(0)
#      Traceback (most recent call last):
#       ...
#      ValueError
#      >>> fact('x')
#      Traceback (most recent call last):
#        ...
#      TypeError
#     '''
#     if n < 1:
#         raise ValueError()
#     if n == 1:
#         return 1
#     return n * fact(n - 1)

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

# ========================================== #
# IO
# with open('/Users/yangqihui/Desktop/test.txt', 'w') as f:
# print(f.read())
# for line in f.readlines():
# print(line.strip())
# print(f.read(12))
# f.write('hello tommorow')
# with open('/Users/yangqihui/Desktop/test.txt', 'r') as f:
# print(f.read())

# ========================================== #
# StringIO
# from io import StringIO

# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world')

# print(f.getvalue())

# f1 = StringIO('Hello\nHi\ngoodbye\n')
# for line in f1.readlines():
#     print(line.strip())

# ========================================== #
# BytesIO
# from io import BytesIO
# f = BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())
# f1 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f1.read())

# ========================================== #
# 操作文件和目录
# import os


# def dir_l(command):
#     if command == "dir -l":
#         curDir = os.path.abspath('.')
#         dirs = os.listdir(curDir)
#         for x in dirs:
#             print(x)
# dir_l('dir -l')

# def find_file(dir, name):
#     path = os.path.abspath(dir)
#     dirs = os.listdir(path)
#     for x in dirs:
#         searchPath = os.path.join(path, x)
#         logging.info(searchPath)
#         if os.path.isdir(searchPath):
#             find_file(searchPath, name)
#         elif os.path.isfile(searchPath):
#             if name in x:
#                 print(searchPath)
# find_file('.', 'test')

# ========================================== #
# 序列化
# import pickle
# d = dict(name='Bob', age=23, score=100)
# f = open('/Users/yangqihui/Desktop/test.txt', 'wb')
# pickle.dump(d, f)
# f.close()

# f1 = open('/Users/yangqihui/Desktop/test.txt', 'rb')
# d = pickle.load(f1)
# f1.close()
# print(d)

# import json
# d = dict(name='Bob', age=23, score=100)
# jsonStr = json.dumps(d)
# print(jsonStr)
# f = open('/Users/yangqihui/Desktop/test.txt', 'w')
# json.dump(d, f)
# f.close()

# d1 = json.loads(jsonStr)
# print(d1)
# f1 = open('/Users/yangqihui/Desktop/test.txt', 'r')
# d2 = json.load(f1)
# print(d2)


# class Student(object):
#     """docstring for Student"""

#     def __init__(self, name, age, score):
#         super(Student, self).__init__()
#         self.name = name
#         self.age = age
#         self.score = score

#     def __str__(self):
#         return 'Student: %s, %s, %s' % (self.name, self.age, self.score)
#     __repr__ = __str__

# s = Student('Bob', 23, 100)
# stuJsonStr = json.dumps(s, default=lambda obj: obj.__dict__)
# print(stuJsonStr)


# def dictToStudent(dict):
#     return Student(dict['name'], dict['age'], dict['score'])
# print(json.loads(stuJsonStr, object_hook=dictToStudent))

# ========================================== #
# 多进程

# import os
# print("Process %s start" % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print("I'm child process %s and my parent process is %s" %
#           (os.getpid(), os.getppid()))
# else:
#     print("I %s just creat a child process %s" % (os.getpid(), pid))


# from multiprocessing import Process
# import os


# def run_proc(p_name):
#     print("Run child process %s %s" % (p_name, os.getpid()))

# if __name__ == "__main__":
#     print("Parent process is %s" % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print("Process will start")
# # 子进程开始
#     p.start()
# # 阻塞当前线程，用于进程间的同步
#     p.join()
#     print("Child process end")


# from multiprocessing import Pool
# import os
# import time
# import random


# def long_time_task(p_name):
#     print("Running task %s %s" % (p_name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print("Tasks %s runs for %.2f seconds" % (p_name, (end - start)))

# if __name__ == "__main__":
#     print("Parent process %s" % os.getpid())
#     p = Pool(4)
#     for i in range(4):
#         p.apply_async(long_time_task, args=(i,))
#     print("Wait for all subprocesses done")
#     p.close()
#     p.join()
#     print("All subprocesses done")


# import subprocess
# print("$ nslookup www.python.org")
# r = subprocess.call(["nslookup", "www.python.org"])
# print("Exit code:", r)


# from multiprocessing import Queue, Process
# import os
# import time
# import random


# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue' % value)
#         q.put(value)
#         time.sleep(random.random())


# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue' % value)

# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))

#     pw.start()
#     pr.start()

#     pw.join()
#     pr.terminate()

# ========================================== #
# 多线程

# import time
# import threading


# def loop():
#     print("thread %s is running..." % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n += 1
#         print("thread %s >>> %s" % (threading.current_thread().name, n))
#         time.sleep(1)
#     print("thread %s is end" % threading.current_thread().name)

# print("thread %s is running..." % threading.current_thread().name)
# t = threading.Thread(target=loop, name="LoopThread")
# t.start()
# t.join()
# print("thread %s is end" % threading.current_thread().name)

import time
import threading

balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance += n
    balance -= n


def run_thread(n):
    for i in range(10):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
