from google.appengine.api import users
import webapp2
from UsersConnector import UserConnector, User


class LogoutHandler(webapp2.RequestHandler):
    def get(self):
        self.request.get("nickname")
        return webapp2.redirect(users.create_logout_url("/"))


app = webapp2.WSGIApplication([
    ('/logout', LogoutHandler)
])