'''
Convert string into a datetime object,
date_string = "May 21 2021 1:30PM"
Ouput: 2021-05-21 13:30:00

'''

from datetime import datetime

datetime_object = datetime.strptime('May 21 2021 1:30PM', '%b %d %Y %I:%M%p')
print(datetime_object)
