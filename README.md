Load App.

Endpoints: 

PUT /loans 

{
    "user_id": "1234",
    "amount": "10000",
    "term":4
}

GET /loans

GET /loans/<loan-id>

GET /loans/user/<user-id>

POST /loans/<loan-id>/approve

Get /loans/<loan-id>/repayments

POST /loans/<loan-id>/repayments {"repayment_amount" : 4000}

To run app:

cd app

pip install flask
python .\app.py

To run tests:

cd tests
python .\run_tests.py


