import datetime
from model.ScheduledPayment import ScheduledRepayment

class Loan:
    def __init__(self, user_id, amount, term, repayment_frequency):
        self.user_id = user_id
        self.amount = int(amount)
        self.term = int(term)
        self.status = 'PENDING'
        self.repayment_frequency = repayment_frequency
        self.scheduled_repayments = []
        self.scheduled_repayments = self.generate_scheduled_repayments()

    def approve_loan(self):
        self.status = 'APPROVED'
    
    def get_loan_details(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'amount': self.amount,
            'term': self.term,
            'status': self.status,
            'repayment_frequency': self.repayment_frequency,
            'scheduled_repayments': self.scheduled_repayments
        }
    

    def generate_scheduled_repayments(self):
        for i in range(self.term):
            date = datetime.date.today() + datetime.timedelta(days=i * 7)
            amount = self.amount / self.term
            scheduled_repayment = ScheduledRepayment(date, amount)
            self.scheduled_repayments.append(scheduled_repayment)
        return self.scheduled_repayments

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'amount': self.amount,
            'term': self.term,
            'status': self.status,
            'repayment_frequency': self.repayment_frequency,
            'scheduled_repayments': [repayment.to_json() for repayment in self.scheduled_repayments]
        }

