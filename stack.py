# coding:utf8
# Author:Victor Chi

# 栈的简单应用:括号匹配问题

class StackUnderflow(ValueError):
    pass


class SStack():
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems

    def top(self):
        if self._elems == []:
            raise StackUnderflow('in SStack.top()')

    def push(self, elem):
        self._elems.append(elem)
        return self._elems
    def pop(self):
        if self._elems == []:
            raise StackUnderflow('in SStack.pop()')
        return self._elems.pop()


def check_parens(text):
    '''括号配对检查函数,text是被检查的正文'''
    parens = "()[]{}"
    open_parens = "([{"
    opposite = {')': '(', ']': '[', "}": "{"}  # 表示配对关系的字典

    def parentheses(text):
        '''括号生成器,每次调用返回text里的下一个括号及其位置'''
        i, text_len = 0, len(text)
        while i < text_len and text[i] not in parens:
            i += 1
        if i >= text_len:
            return
        yield text[i], i
        i += 1

    st = SStack()  # 保存括号的栈

    for pr, i in parentheses(text):
        print(pr,i)
        if pr in open_parens:
            st.push(pr)
            print(pr)
            # print(opposite['{'])
        elif st.pop() != opposite[pr]:  # 不匹配则退出
            print('Unmatching is found at ', i, ' for ', pr)
            return False
    print("All paren theses are correctly matched")
    return True
if __name__ == '__main__':


    text = '{'
    check_parens(text)
