import json

import webapp2

from ProjectConnector import ProjectConnector, Project
from users.UsersConnector import UserConnector


class ProjectsHandler(webapp2.RequestHandler):

    def __init__(self, request, response):
        self.initialize(request, response)
        self.user_conn = UserConnector()
        self.project_conn = ProjectConnector()

    def get(self):
        name = str(self.request.get("name"))

        if name != "":
            rows = self.project_conn.select_all_where("name = '%s'" % name)
        else:
            rows = self.project_conn.select_all()

        response = []
        for row in rows:
            obj = {
                'id': row[0],
                'name': row[1],
                'description': row[2],
                'creatorid': row[3],
                'creatorname': self.user_conn.select_where(["name"], "id = %s" % row[3])[0][0],
                'money': row[4],
                'date': str(row[5]),
            }
            response.append(obj)

        self.response.out.write(json.dumps(response))

    def post(self):
        new_project = Project(str(self.request.get("name")),
                              str(self.request.get("desc")),
                              str(self.request.get("creatorId")))

        if self.project_conn.insert_into(new_project):
            self.response.status = 201
        else:
            self.response.status = 400


app = webapp2.WSGIApplication([
    ('/projects', ProjectsHandler)
])