import webapp2

from backend.transactions import Transaction, TransactionConnector
from backend.transactions import validate


class TransactionHandler(webapp2.RequestHandler):

    def __init__(self, request, response):
        self.initialize(request, response)
        self.user_conn = TransactionConnector()
        self.transaction_conn = TransactionConnector()

    def post(self):
        new_transaction = Transaction(str(self.request.get("projectId")),
                              str(self.request.get("userId")),
                              str(self.request.get("money")))
        if validate(self.response, new_transaction):
            if self.transaction_conn.support_project(new_transaction.user_id, new_transaction.project_id, new_transaction.money):
                self.response.status = 201
            else:
                self.response.status = 400

app = webapp2.WSGIApplication([
    ('/transaction', TransactionHandler)
])