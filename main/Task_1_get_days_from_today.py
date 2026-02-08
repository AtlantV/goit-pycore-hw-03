from datetime import datetime

def get_days_from_today(d):
    input_date = datetime.strptime(d, "%Y-%m-%d").date()
    today = datetime.today().date()
    delta = today - input_date
    return delta.days

d = input("Please insert date (yyyy-mm-dd): ")
result = get_days_from_today(d)

print(f"Difference in days: {result}")
