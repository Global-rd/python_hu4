from datetime import datetime as dt
from datetime import timezone, timedelta

now = dt.now(timezone.utc)
print(now)
print(type(now))

# STRING TO DATE
date_string = "2026-04-28 19:04:00"
date_object = dt.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(date_object)
print(type(date_object))

# DATE TO STRING
date_string = dt.strftime(date_object, "%Y*%m*%d %H_%M_%S")
print(date_string)

days_difference = timedelta(days=5, hours=12)
new_date = now + days_difference
print(new_date)

