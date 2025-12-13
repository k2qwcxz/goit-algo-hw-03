import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 100:
        return []
    if min >= max or quantity > (max - min + 1):
        return []
    
    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    return numbers

result = get_numbers_ticket(1, 100, 5)
print(result)
        

