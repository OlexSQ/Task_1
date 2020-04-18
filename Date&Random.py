import datetime
import random
import string

today = datetime.datetime.now()

tomorow = today + datetime.timedelta(days=1)
tomorow_string = tomorow.strftime("%d-%m-%Y %H:%S")
print(tomorow_string)

some_date_string = '2020-02-03 09:18:36.000'
some_date_datetime = datetime.datetime.strptime(some_date_string, '%Y-%m-%d %H:%M:%S.%f')
print("Day is", some_date_datetime.strftime("%d"))
print("Month is", some_date_datetime.strftime("%m"))
print("Year is", some_date_datetime.year)
print("Hour is", some_date_datetime.strftime("%H"))
print("Second is", some_date_datetime.second)

for number in range(0,3):
    print(random.randrange(100, 999, 5))

random_string = "".join(random.choice(string.ascii_letters) for i in range(10) )
print("Random generated string is", random_string)

tickets = [random.randint(1000000000, 9999999999) for i in range(100)]
winer_tickets = [random.choice(tickets) for i in range(2)]
print("Winer tickets are", winer_tickets)

try:
    error = 10 / 0
except ZeroDivisionError:
    print("Are you crazy??")
finally:
    not_error = 10 / 0.00001
    print(not_error)