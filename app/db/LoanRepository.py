
class LoanRepository:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.loans = []

    def get_loans(self):
        return self.loans

    def get_loan(self, loan_id):
        for loan in self.loans:
            if loan.id == loan_id:
                return loan
        return None

    def create_loan(self, loan):
        loan.id = len(self.loans) + 1
        self.loans.append(loan)
        return loan
        
    def get_loans_by_user(self, user_id):
        return [loan for loan in self.loans if loan.user_id == user_id]

    def update_loan(self, loan):
        for i, stored_loan in enumerate(self.loans):
            if stored_loan.id == loan.id:
                self.loans[i] = loan
                break
