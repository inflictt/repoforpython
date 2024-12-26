Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: D:/python/datatype_lists.py
[10, 20.4, -50, 'SAKSHAM BRO']
>>> 
===================== RESTART: D:/python/datatype_lists.py =====================
[10, 20.4, -50, 'SAKSHAM BRO']
>>> data = [10,20.4,-50,'SAKSHAM BRO']
... print(data)
... 
SyntaxError: multiple statements found while compiling a single statement
>>> data = [10,20.3,-59,"saksham bhai "]
>>> print(data)
[10, 20.3, -59, 'saksham bhai ']
>>> print(data[0])
10
>>> print(data[-1])
saksham bhai 
