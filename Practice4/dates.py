from datetime import datetime, timezone
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
x = datetime.datetime(2020, 5, 21, tzinfo=timezone.utc)
print(x.strftime("%A"))
print(x.month)
print(x.day)

from datetime import datetime, timezone

x = datetime(2026, 6, 20, 14, 30, tzinfo=timezone.utc)

print(x)

u = datetime.datetime(2018, 6, 1)
print(u.strftime("%B")) # name of month
print(u.strftime("%A"))  # weekday name
print(u.strftime("%a"))  # short version of day name
print(u.strftime("%w")) # week day as numbers
print(u.strftime("%d"))  #
print(u.strftime("%C"))