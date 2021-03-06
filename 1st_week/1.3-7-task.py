"""
В процессе выполнения кода на стек добавляются и со стека снимаются функции.
Добавление функции на стек увеличивает его размер на 1, снятие функции со стека уменьшает его размер на 1.

Чему равен максимальный размер стека в процессе выполнения следующего кода?
Обратите внимание, что при интерпретации кода на стеке находится функция module,
которую также нужно учесть при подсчете размера стека.
В рамках данного задания можно считать, что функция print ﻿не вызывает дополнительных функций внутри себя.

def h():
  print(12)

def f():
  g(h)

def g(a):
  a()

g(f)
"""

global stack_num

stack_num = 1


def h():
    global stack_num
    stack_num += 1
    print(12)


def f():
    global stack_num
    stack_num += 1
    g(h)


def g(a):
    global stack_num
    stack_num += 1
    a()


stack_num += 1
g(f)

print('stack_num:', stack_num)  # stack_num: 6
