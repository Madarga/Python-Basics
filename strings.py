def print_string(a):
    return a

print('print_string("Hello World")', print_string("Hello World"))

def substring(a, b, c):
    return a[b:c]

print('substring("Hello World")', substring("Hello World", 1, 4))

def strip_string(a):
    return a.strip()

print('strip_string("Hello World")', strip_string("   Hello World   "))

def string_len(a):
    return len(a)

print('string_len("Hello World")', string_len("Hello World"))

def lowercase_string(a):
    return a.lower()

print('lowercase_string("Hello World")', lowercase_string("Hello World"))

def uppercase_string(a):
    return a.upper()

print('uppercase_string("Hello World")', uppercase_string("Hello World"))

def replace_letter(a):
    return a.replace(a[6], 'T')

print('replace_letter("Hello World")', replace_letter("Hello World"))

def replace_word(a):
    return a.replace(a[6:], 'Kitty')

print('replace_word("Hello World")', replace_word("Hello World"))

def split_string(a):
    return a.split("-")

print('split_string("Hello-Cool-World-!")', split_string("Hello-Cool-World-!"))

def string_format(a, b):
    return '{}{}'.format(a, b)

print('string_format("My age is ", 30)', string_format("My age is ", 30))