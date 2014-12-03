__author__ = 'Administrator'


def fun2_1():  # 2-1
    print 'my name is %s' % 'xxl'


def fun2_2():  # 2-2
    print 1 + 2 * 4


def fun2_3():  # 2-3
    print 3 % 2
    print 3 ** 3


def fun2_4():  # 2-4
    v_str = raw_input('Please input a string type: ')
    print v_str
    v_int = raw_input('Please input a int type: ')
    print v_int


def fun2_5_a():  # 2_5_a
    num = 0
    while True:
        if num > 10:
            break
        print num
        num += 1


def fun2_5_b():  # 2_5_b
    for i in range(11):
        print i


def fun2_6():  # 2_6
    num = int(raw_input('Please input a num: '))
    if num > 0:
        print 'positive num'
    elif num < 0:
        print 'negative num'
    else:
        print 'zero'


def fun2_7():  # 2_7
    var_str = raw_input('Please input a string: ')
    list_char = list(var_str)
    for char in list_char:
        print char,


def fun2_8():  # 2_8
    var_num_str = raw_input('Please input five num: ')
    list_num = var_num_str.split(' ')
    print sum([int(i) for i in list_num])


def fun2_9():  # 2_9
    var_num_str = raw_input('Please input five num: ')
    list_num = var_num_str.split(' ')
    num_sum = sum([int(i) for i in list_num])
    average = num_sum / float(len(list_num))
    print average


def fun2_10():  # 2_10
    while True:
        input_num = raw_input("Please input a number between 1 and 100: ")
        if 1 < int(input_num) < 100:
            print 'Success'
            break
        else:
            print 'Please input again: '
            pass


def fun2_11():  # 2_11
    while True:
        print '(1)get the sum value of five numbers (2)get the average value of five numbers (X)exit'
        your_choice = raw_input('Please input your choice: ')
        if your_choice == '1':
            num_str = raw_input('Please input five numers: ')
            num_list = num_str.split(' ')
            num_sum = sum([int(i) for i in num_list])
            print 'The sum of the five numbers is %s' % num_sum
        elif your_choice == '2':
            num_str = raw_input('Please input five numers: ')
            num_list = num_str.split(' ')
            num_sum = sum([int(i) for i in num_list])
            num_avg = num_sum / float(len(num_list))
            print 'The average of the five numbers is %s' % num_avg
        elif your_choice == 'X':
            print 'exited'
            break

def fun2_15_a():  # 2_15_a
    num_str = raw_input('Please input three numbers: ')
    num_list = [int(i) for i in num_str.split(' ')]
    for i in range(1, len(num_list)):
        key = num_list[i]
        j = i - 1
        while j >= 0 and key < num_list[j]:
            j -= 1
        num_list[j+1] = key
    print num_list


def fun2_16():  # 2_16
    file_name = raw_input('Enter file name: ')
    fobj = open(file_name, 'r')
    for eachLine in fobj:
        print eachLine,
    fobj.close()

fun2_16()


