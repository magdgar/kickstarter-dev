import webapp2
import json
from ProjectConnector import ProjectConnector, Project


class Projects(webapp2.RequestHandler):

    def get(self):
        sqlConn = ProjectConnector()
        name = str(self.request.get("name"))
        if name != "":
            rows = sqlConn.select_all_where("name = '%s'" % name)
        else:
            rows = sqlConn.select_all_from()
        response = []
        obj = ""
        for row in rows:
            obj = {
            'id': row[0],
            'name': row[1],
            'description': row[2],
            'creator': row[3],
            'money': row[4],
            'date': str(row[5])
            }
            response.append(obj)
        self.response.out.write(json.dumps(response))

    def post(self):
        sqlConn = ProjectConnector()
        p = Project(str(self.request.get("name")), str(self.request.get("desc")) + "'", str(self.request.get(
            "creatorId")))
        sqlConn.insert_into(p)


app = webapp2.WSGIApplication([('/', Projects)])