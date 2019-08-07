def list_append(a):
    sort_list = []
    sort_list.append(a)
    return sort_list

print('list_append("grapes")', list_append("grapes"))


def list_insert(i, a):
    fruit_list = ["banana"]
    fruit_list.insert(i, a)
    return fruit_list

print('list_insert("grapes")', list_insert(0, "grapes"))


def list_remove(a):
    fruit_list = ["banana", "grapes"]
    fruit_list.remove(a)
    return fruit_list

print('list_remove("grapes")', list_remove("grapes"))


def list_pop(i):
    fruit_list = ["banana", "grapes", "apple"]
    popped_fruit = pop_list.pop(i)
    return popped_fruit

print('list_pop(1)', list_pop(1))


def list_index(a):
    fruit_list = ["banana", "grapes", "apple"]
    fruit_index = fruit_list.index(a)
    return fruit_index

print('list_index("grapes")', list_index("grapes"))


def list_count(a):
    fruit_list = ["banana", "grapes", "apple", "grapes"]
    fruit_count = fruit_list.count(a)
    return fruit_count

print('list_count("grapes")', list_count("grapes"))


def list_extend(a, b, i):
    fruit_list = ["banana", "grapes", "apple", "grapes"]
    new_fruit_list = []
    new_fruit_list.insert(i, a)
    new_fruit_list.insert(i+1, b)
    fruit = fruit_list.extend(new_fruit_list)
    return "Extended Fruit List: {}".format(fruit_list)

print('list_extend("pineapple", "durian")', list_extend("pineapple", "durian", 0))


def list_reverse_sort(a):
    num_list = [1, 2, 3, 4, 5, 6, 7]
    return sorted(num_list, reverse=a)

print('list_reverse_sort(True)', list_reverse_sort(True))


def list_sort(num_list):
    return sorted(num_list)

print('list_sort(num_list([8, 3, 34, 2]))', list_sort([8, 3, 34, 2]))


def largest_num_list(num_list):
    max = num_list[0]
    for x in num_list:
        if x > max:
            max = x
    return max

print('largest_num_list(num_list([8, 3, 34, 2]))', largest_num_list([8, 3, 34, 2]))

