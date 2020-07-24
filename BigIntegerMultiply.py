def Input():
    # 输入公式或数字
    formula_input = input("Input formula or numbe:")

    # 分离"+"号左右数字
    formula = formula_input.split("*")

    if len(formula) == 1:  # 没有"+"号需要再输入一个数字
        num0 = formula[0]
        num1 = input("Input the second number:")

    elif len(formula) == 2:  # 有"+"号左右数字提取出来
        num0 = formula[0]
        num1 = formula[1]

    else:
        print("Format error!")
        exit(-1)

    return (num0, num1)


def BigIntegerAdd(num0, num1):
    # 判断谁位数更多
    place = len(num0)
    if place < len(num1):
        place = len(num1)

    # 空位补0
    num0 = num0.zfill(place)
    num1 = num1.zfill(place)

    # 字符串>>>列表
    num_list0 = list(num0)
    num_list1 = list(num1)

    num_result = []
    # 进位符
    flag_carry = 0

    for i in reversed(range(place)):
        num = int(num_list0[i]) + int(num_list1[i]) + flag_carry
        flag_carry = num // 10
        num_result.append(str(num % 10))

    if flag_carry > 0:
        num_result.append(str(flag_carry))

    # 反向排序
    num_result.reverse()

    # 转化为字符串
    str_num_result = "".join(num_result)

    return str_num_result


def BigIntegerMul(num0, num1):
    l_number = ''
    l_count = 0
    for i in reversed(list(num0)):
        s_count = 0
        s_number = ''
        for j in reversed(list(num1)):
            median = int(i) * int(j) * 10 ** (l_count + s_count)
            s_number = BigIntegerAdd(str(median), s_number)
            s_count = s_count + 1
        l_number = BigIntegerAdd(str(l_number), s_number)
        l_count = l_count + 1
    return l_number


class BigNumber(object):
    def __init__(self, data):
        self.value = str(data)

    def mul(self, big_number: 'A BigNumber object'):
        # 指数计算和高低位保存
        l_number = ''
        l_count = 0
        for i in reversed(list(self.value)):
            # 计算一位数字和另外一个数字相乘
            s_count = 0
            s_number = ''
            for j in reversed(list(big_number.value)):
                # 计算一位数字和另外一个数值每位相乘
                median = int(i) * int(j) * 10 ** (l_count + s_count)
                s_number = self.__add(str(median), s_number)
                s_count = s_count + 1
            l_number = self.__add(str(l_number), s_number)
            l_count = l_count + 1
        self.value = l_number

    def __add(self, num0, num1):
        place = len(num0)
        if place < len(num1):
            place = len(num1)

        # 空位补0
        num0 = num0.zfill(place)
        num1 = num1.zfill(place)

        # 字符串>>>列表
        num_list0 = list(num0)
        num_list1 = list(num1)

        num_result = []
        # 进位符
        flag_carry = 0

        for i in reversed(range(place)):
            num = int(num_list0[i]) + int(num_list1[i]) + flag_carry
            flag_carry = num // 10
            num_result.append(str(num % 10))
        if flag_carry > 0:
            num_result.append(str(flag_carry))
        # 反向排序
        num_result.reverse()
        # 转化为字符串
        str_num_result = "".join(num_result)
        return str_num_result


import unittest


class TestDoubleStack(unittest.TestCase):
    def setUp(self):
        pass

    def test_mul(self):
        num_1 = BigNumber(3456789)
        num_2 = BigNumber(23543579)
        num_2.mul(num_1)
        print(num_2.value)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
