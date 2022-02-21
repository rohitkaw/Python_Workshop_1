'''
Calculate number of days between two given dates 2019-02-25 and 2020-09-17

'''

import datetime

date1 = datetime.date(2019, 2, 25)
date2 = datetime.date(2020, 9, 17)
allDays = (date2 - date1)

# checking if first date is smaller that second one:
if (allDays.days > 0):
    print("No. of days are: ", allDays.days)
else:
    print("first date is smaller than Second")
