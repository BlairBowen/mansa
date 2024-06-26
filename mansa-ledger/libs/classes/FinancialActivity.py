import datetime

ACTIVITY_TYPES = ["income", "expense_fixed", "debt", "expense_flexible", "savings"]
TAXABLE = True
NON_TAXABLE = False


def date_validator(date):
    if date is str():
        return datetime.datetime.strptime(date, "%Y%m%d")
    else:
        raise ValueError("not a valid date")


def activity_type_validator(activity_type):
    if activity_type in ACTIVITY_TYPES:
        return activity_type
    else:
        raise KeyError(f"{activity_type} is not a valid activity type")


def amount_converter(amount):
    amount = float(amount)
    amount = round(amount, 2)
    return amount


class FinancialActicity:
    def __init__(
        self,
        date: str,
        transaction_id: int,
        account: str,
        category: str,
        amount: float,
        activity_type: str,
        payment_method: str,
        entity: str,
        description: str = None,
        taxable: bool = False,
        subcategory: str = None,
        tags: list = [],
        notes: str = None,
    ) -> None:
        self.amount = amount_converter(amount)
        self.activity_type = activity_type_validator(activity_type)
        self.date = date_validator(date)
        self.entity = entity
        self.description = description
        self.transaction_id = transaction_id
        self.account = account
        self.category = category
        self.payment_method = payment_method
        self.taxable = taxable
        self.subcategory = subcategory
        self.tags = tags
        self.notes = notes
