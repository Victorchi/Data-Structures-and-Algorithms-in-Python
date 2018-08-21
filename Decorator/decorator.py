'''
今天我需要写一个方法,来统计我每个方法运行了多少时间.当然我选择使用decorator这个来做.
'''
import time


def funcCost(func):
    # 不带参数，只是单纯的加一点东西。
    def inner(*args, **kwargs):
        a = time.time()
        result = func(*args, **kwargs)
        b = time.time()
        print('This function use {} time'.format(b - a))
        return result

    return inner


def discount(discount=1):
    # 加入参数来修饰一下，这个主要是可以改变的，也可以是多个参数。
    def actual_discount(function):
        def inner(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * discount

        return inner

    return actual_discount


@funcCost
def sum():
    time.sleep(0.92)
    return 1


@discount(discount=0.55)
def price():
    return 10


if __name__ == '__main__':
    a = price()
    print(a)
