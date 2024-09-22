import datetime

# Function for determining the day of the week
def get_day_of_week(day, month, year):
    date = datetime.date(year, month, day)
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[date.weekday()]

# Function for checking leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# The function for calculating the age
def calculate_age(day, month, year):
    today = datetime.date.today()
    birthdate = datetime.date(year, month, day)
    age = today.year - birthdate.year
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age -= 1
    return age

digits_patterns = {
    '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
    '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
    '2': [" *** ", "    *", " *** ", "*    ", " *** "],
    '3': [" *** ", "    *", " *** ", "    *", " *** "],
    '4': ["*   *", "*   *", " *** ", "    *", "    *"],
    '5': [" *** ", "*    ", " *** ", "    *", " *** "],
    '6': [" *** ", "*    ", " *** ", "*   *", " *** "],
    '7': [" *** ", "    *", "    *", "    *", "    *"],
    '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
    '9': [" *** ", "*   *", " *** ", "    *", " *** "],
}
# Function for displaying numbers in the form of asterisks (electronic scoreboard)
def display_date_as_stars(day, month, year):
    date_str = f"{day:02} {month:02} {year}"
    for i in range(5):
        line = ""
        for char in date_str:
            if char == " ":
                line += "     "
            else:
                line += digits_patterns[char][i] + "  "
        print(line)

# The main program
def main():
    # Requesting data from the user
    day = int(input("Введите день вашего рождения (дд): "))
    month = int(input("Введите месяц вашего рождения (мм): "))
    year = int(input("Введите год вашего рождения (гггг): "))
    
    # We define the day of the week
    day_of_week = get_day_of_week(day, month, year)
    print(f"Вы родились в {day_of_week}.")

    # Checking if the year was a leap year
    leap_year = is_leap_year(year)
    if leap_year:
        print(f"{year} был високосным годом.")
    else:
        print(f"{year} не был високосным годом.")

    # Calculating the age
    age = calculate_age(day, month, year)
    print(f"Ваш возраст: {age} лет.")

    # We display the date in the form of asterisks
    print("Дата вашего рождения в формате электронного табло:")
    display_date_as_stars(day, month, year)

# start programm
if __name__ == "__main__":
    main()
