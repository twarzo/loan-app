from unittest.mock import MagicMock
from db.LoanRepository import LoanRepository
from service.LoanManager import LoanManager
import unittest

class MockLoan:
    def __init__(self, id, user_id, amount, term, status, scheduled_repayments):
        self.id = id
        self.user_id = user_id
        self.amount = amount
        self.term = term
        self.status = status
        self.scheduled_repayments = scheduled_repayments

class MockRepayment:
    def __init__(self, amount, due_date, status):
        self.date = due_date
        self.amount = amount
        self.status = status

class TestLoanManager(unittest.TestCase):
    def setUp(self):
        self.loan_repository = LoanRepository()
        self.loan_manager = LoanManager(self.loan_repository)
        self.loan1 = MockLoan(id=1, user_id=1, amount=1000, term=12, status="APPROVED", scheduled_repayments=[MockRepayment(amount=100, due_date="2022-01-01", status="PENDING")])
        self.loan2 = MockLoan(id=2, user_id=2, amount=2000, term=24, status="PENDING", scheduled_repayments=[])

    def test_create_loan(self):
        self.loan_repository.create_loan = MagicMock(return_value=self.loan1)
        loan = self.loan_manager.create_loan(1, 1000, 12)
        self.assertEqual(loan.amount, self.loan1.amount)
        self.assertEqual(loan.id, self.loan1.id)
        self.loan_repository.create_loan.assert_called_once()
    
    def test_get_loans(self):
        self.loan_repository.get_loans = MagicMock(return_value=[self.loan1, self.loan2])
        loans = self.loan_manager.get_loans()
        self.assertEqual(loans, [self.loan1, self.loan2])
        self.loan_repository.get_loans.assert_called_once()
    
    def test_get_loan(self):
        self.loan_repository.get_loan = MagicMock(return_value=self.loan2)
        loan = self.loan_manager.get_loan(2)
        self.assertEqual(loan.amount, self.loan2.amount)
        self.assertEqual(loan.id, self.loan2.id)
        self.loan_repository.get_loan.assert_called_once_with(2)
    
    def test_approve_loan(self):
        self.loan_repository.get_loan = MagicMock(return_value=self.loan1)
        self.loan_repository.update_loan = MagicMock()
        self.loan_manager.approve_loan(1)
        self.loan_repository.update_loan.assert_called_once_with(self.loan1)
    
    def test_add_repayment(self):
        self.loan1.status = "APPROVED"
        self.loan_repository.get_loan = MagicMock(return_value=self.loan1)
        self.loan_repository.update_loan = MagicMock()
        self.loan_manager.add_repayment(1, 100)
        self.loan_repository.update_loan.assert_called_once()
    
    def test_get_loans_by_user_id(self):
        self.loan_repository.get_loans_by_user = MagicMock(return_value=[self.loan1])
        loans = self.loan_manager.get_loans_by_user_id(1)
        self.assertEqual(loans, [self.loan1])
        self.assertEqual(loans[0].user_id, 1)
        self.loan_repository.get_loans_by_user.assert_called_once_with(1)


