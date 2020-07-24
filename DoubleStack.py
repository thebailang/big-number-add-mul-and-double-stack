import numpy as np


class DoubleStack(object):
    def __init__(self, long):
        # 创建空列表实现栈
        self.__long = long
        self.__list = np.zeros(self.__long)
        self.__top1 = -1  # left指针
        self.__top2 = self.__long  # right指针

    def __is_l_empty(self):
        # 判断left是否为空
        return self.__top1 == -1

    def __is_r_empty(self):
        # 判断right是否为空
        return self.__top2 == self.__long

    def __is_full(self):
        # 判断是否满栈
        return self.__top1 == self.__top2 - 1

    def l_push(self, item):
        # 压栈，left添加元素
        if self.__is_full():
            return
        else:
            self.__top1 = self.__top1 + 1
            self.__list[self.__top1] = item

    def r_push(self, item):
        # 压栈，right添加元素
        if self.__is_full():
            return
        else:
            self.__top2 = self.__top2 - 1
            self.__list[self.__top2] = item

    def l_pop(self):
        # 弹栈，弹出left最后压入栈的元素
        if self.__is_l_empty():
            return
        else:
            self.__top1 = self.__top1 - 1
            return self.__list[self.__top1 + 1]

    def r_pop(self):
        # 弹栈，弹出right最后压入栈的元素
        if self.__is_r_empty():
            return
        else:
            print(self.__top2)
            self.__top2 = self.__top2 + 1
            return self.__list[self.__top2 - 1]

    def l_top(self):
        # 取最后压入left栈的元素
        if self.__is_l_empty():
            return
        else:
            return self.__list[self.__top1]

    def r_top(self):
        # 取最后压入right栈的元素
        if self.__is_r_empty():
            return
        else:
            return self.__list[self.__top2]


import unittest


class TestDoubleStack(unittest.TestCase):
    def setUp(self):
        print("start")

    def test_l_pop(self):
        test_stack = DoubleStack(100)
        test_stack.l_pop()

    def test_r_pop(self):
        test_stack = DoubleStack(100)
        test_stack.r_pop()

    def test_l_push(self):
        test_stack = DoubleStack(100)
        test_stack.l_push("45678")

    def test_r_push(self):
        test_stack = DoubleStack(100)
        test_stack.r_push(4567)

    def tearDown(self):
        print("end")


if __name__ == "__main__":
    unittest.main()
