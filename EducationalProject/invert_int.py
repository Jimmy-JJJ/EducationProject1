from math import floor

def invert_int(some_int):
    list_num = []
    for i in str(some_int):
        list_num.append(i)
    my_nums = []
    list_len = len(list_num)
    for i in range(len(list_num)):
        my_nums.insert(1,list_num[i-1])
    print(my_nums)
