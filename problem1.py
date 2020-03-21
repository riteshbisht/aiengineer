import sys
"""
Write a method which calculates the difference between 2 dates (in terms of days) without using any library. 

The method would accept the following parameters: 

year1, month1, day1, year2, month2, day2 

Example: 

Input: 2012,1,1,2012,2,28
where, 
Start_Date: 2012-01-01
End_Date: 2012-02-28

Output: 58
"""

def get_days_of_month(month, leap_year=False):
    list_31  = [1, 3, 5, 7, 8, 10, 12]
    month_to_days = {i:31 if i in list_31 else 30 for i in range(1,13)}
    
    # for august
    month_to_days[8] = 31

    # for february
    month_to_days[2] = 28
    
    if leap_year:
        month_to_days[2] = 29
    return month_to_days[month]

if __name__ == '__main__':
    date = map(int,'2012,1,1,2012,2,28'.split(','))
    first_date = date[0:3]
    second_date = date[3:6]
    # year at 0th index , month at 1st index and day at 2nd index
    
    # calculate months 
    start_year, end_year = first_date[0], second_date[0]
    start_month, end_month = first_date[1], second_date[1]
    start_day, end_day = first_date[2], second_date[2]
    if start_year > end_year or(start_year==end_year and start_month > end_month):
        print('enter correct date')
        sys.exit()
    
    days = get_days_of_month(start_month) - start_day
    month = start_month
    while(True):
        leap = False
        month += 1
        if month > 12:
            start_year += 1
            month = month % 12
        if start_year == end_year and (month==end_month):
            days += end_day
            break
        if start_year % 4 == 0:
            leap = True
        days += get_days_of_month(month, leap)
    print(days)
        