# Module 068: Working with Dates and Times — Exercises

1. **Current datetime**: Get the current date, time, and datetime separately using `date.today()`, `datetime.now()`, and `time`. Print each.

2. **Date arithmetic**: Calculate the date 30 days from today and the date 45 days before today using `timedelta`. Print all three dates.

3. **strftime formatting**: Create a `datetime` object for `2025-12-25 10:30:00`. Format it as: `"12/25/2025 10:30 AM"` and `"2025-12-25 10:30:00"`.

4. **strptime parsing**: Parse the string `"July 4, 2026 at 09:15"` using `strptime` with the appropriate format string.

5. **Timezone conversion**: Create a timezone-aware datetime for `"2025-06-15 12:00:00"` in UTC. Convert it to `"US/Eastern"` and `"Asia/Tokyo"` using `zoneinfo`. Print all three.

6. **Age calculator**: Write a function `age(birth_date_str)` that parses a birth date string (format: "YYYY-MM-DD") and returns the person's age in years as of today.
