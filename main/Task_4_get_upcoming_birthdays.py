from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    greet_list_of_dict = [] #у цьому списку словників будемо збирати тих, кого вітати. Це результат функції
    today_date = datetime.today().date()

    for user in users:
        birth_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date() #перводимо str to date
        birthday_this_year = birth_date.replace(year=today_date.year) #замінюємо рік на поточний

        if birthday_this_year < today_date: #якщо дата пройшла - рік замінюємо на наступний
            birthday_this_year = birthday_this_year.replace(year=today_date.year + 1)
        
        delta_days = (birthday_this_year-today_date).days
        if 1 <= delta_days <= 7: #перевірка на входження у 7 днів
            if birthday_this_year.weekday() == 5:  #перевірка на вихідні (субота) + переносимо дату на понеділок
                birthday_this_year = birthday_this_year + timedelta(days=2)
                greet_list_of_dict.append({ 
                "name": user["name"], 
                "congratulation_date": birthday_this_year.strftime("%Y-%m-%d") 
                })
            elif birthday_this_year.weekday() == 6:  #перевірка на вихідні (неділя)
                birthday_this_year = birthday_this_year + timedelta(days=1)
                greet_list_of_dict.append({ 
                "name": user["name"], 
                "congratulation_date": birthday_this_year.strftime("%Y-%m-%d") 
                })
            else:
                greet_list_of_dict.append({ 
                "name": user["name"], 
                "congratulation_date": birthday_this_year.strftime("%Y-%m-%d") 
                })
    return greet_list_of_dict    
 
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Joe Smith", "birthday": "1990.03.01"},
    {"name": "Zoe Dash", "birthday": "1990.02.14"}, #тут у нас субота
    {"name": "Jin Dode", "birthday": "1985.02.15"}, #тут у нас неділя
    {"name": "Jane Sent", "birthday": "1990.02.13"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)