from google.appengine.api import users
import webapp2
from UsersConnector import UserConnector, User


class UserHandler(webapp2.RequestHandler):
    def get(self):
        path = self.request.get("path")
        if path == "":
            path = '/'
        return webapp2.redirect(users.create_logout_url(path))


app = webapp2.WSGIApplication([
    ('/logout', UserHandler)
])