# coding:utf8
# Author:Victor Chi
import random

# 预测模型
# link = https://facert.gitbooks.io/python-data-structure-cn/3.%E5%9F%BA%E6%9C%AC%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/3.14.%E6%A8%A1%E6%8B%9F%EF%BC%9A%E6%89%93%E5%8D%B0%E6%9C%BA/

class Printer:
    '''为了设计此模拟，我们将为上述三个真实世界对象创建类：Printer, Task, PrintQueue
Printer 类（Listing 2）需要跟踪它当前是否有任务。如果有，则它处于忙碌状态（13-17 行），并且可以从任务的页数计算所需的时间。
构造函数允许初始化每分钟页面的配置，tick 方法将内部定时器递减直到打印机设置为空闲(11 行)'''

    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            # print(self.timeRemaining,'--')
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        # 更改状态
        self.currentTask = newtask
        # 获取打印剩余的时间
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate
        print('print feed time {}'.format(self.timeRemaining))


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


from pythonds.basic.queue import Queue


def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagesPerMinute):
    # 设置打印机每分钟打印的次数
    labprinter = Printer(pagesPerMinute)
    # 创建一个打印机队列
    printQueue = Queue()
    # 等待的时间
    waitingtimes = []

    # 等待的时间
    for currentSecond in range(numSeconds):
        # print('currentSecond ',currentSecond)
        # 如果是一个新的任务,每180s会有一个任务
        if newPrintTask():
            print('add Task ', currentSecond)
            # 创建一个新的任务将时间戳填入进去
            task = Task(currentSecond)
            # 将开启任务的currentSecond跟页数添加进入队列里面
            printQueue.enqueue(task)

        # 如果任务不在进行并且队列中还有任务
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            # 从队列中调取下一个任务
            nexttask = printQueue.dequeue()
            # 创建任务的时间戳-当前的时间戳是等待的时间
            wait = nexttask.waitTime(currentSecond)
            print('wait time ', wait)
            waitingtimes.append(nexttask.waitTime(currentSecond))
            # 计算完成本次任务需要的时间
            labprinter.startNext(nexttask)
        # 开始完成任务,当完成时开启下一次任务
        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()), len(waitingtimes))


#
for i in range(10):
    simulation(3600, 5)
    # simulation(360000, 5)

    # a = Task(60)
    # print(a)
