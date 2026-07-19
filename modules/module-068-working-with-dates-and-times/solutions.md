# Module 068: Working with Dates and Times — Solutions

```python
from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo


# 1. Current date, time, and datetime
print("Today:", date.today())
print("Now:", datetime.now())
print("Current time:", datetime.now().time())


# 2. Date arithmetic
today = date.today()
plus_30 = today + timedelta(days=30)
minus_45 = today - timedelta(days=45)
print(f"Today: {today}, +30d: {plus_30}, -45d: {minus_45}")


# 3. strftime formatting
dt = datetime(2025, 12, 25, 10, 30, 0)
fmt1 = dt.strftime("%m/%d/%Y %I:%M %p")
fmt2 = dt.strftime("%Y-%m-%d %H:%M:%S")
print("Format 1:", fmt1)
print("Format 2:", fmt2)


# 4. strptime parsing
parsed = datetime.strptime("July 4, 2026 at 09:15", "%B %d, %Y at %H:%M")
print("Parsed:", parsed)


# 5. Timezone conversion
utc_dt = datetime(2025, 6, 15, 12, 0, 0, tzinfo=ZoneInfo("UTC"))
eastern = utc_dt.astimezone(ZoneInfo("US/Eastern"))
tokyo = utc_dt.astimezone(ZoneInfo("Asia/Tokyo"))
print(f"UTC: {utc_dt}")
print(f"Eastern: {eastern}")
print(f"Tokyo: {tokyo}")


# 6. Age calculator
def age(birth_date_str: str) -> int:
    birth = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
    today = date.today()
    return today.year - birth.year - (
        (today.month, today.day) < (birth.month, birth.day)
    )


print("Age for 1990-05-15:", age("1990-05-15"))
```
