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
    list = ["banana", "grapes", "apple"]
    fruit_index = list.index(a)
    return fruit_index

print('list_index("grapes")', list_index("grapes"))

def list_count(a):
    list = ["banana", "grapes", "apple", "grapes"]
    fruit_count = list.count(a)
    return fruit_count

print('list_count("grapes")', list_count("grapes"))

def list_extend(a, b):
    fruit_list = ["banana", "grapes", "apple", "grapes"]
    new_fruit_list = (a, b)
    fruit = fruit_list.extend(new_fruit_list)
    return fruit

print('list_extend("pineapple", "durian")', list_extend("pineapple", "durian"))



def list_sort():
    fruit_list = [1, 2, 3, 4, 5, 6, 7]
    return fruit_list

print('list_sort(2, 4)', list_sort())