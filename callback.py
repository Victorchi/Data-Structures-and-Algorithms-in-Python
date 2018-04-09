#!/usr/bin/python
# coding=utf-8
class simhash:
    # 构造函数
    def __init__(self, tokens='', hashbits=128):
        self.hashbits = hashbits
        self.hash = self.simhash(tokens)

    # toString函数
    def __str__(self):
        return str(self.hash)

    # 生成simhash值
    def simhash(self, tokens):
        v = [0] * self.hashbits
        for t in [self._string_hash(x) for x in tokens]:  # t为token的普通hash值
            for i in range(self.hashbits):
                bitmask = 1 << i
                if t & bitmask:
                    v[i] += 1  # 查看当前bit位是否为1,是的话将该位+1
                else:
                    v[i] -= 1  # 否则的话,该位-1
        fingerprint = 0
        for i in range(self.hashbits):
            if v[i] >= 0:
                fingerprint += 1 << i
        return fingerprint  # 整个文档的fingerprint为最终各个位>=0的和

    # 求海明距离
    def hamming_distance(self, other):
        x = (self.hash ^ other.hash) & ((1 << self.hashbits) - 1)
        tot = 0
        while x:
            tot += 1
            x &= x - 1
        return tot

    # 求相似度
    def similarity(self, other):
        a = float(self.hash)
        b = float(other.hash)
        if a > b:
            return b / a
        else:
            return a / b

    # 针对source生成hash值   (一个可变长度版本的Python的内置散列)
    def _string_hash(self, source):
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** self.hashbits - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            return x


def levenshtein_distance(first, second):
    '''
    计算两个字符串之间的L氏编辑距离
    :输入参数 first: 第一个字符串
    :输入参数 second: 第二个字符串
    :返回值: L氏编辑距离
    '''
    if len(first) == 0 or len(second) == 0:
        return len(first) + len(second)
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [range(second_length) for i in range(first_length)]  # 初始化矩阵
    for i in range(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i - 1][j] + 1
            insertion = distance_matrix[i][j - 1] + 1
            substitution = distance_matrix[i - 1][j - 1]
            if first[i - 1] != second[j - 1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion, deletion, substitution)
    return distance_matrix[first_length - 1][second_length - 1]


if __name__ == '__main__':
    s = 'Sklavos, Nicolas et al., Wireless security and cryptography. Specifications and implementations. Boca Raton, FL: CRC Press'.lower()
    hash1 = simhash(s.split())

    s = 'Sklavos, Nicolas et al., Wireless security and cryptography. Specifications and implementations. Boca Raton, FL: CRC Press'.lower()
    hash2 = simhash(s.split())

    s = 'Sklavos, Nicolas et al., Wireless security and cryptography. Specifications and implementations. Boca Raton, FL: CRC Pressq'.lower()
    hash3 = simhash(s.split())

    # print(hash1.hamming_distance(hash2), "   ", hash1.similarity(hash2))
    # print(hash1.hamming_distance(hash3), "   ", hash1.similarity(hash3))

    print(levenshtein_distance("垃圾消息", "A垃圾信息"))  # 运行结果为：2)
