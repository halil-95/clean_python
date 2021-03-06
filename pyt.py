# ************************************************************правила*****************************************************************

# _____отступы очень важны

# if 15>10:
# 	print('yep')
# else:
	# print('no')
# error	
# if 15>10:
# print('yep')

# пробелы зависять от меня

# №1
# if 15>10:
# 	print('yep')

# №2
#1 if 15>10:
#         print('yep')
# но лучше №1


# Вы должны использовать одинаковое количество пробелов в одном и том же блоке кода, иначе Python выдаст вам ошибку:

# if 5 > 2:
#  print("Five is greater than two!")
#         print("Five is greater than two!")
# ////////////
#   File "C:\Users\halil\Desktop\pyt.py", line 28
#     print("Five is greater than two!")
# IndentationError: unexpected indent
# [Finished in 195ms]
# ///////////////
# #####################################################правила#######################################################################










# *******************************************************<variable>*****************************************************************

# variable создаются, когда вы присваиваете им значение:
# variable не нужно объявлять с каким-либо конкретным типом , и они могут даже изменить тип после того, как они были установлены.

# x = 4       # x is of type int
# x = "Sally" # x is now of type str
# print(x)


"""
Имя переменной должно начинаться с буквы или символа подчеркивания.
Имя переменной не может начинаться с цифры
Имя переменной может содержать только буквенно-цифровые символы и символы подчеркивания (Az, 0–9 и _).
Имена переменных чувствительны к регистру (age, Age и AGE — это три разные переменные).				
"""

# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"

# ----------------------

# ______виды записы

# Camel Case
# myVariableName = "John"

# Pascal Case
# MyVariableName = "John"

# Snake Case
# my_variable_name = "John"

# ------------------

# ______Если вы хотите указать тип данных переменной, это можно сделать с помощью приведения типов.

# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

# ------------------

# ______Множество значений для нескольких переменных

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# Примечание. Убедитесь, что количество переменных соответствует количеству значений, иначе вы получите ошибку.

# ------------------

# Строковые переменные могут быть объявлены с использованием одинарных или двойных кавычек:

# x = "John"
# # is the same as
# x = 'John'

# --------------------

'''
Распаковать коллекцию --- Если у вас есть набор значений в виде списка, кортежа и т. д. 
Python позволяет извлекать значения в переменные. Это называется распаковкой
'''
# fruits = ["apple", "banana", "cherry", "hello"]
# x, y, z, w = fruits
# print(x)
# print(y)
# print(z)
# print(w)

# ---------------------

# ####################################################</variable>##################################################################










# ************************************************************comment*********************************************************

# Комментарии начинаются с #, а оставшуюся часть строки Python отобразит как комментарий:

#_______№1
# #This is a comment.
# print("Hello, World!")

#______№2
# print("Hello, World!") #This is a comment

# ------------------

# ___ Многострочные комментарии

"""
 Поскольку Python будет игнорировать строковые литералы, 
которые не назначены переменной, вы можете добавить в свой код многострочную строку (тройные кавычки) и поместить в нее свой комментарий:
"""
'''
или однострочную кавычку
'''


# ##########################################################comment##################################################################







# **************************************************************FUNCTION***************************************************************
# _____________________________________________________предороеделенный функция________________________________________________


# ____вывода переменных
# часто используется для вывода переменных.
# x = "Python is awesome"
# print(x) 

# В print() функции вы выводите несколько переменных, разделенных запятой:
# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)

# Вы также можете использовать +оператор для вывода нескольких переменны
# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# Для чисел +символ работает как математический оператор:
# x = 5
# y = 10
# print(x + y)

# В print()функции, когда вы пытаетесь объединить строку и число + оператором, Python выдаст вам ошибку:
# x = 5
# y = "John"
# print(x + y)

# Лучший способ вывести несколько переменных в print()функцию — разделить их запятыми, которые даже поддерживают разные типы данных:
# x = 5
# y = "John"
# print(x, y)
# ---------------------------------

# ######################################################FUNCTION######################################################################
