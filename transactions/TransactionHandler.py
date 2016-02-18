from google.appengine.api import users
import webapp2

from transactions.TransactionConnector import Transaction, TransactionConnector


class TransactionHandler(webapp2.RequestHandler):

    def __init__(self, request, response):
        self.initialize(request, response)
        self.user_conn = TransactionConnector()
        self.transaction_conn = TransactionConnector()

    def post(self):
        new_transaction = Transaction(str(self.request.get("projectId")),
                              str(self.request.get("userId")),
                              str(self.request.get("money")))
        if self.transaction_conn.insert_into(new_transaction):
            self.response.status = 201
        else:
            self.response.status = 400

app = webapp2.WSGIApplication([
    ('/transaction', TransactionHandler)
])