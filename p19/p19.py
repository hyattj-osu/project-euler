# https://projecteuler.net/problem=19
# Counting Sundays

'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

# year -> month -> day -> day label

# year divisible by 4
# only on a century if divible by 400
def leap_check(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0): 
                return(True)
        else:
            return(True)
    return(False)

def main():

    # leap_check(2004) #y
    # leap_check(2003) #n
    # leap_check(1900) #n
    # leap_check(2000) #y

    count = 0
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day_in_week = 1
    for y in range(1900, 2001):
        for m in range(12):
            days = days_in_months[m]
            if leap_check(y) and (m == 1):
                days += 1                
            
            day_in_week = (day_in_week + days) % 7
            if day_in_week == 0 and y > 1900:
                count += 1

    print(count)

    
    return()



if __name__ == "__main__":
    main()