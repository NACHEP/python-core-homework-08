from datetime import date, datetime

def get_birthdays_per_week(users):

    week_day_names = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Monday",
        6: "Monday"
    }

    current_date = date.today()
    print(current_date)
    if not users:
        return {}
    
    day_name = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []}
    
    for user in users:
        birthdays_user = user["birthday"].replace(year=current_date.year)

        if birthdays_user < current_date:
            birthdays_user = user["birthday"].replace(year = current_date.year + 1)
           
        days_to_birthday = (birthdays_user - current_date).days

        if 0 <= days_to_birthday <= 6:
            day_name.get(week_day_names.get(birthdays_user.weekday())).append(user["name"])
            print(day_name)

    return {day: name for day, name in day_name.items() if name}
   


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},#mandag
        {"name": "Jan Suesen", "birthday": datetime(1976, 12, 12).date()},#tirsdag
        {"name": "Henrik Nielsen", "birthday": datetime(1976, 11, 4).date()},#lørdag
        {"name": "Henrik Henriksen", "birthday": datetime(1976, 12, 7).date()} #torsdag
    ]
    
    result = get_birthdays_per_week(users)
    
    # Print the result
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")