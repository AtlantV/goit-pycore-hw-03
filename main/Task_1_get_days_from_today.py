from datetime import datetime

def get_days_from_today(d):
    try: #перевірка на формат
        input_date = datetime.strptime(d, "%Y-%m-%d").date() 
    except ValueError: 
        return "Неправильний формат дати. Використовуйте yyyy-mm-dd."
    
    today = datetime.today().date()
    delta = today - input_date
    return delta.days

d = input("Please insert date (yyyy-mm-dd): ")
result = get_days_from_today(d)

print(f"Difference in days: {result}")
