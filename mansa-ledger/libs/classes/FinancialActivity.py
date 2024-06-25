import datetime

ACTIVITY_TYPES = [
    "income",
    "expense_fixed",
    "debt",
    "expense_flexible",
    "savings"
]

def format_date(date):
    if date is str():
        return datetime.datetime.strptime(date, "%Y%m%d")
    elif date is datetime.date():
        return date
    else:
        raise ValueError("not a valid date")
    

def activity_type_check(activity_type):
    if type in ACTIVITY_TYPES:
        return activity_type
    else:
        raise KeyError(f"{activity_type} is not a valid activity type")


def amount_converter(amount):
    amount = float(amount)
    amount = round(amount, 2)
    return amount
            

class FinancialActicity:

    def __init__(self, activity_type, amount, date) -> None:
        self.amount = amount_converter(amount)
        self.activity_type = activity_type_check(activity_type)
        self.date = format_date(date)
        
        

