from datetime import datetime

database_date = '2021-09-01 18:37:23'

UI_date = '01 September 2021 06:37:23 PM'

str_dbDate = datetime.fromisoformat(database_date) #creates a dateoject from string

new_dbDate = str_dbDate.strftime('%d %B %Y %I:%M:%S %p')

assert UI_date == new_dbDate,"actual date is {} and exected dt is {}".format(new_dbDate,UI_date)

print("actual date is {} and exected dt is {}".format(new_dbDate,UI_date))