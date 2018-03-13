'''
yield,写着的目的是彻底了解yeild的用法,另外严格按照pep8的规则写代码
The purpose of writing is to thoroughly understand the usage of yield,and strictly follow the rule of pep8 to write code
'''

# 迭代器 iteration
# 为了了解yield有什么用,首先理解generators,而理解generators前还要理解iterables

# Iterables

# 当你创建了一个列表,你可以一个一个的读取它的每一项,这叫做iteration
import itertools

mylist = [1, 2, 3]
for i in mylist:
    print(i)

# Mylist是可迭代的.当你用列表推导式的时候,你就创建了一个列表,而这个列表也是可迭代的:

mylist = [x * x for x in range(3)]
for i in mylist:
    print(i)

# 所有你可以用在for...in...语句中的都是可迭代的:比如lists,strings,files...因为这些可迭代的对象你可以随意的读取所以非常方便易用,
# 但是你必须把它们的值放到内存里,当它们有很多值时就会消耗太多的内存.

# yield 目的之一 减少内存的消耗

# Generators
# 生成器也是迭代器的一种,但是你只能迭代它们一次.原因很简单,因为它们不是全部存在内存里,它们只在要调用的时候在内存里生成:

mygenerator = (x * x for x in range(3))
n = 0
for i in mygenerator:
    n += 1
    print(i)
    if n == 1:
        break
# 生成器跟迭代器的区别就是用()代替[],还有你不用 for i in mygenerator 第二次调用生成器":首先计算0,然后会在内存里丢掉0去计算1,直到计算完4.

# 不会再次调用(除非生成器里面还有值)
for i in mygenerator:
    print('除非生成器里面还有值')
    print(i)


# Yield
# yield的用法和关键字return差不多

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i * i


mygenerator = createGenerator()  # 创建一个生成器


# print(mygenerator)  # mygenerator is an object

# 在这里这个例子好像没什么用,不过当你的函数要返回一个非常大的集合并且你希望只读一次的话,那么它就非常的方便了.

# 要理解Yield你必须先理解当你调用函数的时候,函数里的代码并没有运行.函数仅仅返回生成器对象,这就是它最微妙的地方:-)
# 然后呢,每当for语句迭代生成器的时候你的代码才会运转.

# 最难的部分
# 当for语句第一次调动函数里返回的生成器对象,函数里的代码就开始运作,直到碰到yield,然后会返回本次循环的第一个返回值.所以下次调用也将循环一次
# 然后返回下一个值,直到没有值可以返回
# 一旦函数运行没有碰到yield 语句就认为生成器已经为空了.原因可能是循环结束或者没有满足if/else之类的


# 控制迭代器的穷尽

class Bank(object):
    crisis = False

    def create_atm(self):
        while not self.crisis:
            yield '$100'


hsbc = Bank()
corner_street_atm = hsbc.create_atm()
# print(next(corner_street_atm))
# print([next(corner_street_atm) for cash in range(5)])

hsbc.crisis = True  # 经济危机来了,没钱了
# print(next(corner_street_atm))

wall_street_atm = hsbc.create_atm()  # 对其他的ATM 还是true
# print(next(wall_street_atm),type(wall_street_atm))

hsbc.crisis = False  # 经济危机过去了,麻烦的是,ATM里面还是空的
print(type(wall_street_atm))

brand_new_atm = hsbc.create_atm()  # 新建一个atm
print(next(brand_new_atm))

# itertools,你的好基友

# itertools模块包含了一些特殊的函数可以操作可迭代对象.有没有想过复制一个生成器?链接两个生成器?把嵌套列表里的值组织成一个列表?
# Map/Zip还不用创建另一个列表?
horses = [1, 2, 3, 4]
races = itertools.permutations(horses)  # 快速排列组合
print(races)
a = list(races)
print(type(a), len(a))

#