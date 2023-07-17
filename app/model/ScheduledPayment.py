class ScheduledRepayment:
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount
        self.status = "PENDING"

    def repay(self, amount):
        if amount >= self.amount:
            self.status = "PAID"
        else:
            self.status = "PARTIALLY_PAID"
    
    def to_json(self):
        return {
            'date': self.date,
            'amount': self.amount,
            'status': self.status
        }