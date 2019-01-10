'''
12/04/2019

2018 years
+
3 months
+
12 days

leap year: y / 400 == 0 || (y % 4 == 0 && y % 100 != 0)

year = 413
year//4 - year//100 + year//400
'''

def count_days(date):
	months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
	day, month, year = tuple(map(int, date.split('/')))
	days = year * 365 + year//400 + year//4 - year//100

	for m in range(month):
		days += months[m]

	days += day

	return days



date1 = input("Enter the first date")
date2 = input("Enter the second date")

days1 = count_days(date1)
days2 = count_days(date2)

print(abs(days1 - days2))
