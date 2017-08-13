
def is_leap_year(year, is_gregorian):

    if is_gregorian :
        if  (year % 4 != 0):
            return False
        
        if (year % 100 != 0):
            return True

        if  (year % 400 == 0):
            return True
        
        return False

    if  (year % 4 == 0):
        return True
    else:
        return False

def is_gregorian(year):
    return False if year < 1918 else True
    
def get_fev_days(year):

    if year < 1918:
        return 29 if is_leap_year(year, False) else 28

    if year > 1918:
        return 29 if is_leap_year(year, True) else 28

    return 15

def init_calendar(year):
    gregorian_calendar = [31, get_fev_days(year), 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
    julian_calendar = [31, get_fev_days(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return gregorian_calendar if is_gregorian(year) else julian_calendar

year = 2016
calendar = init_calendar(year)

b = 0
month = 0

while b < 252:
    b += calendar[month]
    month += 1

day = 256 - (b - calendar[month])
print "%02d.%02d.%04d" % (day, month, year)

