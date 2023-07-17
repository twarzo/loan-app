from service.LoanManager import LoanManager

class LoanController:
    def __init__(self, loan_manager = None):
        if loan_manager is None:
            self.loan_manager = LoanManager()
        else:
            self.loan_manager = loan_manager

    def create_loan(self, user_id, amount, term):
        return self.loan_manager.create_loan(user_id, amount, term)

    def get_loans(self):
        return self.loan_manager.get_loans()

    def get_loan(self, loan_id):
        return self.loan_manager.get_loan(loan_id)
    
    def approve_loan(self, loan_id):
        return self.loan_manager.approve_loan(loan_id)

    def add_repayment(self, loan_id, repayment_amount):
        return self.loan_manager.add_repayment(loan_id, repayment_amount)
    
    def get_loans_by_user_id(self, user_id):
        return self.loan_manager.get_loans_by_user_id(user_id)
    
    def get_repayments(self, loan_id):
        loan = self.loan_manager.get_loan(int(loan_id))
        if loan is None:
            raise Exception("Loan not found")
        return loan.scheduled_repayments