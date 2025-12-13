import re 
def normalize_phone(phone_number: str) -> str: 
    number = re.sub(r"[^0-9]", "", phone_number)
    if phone_number.startswith('+'):
        return '+' + number
    elif number.startswith("380"):
        return '+' + number
    else:
        return "+38" + number

file = open('phones.txt', 'r', encoding='utf-8')
lines = file.readlines() 
for line in lines:
    phone = line.strip()
    if phone:
        normalized_phone = normalize_phone(phone)
        print(normalized_phone)
file.close()
    