from datetime import datetime 

def get_days_from_today(date):
    try:
         given_date = datetime.strptime(date, "%Y-%m-%d")
         current_date = datetime.now()
         return (current_date - given_date).days
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."
    except TypeError:
        return  "INVALID INPUT"




my_date = "2020-10-09"
result = get_days_from_today(my_date)

if isinstance(result, int):
    print(f"Days from {my_date} to today: {result} days")
else:
    print(result)
    
    