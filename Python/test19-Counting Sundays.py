""" 
    You are given the following information, but you may prefer to do some research for yourself.

*   1 Jan 1900 was a Monday.
*   Thirty days has September,
*   April, June and November.
*   All the rest have thirty-one,
*   Saving February alone,
*   Which has twenty-eight, rain or shine.
*   And on leap years, twenty-nine.
*   A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

?   How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)? 
"""


def days_for_month(year: int, month: int) -> int:
    """ return how many days in given month and year

    Args:
    ----
        year (int): 
        month (int): 

    Returns:
    ----
        int: 
    """

    if (month == 4 or 
        month == 6 or 
        month == 9 or 
        month == 11):
        return 30

    elif (month == 2 and 
        ((year % 100 == 0 and 
                year % 400 != 0) or 
                year % 4 != 0)):
        return 28

    elif month == 2:
        return 29

    else:
        return 31


def calender(year: int, month: int) -> None:
    """ create a calender and add to calender list by using previous calender

    Args:
    ----
        year (int): 
        month (int): 

    Returns:
    ----
        [type]: 
    """

    global calender_curr, calender_lst, calender_prev

    calender_curr = [0] * (7*6)   # get new calender to fill
    ## calculating firs day's possition ##
    calender_prev.reverse()
    next_start = (14 - calender_prev.index(1)) % 7  # as indexing use in python (start from 0)
    #######

    for mark in range(next_start, next_start + days_for_month(year, month)):        # from the starting point fill the calender
        calender_curr[mark] = 1

    calender_prev = calender_curr
    calender_lst.append(calender_prev.copy())  # add to calender list

    return None


def first_month() -> None:
    """ create first month """

    global calender_curr, calender_prev, calender_lst
    
    for day in range(31):
        calender_curr[day] = 1

    calender_prev = calender_curr           # add to last month for use of calculating next month
    calender_lst.append(calender_prev.copy())       # add to calender 
    
    return None


def calender_generator(end_year: int) -> int:
    """ generate calender list for given range from 1900

    Args:
    ----
        end_year (int): ending year
    """
    
    for year in range(1900, end_year + 1):
        for month in range(1, 13):
            if year != 1900 or month != 1:
                calender(year, month)
    
    return None


def sunday_1st_counter() -> int:
    """ count sundays

    Returns:
        int: sundays
    """
    count = 0
    for i in range(12, len(calender_lst)):     # star from year ahead in calender list
        cur = calender_lst[i]                   # get each month

        if cur.index(1) == 6:           # check for fist day as Sunday
            count += 1

    return count


def easy_way(end_year: int) -> int:
    import calendar

    count = 0
    for year in range(1901, end_year + 1):
        for month in range(1, 13):
            cal = calendar.monthcalendar(year, month)       # gives 2D array of days in month start from monday. if not in month it's 0
            cal = cal[0]                                  # get first week

            if cal.index(1) == 6:                         # first day is Sunday
                count += 1

    return count

    
if __name__ == '__main__':
    start_day: tuple[int, str] = (1900, 1, 1, 'Monday')

    ## create calender list for every month ##
    calender_curr: list[int] = [0] * (7 * 6)
    calender_prev: list[int] = []
    calender_lst: list[list[int]] = []          # calender list
    #########################################
    
    first_month()
    calender_generator(2000)

    print(sunday_1st_counter())
    
    #######
    # print(easy_way(2000))