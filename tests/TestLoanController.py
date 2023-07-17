import unittest
from unittest.mock import MagicMock
from controllers.LoanController import LoanController
from service.LoanManager import LoanManager

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

class TestLoanController(unittest.TestCase):
    def setUp(self):
        self.loan_manager = LoanManager()
        self.loan_controller = LoanController(self.loan_manager)
        self.loan1 = MockLoan(id=1, user_id=1, amount=1000, term=12, status="APPROVED", scheduled_repayments=[MockRepayment(amount=100, due_date="2022-01-01", status="PENDING")])
        self.loan2 = MockLoan(id=2, user_id=2, amount=2000, term=24, status="PENDING", scheduled_repayments=[])

    def test_create_loan(self):
        self.loan_manager.create_loan = MagicMock(return_value=self.loan1)
        loan = self.loan_controller.create_loan(1, 1000, 12)
        self.assertEqual(loan.user_id, self.loan1.user_id)
    
    def test_get_loans(self):
        self.loan_manager.get_loans = MagicMock(return_value=[self.loan1, self.loan2])
        loans = self.loan_controller.get_loans()
        self.assertEqual(len(loans), 2)
        self.loan_manager.get_loans.assert_called_once()
    
    def test_get_loan(self):
        self.loan_manager.get_loan = MagicMock(return_value=self.loan1)
        loan = self.loan_controller.get_loan(1)
        self.assertEqual(loan.user_id, self.loan1.user_id)
        self.loan_manager.get_loan.assert_called_once_with(1)
    
    def test_approve_loan(self):
        self.loan_manager.approve_loan = MagicMock()
        self.loan_controller.approve_loan(1)
        self.loan_manager.approve_loan.assert_called_once_with(1)
    
    def test_add_repayment(self):
        self.loan_manager.add_repayment = MagicMock()
        self.loan_controller.add_repayment(1, 1000)
        self.loan_manager.add_repayment.assert_called_once_with(1, 1000)
    
    def test_get_loans_by_user_id(self):
        self.loan_manager.get_loans_by_user_id = MagicMock(return_value=[self.loan1])
        loans = self.loan_controller.get_loans_by_user_id(1)
        self.assertEqual(len(loans), 1)
        self.assertEqual(loans[0].id, self.loan1.id)
        self.loan_manager.get_loans_by_user_id.assert_called_once_with(1)
    
    def test_get_repayments(self):
        self.loan_manager.get_loan = MagicMock(return_value=self.loan1)
        repayments = self.loan_controller.get_repayments(1)
        self.assertEqual(repayments, self.loan1.scheduled_repayments)
        self.loan_manager.get_loan.assert_called_once_with(1)