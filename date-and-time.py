def append_time(a, b, c):
    at = datetime.time(a, b, c)
    return '{}h:{}m:{}s'.format(at.hour, at.minute, at.second)

print('append_time(12, 3, 8)', append_time(12, 3, 8))


def convert_date_to_string(datestring):
    return datestring.strftime("%A, %d %b %Y")

print('convert_date_to_string(datetime.datetime.now()', convert_date_to_string(datetime.datetime.now()))


def convert_string_to_date(datestring):
    datetimestring = datetime.datetime.strptime(datestring, "%b %d %Y %I:%M")
    return datetimestring

print('convert_string_to_date("Aug 07 2019 03:27PM")', convert_string_to_date('Aug 07 2019 03:27'))


def aug_calendar(year, month):
    cal = calendar.prmonth(year, month)
    return cal

print('aug_calendar(2019, August)', aug_calendar(2019, 8))


def date_monthrange(year, month):
    return calendar.monthrange(year, month)

print('date_monthrange(2016, July)', date_monthrange(2016, 7))


def date_weekheader(n):
    return calendar.weekheader(n)

print('date_weekheader(3)', date_weekheader(3))


def date_leapdays(year1, year2):
    return calendar.leapdays(year1, year2)

print('date_leapdays(2000, 2020)', date_leapdays(2000, 2020))


def date_monthdayscalendar(year, month):
    obj = calendar.Calendar()
    return obj.monthdayscalendar(year, month)

print('date_monthdayscalendar(2015, 5)', date_monthdayscalendar(2015, 5))


def date_isleap(year):
    return calendar.isleap(year)

print('date_isleap(2020)', date_isleap(2020))


def date_monthcalendar(year, month):
    return calendar.monthcalendar(year, month)

print('date_monthcalendar(2014, 5)', date_monthcalendar(2014, 5))

