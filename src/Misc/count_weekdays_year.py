'''
import calendar


class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        current_month = 1
        number_of_days = 0
        while (current_month <= 12):
            for data in self.monthdays2calendar(year, current_month):
                if data[weekday][0] != 0:
                    number_of_days = number_of_days + 1

            current_month = current_month + 1
        return number_of_days

my_calendar = MyCalendar()
number_of_days = my_calendar.count_weekday_in_year(2023, calendar.MONDAY)

print(number_of_days)
'''

'''
def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s

for x in fun(2):
    print(x, end='')
'''

'''
myt = (0,1,2,3,4,5,6)
foo = list(filter(lambda x: x-0 and x-1, myt))
print(foo)
'''

'''
import random

a = random.randint(0,100)
b = random.randrange(10,100,3)
c = random.choice((0,100,3))
print(a,b,c)
'''

print(len('\\'))