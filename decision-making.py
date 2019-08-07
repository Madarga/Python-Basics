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


def greatest_num(a, b, c):
    if a > b and a > c:
        return "a is greater than b and c"
    elif b > a and b > c:
        return "b is greater than a and c"
    elif c > a and c > b:
        return "c is greater than a and b"

print('greater_or(1, 2, 3)', greatest_num(1, 2, 3))


def neg_pos_int(a):
    if a < 0:
        return '{} is a negative integer.'.format(a)
    elif a > 0:
        return '{} is a positive integer.'.format(a)
    elif a == 0:
        return '{} is a zero.'.format(a)
    else:
        return 'Please Enter a Valid Integer!'

print('neg_pos_int(-21)', neg_pos_int(-21))


def week_day(day):
    if day == 1:
        return "Sunday"
    elif day == 2:
        return "Monday"
    elif day == 3:
        return "Tuesday"
    elif day == 4:
        return "Wednesday"
    elif day == 5:
        return "Thurdsday"
    elif day == 6:
        return "Friday"
    elif day == 7:
        return "Saturday"
    else:
        return "Enter from 1 to 7."

print('week_day(6)', week_day(6))


def passing_grade(grade):
    if grade <= 100 and grade >=90:
        return 'Mark: A+'
    elif grade <= 89 and grade >= 85:
        return 'Mark: B'
    elif grade <= 84 and grade >= 80:
        return 'Mark: C'
    elif grade <= 79 and grade >= 75:
        return 'Mark: D'
    else:
        return 'Mark F'

print('passing_grade(83)', passing_grade(83))



def odd_even_num(a):
    if a % 2 == 0:
        even_num = "Number is an Even Number!"
        return even_num
    else:
        odd_num = "Number is an Odd Number!"
        return odd_num

print('odd_even_num(45)', odd_even_num(45))


def classify_triangle(a, b, c):
    if a == b and b == c:
        return "Triangle is Equilateral"
    elif a == b or a == c or b == c:
        return "Triangle is Isosceles"
    else:
        return "Triangle is Scalene"

print('classify_triangle(5, 7, 5)', classify_triangle(5, 7, 5))


def identify_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return '{} is a leap year!'.format(year)
            else:
                return '{} is not a leap year!'.format(year)
        else:
            return '{} is a leap year!'.format(year)
    else:
        return '{} is not a leap year!'.format(year)

print('identify_leap_year(2019)', identify_leap_year(2019))