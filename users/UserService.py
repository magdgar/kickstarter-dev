from google.appengine.api import users
from UsersConnector import UserConnector, User


def get_user():
    user = users.get_current_user()
    if user:
        user_conn = UserConnector()
        response = user_conn.select_where(["google_id"], ("google_id = %s" % user.user_id()))
        if len(response) < 1:
            new_user = User(str(user.user_id()), user.nickname())
            user_conn.insert_into(new_user)
            return True
    else:
        return False