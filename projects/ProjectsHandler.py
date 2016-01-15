import webapp2
import json
from ProjectConnector import ProjectConnector, Project
from UsersConnector import UserConnector

class ProjectsHandler(webapp2.RequestHandler):

    def get(self):
        sql_conn = ProjectConnector()
        user_conn = UserConnector()
        name = str(self.request.get("name"))
        if name != "":
            rows = sql_conn.select_all_where("name = '%s'" % name)
        else:
            rows = sql_conn.select_all()
        response = []

        for row in rows:
            obj = {
                'id': row[0],
                'name': row[1],
                'description': row[2],
                'creatorid': row[3],
                'creatorname': user_conn.select_where(["name"], "id = %s" % row[3])[0][0],
                'money': row[4],
                'date': str(row[5]),
            }
            response.append(obj)

        self.response.out.write(json.dumps(response))

    def post(self):
        sql_conn = ProjectConnector()
        new_project = Project(str(self.request.get("name")),
                              str(self.request.get("desc")),
                              str(self.request.get("creatorId")))

        sql_conn.insert_into(new_project)


app = webapp2.WSGIApplication([
    ('/projects', ProjectsHandler),
])