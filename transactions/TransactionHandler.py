from google.appengine.api import users
import webapp2
from UsersConnector import UserConnector, User

from transactions.TransactionConnector import Transaction, TransactionConnector


class TransactionHandler(webapp2.RequestHandler):

    def __init__(self, request, response):
        self.initialize(request, response)
        self.user_conn = UserConnector()
        self.project_conn = TransactionConnector()

    def post(self):
        new_project = Transaction(str(self.request.get("projectId")),
                              str(self.request.get("userId")),
                              str(self.request.get("money")))

        self.project_conn.insert_into(new_project)

app = webapp2.WSGIApplication([
    ('/transaction', TransactionHandler)
])