# 链表

class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        if self._head is None:  # 空表
            raise LinkedListUnderflow(' in pop_last')
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            # print(p.next,'===')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')

    def for_each(self, proc):
        # 表的遍历
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    def elements(self):
        # 生成器
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def filter(self, pred):
        # 过滤器
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next


# mlist1 = LList()
# for i in range(10):
#     mlist1.append(i)
#
# for i in range(11, 20):
#     mlist1.append(i)
#
# mlist1.printall()


class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    # def prepend(self, elem):
    #     self._head = LNode(elem, self._head)
    #     if self._rear is None:  # 空表
    #         self._rear = self._head

    def prepend(self, elem):
        # 这个比较好一些
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e


mlist1 = LList1()
for i in range(10):
    mlist1.append(i)

print(mlist1.printall())
