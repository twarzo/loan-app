from flask import Flask, request
from controllers.LoanController import LoanController

app = Flask(__name__)

loan_controller = LoanController()


@app.route("/loans", methods=["PUT"])
def create_loan():
    request_data = request.get_json()
    amount = request_data.get("amount")
    user_id = request_data.get("user_id")
    term = request_data.get("term")
    loan = loan_controller.create_loan(user_id, amount, term)
    return loan.to_json()

@app.route("/loans/<loan_id>/approve", methods=["POST"])
def approve_loan(loan_id):
    try:
        loan_controller.approve_loan(int(loan_id))
        return "Loan approved", 200
    except Exception as e:
        return str(e), 500

@app.route("/loans/<loan_id>/repayments", methods=["POST"])
def add_repayment(loan_id):
    request_data = request.get_json()
    repayment_amount = request_data.get("repayment_amount")
    try:
        loan_controller.add_repayment(int(loan_id), repayment_amount)
        return "Repayment added", 200
    except Exception as e:
        return str(e), 500

@app.route("/loans", methods=["GET"])
def get_loans():
    loans = loan_controller.get_loans()
    return [loan.to_json() for loan in loans]

@app.route("/loans/<loan_id>", methods=["GET"])
def get_loan(loan_id):
    loan = loan_controller.get_loan(int(loan_id))
    if loan == None:
        return "Loan not found", 404
    return loan.to_json()

@app.route("/loans/user/<user_id>", methods=["GET"])
def get_loans_by_user_id(user_id):
    loans = loan_controller.get_loans_by_user_id(user_id)
    return [loan.to_json() for loan in loans]

@app.route("/loans/<loan_id>/repayments", methods=["GET"])
def get_repayments(loan_id):
    repayments = loan_controller.get_repayments(loan_id)
    return [repayment.to_json() for repayment in repayments]


@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == "__main__":
    app.run(debug=True)


