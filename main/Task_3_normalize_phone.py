import re


def normalize_phone(phone_number):
    clean_numb = re.sub(r"\D", "", phone_number) #видаляємо всі зайві символи, залишаємо тільки цифри
    if len(clean_numb) == 12: #вводимо перевірку на перфікс і змінюємо в різних патернах
        clean_numb = re.sub(r"^3", "+3", clean_numb) #оскільки префіск не додається, ми міняємо перші цифри на потрібні префікси
    elif len(clean_numb) == 11:
        clean_numb = re.sub(r"^8", "+38", clean_numb)
    else:
        clean_numb = re.sub(r"^0", "+380", clean_numb)
    return clean_numb

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    ]

sanitized_numbers = [normalize_phone(phone_number) for phone_number in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

