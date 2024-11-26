from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_difference = (birthday_this_year - today).days

        if 0 <= days_difference <= 7:
            if birthday_this_year.weekday() in [5, 6]:
                while birthday_this_year.weekday() != 0:
                    birthday_this_year += timedelta(days=1)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "Alice", "birthday": "1990.11.26"},  # Завтра, понеділок.
    {"name": "Bob", "birthday": "1985.11.27"},    # Післязавтра, вівторок.
    {"name": "Charlie", "birthday": "1992.11.30"},  # Субота, переноситься на 02.12 (понеділок).
    {"name": "Diana", "birthday": "2000.12.01"},    # Неділя, переноситься на 02.12 (понеділок).
    {"name": "Eve", "birthday": "1988.01.01"},  # Уже був у цьому році, буде врахований у 2025.
    {"name": "Frank", "birthday": "1995.12.10"},  # Позамежний діапазон, не враховувати.
    {"name": "Grace", "birthday": "1999.11.24"},  # Сьогоднішній день.
]

print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))
