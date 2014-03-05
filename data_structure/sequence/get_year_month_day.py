#!/usr/bin/env python

months = ['January',
        'Febrary',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
        ]

day_ending = ['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']

year = raw_input('Year: ')
month = raw_input('Month(1-12): ')
day = raw_input('Day(1-31): ')

month_num = int(month)
day_num = int(day)

month_name = months[month_num-1]
day_name = day + day_ending[day_num-1]

print day_name+' '+month_name+', '+year

