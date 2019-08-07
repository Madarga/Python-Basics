def count_num(x):
    n = 0
    while (n < x):
        n + 1
        return 'Finish Looping!'

print('count_num(15)', count_num(15))


def find_even_num(x):
    n = 0
    while n < x:
        if n % 2 == 0:
            even_list = []
            even_list.insert(n, n)
            return even_list
            n = n + 1

print('find_even_num(x)', find_even_num(20))


def break_loop(a):
    i = 0
    while i < a:
        return i
        i = i + 1

print('break_loop(15)', break_loop(15))


def find_item(a):
    fruit_list = ["banana", "grapes", "apple", "grapes"]
    for x in fruit_list:
        if x == a:
            return '{} is in index {}'.format(a, fruit_list.index(x))

print('find_item("apple")', find_item("apple"))


def count_even_num(num_list):
    for x in num_list:
        if x % 2 != 0:
            num_list.pop(x)
            return 'Odd Number: {}'.format(x)

print('count_even_num(20)', count_even_num([8, 3, 34, 2]))


def smallest_num_list(num_list):
    min = num_list[0]
    for x in num_list:
        if x < min:
            min = x
    return min

print('smallest_num_list(num_list([8, 3, 34, 2]))', smallest_num_list([8, 3, 34, 2]))


def get_int_five(a):
    i = 0
    while i < a:
        if i == 5:
            return i
        i += 1

print('get_int_five(10)', get_int_five(10))


def get_int_nine(a):
    i = 0
    while i < a:
        if i == 9:
            return i
        i += 1

print('get_int_nine(10)', get_int_nine(10))


def modify_list(num_list):
    return [x+1 for x in num_list]

print('modify_list(num_list([8, 3, 34, 2]))', modify_list([8, 3, 34, 2]))


def power_list(num_list):
    return [pow(x, 2) for x in num_list]

print('power_list(num_list([8, 3, 34, 2]))', power_list([8, 3, 34, 2]))
