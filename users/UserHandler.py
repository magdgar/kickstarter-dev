from google.appengine.api import users
import webapp2
from UsersConnector import UserConnector, User


class UserHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            user_conn = UserConnector()
            response = user_conn.select_where(["google_id"], ("google_id = %s" % user.user_id()))
            if len(response) < 1:
                new_user = User(str(user.user_id()), user.nickname())
                user_conn.insert_into(new_user)
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))

        self.response.out.write(greeting)


app = webapp2.WSGIApplication([
    ('/login', UserHandler)
])