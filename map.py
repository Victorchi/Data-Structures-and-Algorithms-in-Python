# coding:utf8
# Author:Victor Chi

_list = [1, 2, 3, 4, 5, 6, 7]
_list2 = []


# for i in _list:
#     a = i*i
#     _list2.append(a)

# print(_list2)

# def fun(i):
#     return i * i


a = map(lambda x:x*x,_list)

print(list(a))
