def add_to_dict(a, b):
    d = {'Name':'Michael', 'Age':30}
    d[a] = b
    return d

print('add_to_dict("Gender", "Male"', add_to_dict("Gender", "Male"))


def update_dict(a):
    d = {'Name':'Michael', 'Age':30, 'Gender':'Male'}
    d['Age'] = a
    return d

print('update_dict(32)', update_dict(32))


def pop_dict(a):
    d = {'Name':'Michael', 'Age':30, 'Gender':'Male'}
    return 'Popped: {}'.format(d.pop(a))

print('pop_dict("Gender")', pop_dict("Gender"))


def delete_dict(a):
    d = {'Name':'Michael', 'Age':30, 'Gender':'Male'}
    del d[a]
    return d

print('delete_dict("Gender")', delete_dict("Gender"))


def loop_dict(a):
    d = {'Name':'Michael', 'Age':30, 'Gender':'Male'}
    for x in d:
        if x == a:
            d1 = d.pop(x)
            return d

print('loop_dict("Gender")', loop_dict("Gender"))


def sort_dict(name_dict):
    return sorted(name_dict)

print('sort_dict(name_dict(("Michael", "John", "Anne", "Clyde")))', sort_dict(('Michael', 'John', 'Anne', 'Clyde')))


def reverse_sort_dict(name_dict):
    return sorted(name_dict, reverse=True)

print('reverse_sort_dict(name_dict(("Michael", "John", "Anne", "Clyde")))', reverse_sort_dict(('Michael', 'John', 'Anne', 'Clyde')))


def value_by_index(a):
    d = {'Name':'Michael', 'Age':30, 'Gender':'Male'}
    return list(d)[a]

print('value_by_index(1)', value_by_index(1))


def check_key(a):
    d = {'Name':'Michael', 'Age':30, 'Gender':'Male'}
    for x in d:
        if x == a:
            return '{} already exists!'.format(a) 

print('check_key("Gender")', check_key("Gender"))


def get_name(a):
    d = {'Name':'Michael', 'Age':30, 'Gender':'Male'}
    for x in d:
        if x == a:
            return x

print('get_name("Name")', get_name('Name'))









