sales =map(int, input('Sales data(seperate by comma): ').split(','))
print('Map object for above sales of the week:', list(sales))
second_week = [651,752,366,76,368,455,88]
sales.extend(second_week)
print ('Sales in last two weeks:', sales)

last_day=int(input('Last day sales:'))
sales.append(last_day)
print('Sales in last two weeks(appended last day sales):', sales)
