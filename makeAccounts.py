#!coding:utf8
import random

"""
    1.以@163.com结尾
    2.长度由用户输入，产生多少条也由用户输入
    3.用户名不能重复
    4.用户名必须由大写字母、小写字母、数字组成
"""

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

low_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

big_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

total_list = num_list + low_list + big_list

left_list = []

# 检测新生成的账号是否在已有列表中
def check_not_same(new, old_list):
    if new in old_list:
        return True
    else:
        return False

# 生成随机数字
def make_rangenum():
    x = random.choice(num_list)
    return x

# 生成随机大写字母
def make_bigger():
    y = random.choice(big_list)
    return y

# 生成随机小写字母
def make_lower():
    z = random.choice(low_list)
    return z

# 生成账号左侧部分，同时校验长度
def make_range(lenth):
    if int(lenth) < 3:
        raise Exception('长度至少要大于3')

    # 当长度大于3，首先保证至少有一个数字，一个大写和一个小写，然后看长度在补充位
    first = make_lower()+make_bigger() + str(make_rangenum())
    remain_len = lenth - 3
    if remain_len == 0:
        return first
    else:
        remainString = ''
        for i in range(0, remain_len):
            f = str(random.choice(total_list))
            remainString = remainString + f
        fullString = first + remainString
    return fullString

# 调用其他方法生成，传入账号长度和和所需账号的个数
def make_account(length, num):
    account_list = []
    RIGHT = '@163.com'
    m = 0
    while m < num:
        LEFT = make_range(length)
        if check_not_same(LEFT, left_list):
            pass
        else:
            FULL = LEFT + RIGHT
            account_list.append(FULL)
            m = m + 1
    return account_list


for s in make_account(8, 5):
    print(s)