from datetime import datetime

def get_days_from_today(d):
    input_date = datetime.strptime(d, "%Y-%m-%d").date() 
    today = datetime.today().date()
    delta = today - input_date
    return delta.days

while True:
    in_date = input("Please insert date (yyyy-mm-dd): ")
    try:
        result = get_days_from_today(in_date)
        print(f"Difference in days: {result}")
        break #завершення у разі правильної дати
    except ValueError:
        print("Incorrect date fomat, please use 'yyyy-mm-dd':")



