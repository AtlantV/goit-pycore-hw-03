import random

def get_numbers_ticket(min_value, max_value, quantity): #min/max -> min/max_value змінив умови завдання (так ніби правильніше аби не плутати з базовими функціями)
    numbers_set = set() 
    if min_value >= 1 and max_value <= 1000: #перевірка на відповідність умовам
        while len(numbers_set) < quantity: #виконаня за заданою кількістю цифр
            numbers_set.add(random.randint(min_value, max_value))
        return sorted(numbers_set) #виконання умови відсортованого списку
    else:
        return list(numbers_set) #можна було повернути мабуть просто новий пустий список, як варіант  
    
a = get_numbers_ticket (2, 50, 15)
print(a)
