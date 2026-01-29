```python
# calendar.py

import calendar
import datetime

def print_month(year, month):
    print(calendar.month(year, month))

def print_year(year):
    print(calendar.calendar(year))

def print_month_name(year, month):
    print(calendar.month_name[month] + " " + str(year))

def print_day_of_week(year, month, day):
    print(calendar.day_name[calendar.weekday(year, month, day)])

def print_days_in_month(year, month):
    print(calendar.monthrange(year, month)[1])

def print_days_in_year(year):
    print(calendar.monthrange(year, 1)[1])

def print_leap_year(year):
    if calendar.isleap(year):
        print(str(year) + " is a leap year")
    else:
        print(str(year) + " is not a leap year")

def print_today():
    today = datetime.date.today()
    print("Today's date is: " + str(today))

def main():
    print_month_name(2024, 9)
    print_day_of_week(2024, 9, 10)
    print_days_in_month(2024, 9)
    print_days_in_year(2024)
    print_leap_year(2024)
    print_today()

if __name__ == "__main__":
    main()
```

```bash
# run the script
python calendar.py
```