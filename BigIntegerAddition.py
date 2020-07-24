class BigNumber(object):
    def __init__(self, data):
        self.value = str(data)

    def add(self, big_number: 'A BigNumber object'):

        place = len(self.value)
        if place < len(big_number.value):
            place = len(big_number.value)

        # 空位补0
        num0 = self.value.zfill(place)
        num1 = big_number.value.zfill(place)

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

        self.value = str_num_result


import unittest


class TestDoubleStack(unittest.TestCase):
    def setUp(self):
        pass

    def test_add(self):
        num_1 = BigNumber(14567890789009876)
        num_2 = BigNumber(567893045987645324526374859)
        num_2.add(num_1)
        print(num_2.value)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
