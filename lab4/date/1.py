#1
from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date - timedelta(days=5)

print("Current Date:", current_date.strftime('%Y-%m-%d'))
print("Date after subtracting 5 days:", new_date.strftime('%Y-%m-%d'))

#2
from datetime import datetime, timedelta

today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#3
from datetime import datetime

current_datetime = datetime.now().replace(microsecond=0)

print("Datetime without microseconds:", current_datetime)

#4
from datetime import datetime

date1 = datetime(2025, 2, 10, 12, 0, 0)  # Example date
date2 = datetime(2025, 2, 12, 14, 30, 0)  # Another example date

difference = abs((date2 - date1).total_seconds())

print("Difference in seconds:", difference)