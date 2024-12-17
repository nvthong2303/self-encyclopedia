#!/usr/bin/env python
import psutil
# gives a single float value
# psutil.cpu_percent()
# # gives an object with many fields
# psutil.virtual_memory()
# # you can convert that object to a dictionary
# dict(psutil.virtual_memory()._asdict())
# you can have the percentage of used RAM
x = psutil.virtual_memory().used / 1000000000
print("the percentage of used RAM :", x)
# 79.2
# you can calculate percentage of available memory
# y = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
# print("percentage of available memory :", y)
# 20.8

z = psutil.virtual_memory().total / 1000000000
print("total of available memory :", z)
