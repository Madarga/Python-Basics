def print_tuple(a):
    fruit_tuple = ("banana", "grapes", "apple", "pineapple", "durian", "orange")
    return fruit_tuple[a]

print('print_tuple(2)', print_tuple(2))

def tuple_selected(a, b):
    fruit_tuple = ("banana", "grapes", "apple", "pineapple", "durian", "orange")
    return fruit_tuple[a:b]

print('tuple_selected(1, 5)', tuple_selected(1, 5))

def delete_tuple_elem(a, b):
    fruit_tuple = ("banana", "grapes", "apple", "pineapple", "durian", "orange")
    return fruit_tuple[a:b]

print('delete_tuple_elem(1, 3)', delete_tuple_elem(1, 3))

def member_in_tuple(a):
    fruit_tuple = ("banana", "grapes", "apple", "pineapple", "durian", "orange")
    return a in fruit_tuple

print('member_in_tuple("pineapple")', member_in_tuple("pineapple"))

def index_of(a):
    fruit_tuple = ("banana", "grapes", "apple", "pineapple", "durian", "orange")
    index = fruit_tuple.index(a)
    return index

print('index_of("durian")', index_of("durian"))

def reverse_sort_tuple(a):
    fruit_tuple = ("banana", "grapes", "apple", "pineapple", "durian", "orange")
    return sorted(fruit_tuple, reverse=a)

print('reverse_sort_tuple(True)', reverse_sort_tuple(True))

def check_member(a):
    fruit_tuple = ("banana", "grapes", "apple", "pineapple", "durian", "orange")
    if a in fruit_tuple:
        return '{} is in the tuple!'.format(a)

print('check_member("durian")', check_member("durian"))

def count_tuple(a):
    fruit_tuple = ("banana", "grapes", "grapes", "apple", "pineapple", "durian", "orange")
    return fruit_tuple.count(a)

print('count_tuple("grapes")', count_tuple("grapes"))

def replace_tuple_elem(a):
    fruit_tuple = ("banana", "grapes", "apple", "pineapple", ["durian", "orange"])
    fruit_tuple[4][1] = a
    return fruit_tuple

print('replace_tuple_elem("guyabano")', replace_tuple_elem("guyabano"))

def tuple_concat(num_tuple):
    fruit_tuple = ("banana", "grapes", "apple", "pineapple", ["durian", "orange"])
    return fruit_tuple + num_tuple

print('tuple_concat(num_tuple([3, 2, 5]))', tuple_concat((3, 2, 5)))

