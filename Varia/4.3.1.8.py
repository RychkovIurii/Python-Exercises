def is_year_leap(year):
 if year % 400 ==0:
     return True
 elif year % 100 == 0:
     return False
 elif year % 4 == 0:
     return True
 else:
     return False

def days_in_month(year, month):
    list_months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if month == 2 and is_year_leap(year):
        return 29
    elif month == 2 and is_year_leap(year)== False:
        return 28
    return list_months[month - 1]

def day_of_year(year, month, day):
    list_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    cur_month = month
    if is_year_leap(year):
        list_months [1] = 29
    while month > 1:
        days += list_months[month - 1]
        month = month - 1
    if day <= list_months[cur_month - 1]:
        days += day
        return days
    elif day > list_months[cur_month - 1]:
        return None

print(day_of_year(2000, 12, 31))
print(day_of_year(2000, 1, 31))