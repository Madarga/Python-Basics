less than, 

def is_less_than(a, b):
    if a < b:
        return True
    else:
        return False

print('is_less_than(1, 2)', is_less_than(1, 2))

def is_greater_than(a, b):
    if a > b:
        return True
    else: 
        return False

print('is_greater_than(1, 2)', is_greater_than(1, 2))

def is_equal(a, b):
    if a == b:
        return True
    else:
        return False

print('is_equal(1, 2)', is_equal(1, 2))

def greater_and(a, b, c):
    if a > b and a > c:
        return "a is greater than b and c"
    elif b > a and b > c:
        return "b is greater than a and c"
    elif c > a and c > b:
        return "c is greater than a and b"

print('greater_or(1, 2, 3)', greater_and(1, 2, 3))
