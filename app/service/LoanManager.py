from db.LoanRepository import LoanRepository
from model.Loan import Loan

class LoanManager:
    def __init__(self, loan_repository = None):
        if loan_repository is None:
            self.loan_repository = LoanRepository()
        else:
            self.loan_repository = loan_repository

    def create_loan(self, user_id, amount, term):
        loan = Loan(user_id, amount, term, "WEEKLY")
        return self.loan_repository.create_loan(loan)

    def approve_loan(self, loan_id):
        loan = self.get_loan(loan_id)
        if loan == None:
            raise Exception("Loan not found")
        loan.status = 'APPROVED'
        self.loan_repository.update_loan(loan)

    def get_loans(self):
        return self.loan_repository.get_loans()
    
    def get_loan(self, loan_id):
        return self.loan_repository.get_loan(loan_id)
    
    def get_loans_by_user_id(self, user_id):
        return self.loan_repository.get_loans_by_user(user_id)

    def add_repayment(self, loan_id, repayment_amount):
        loan = self.get_loan(loan_id)
        if loan == None:
            raise Exception("Loan not found")
        
        if loan.status != 'APPROVED':
            raise Exception("Loan not approved")
        if loan.status == 'PAID':
            raise Exception("Loan already paid")
        
        for repayment in loan.scheduled_repayments:
            if repayment.status == 'PENDING':
                if repayment_amount >= repayment.amount:
                    repayment.status = 'PAID'
                break
    
        if all(repayment.status == 'PAID' for repayment in loan.scheduled_repayments):
            loan.status = 'PAID'
        self.loan_repository.update_loan(loan)
