import datetime
import webapp2
import json
import SQLConnector


class Projects(webapp2.RequestHandler):

    def get(self):
        sqlConn = SQLConnector()
        name = str(self.request.get("name"))
        if name != "":
            rows = sqlConn.select_all_where("projects", "name = '%s'" % name)
        else:
            rows = sqlConn.select_all_from("projects")
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
        sqlConn = SQLConnector()
        name = "'" + str(self.request.get("name")) + "'"
        desc = "'" + str(self.request.get("desc")) + "'"
        creator = str(self.request.get("creatorId"))
        today = "'" + datetime.datetime.now().strftime('%Y-%m-%d') + "'"
        sqlConn.insert_into("projects", {"name": name, "description": desc, "creator": creator, "createdOn": today})

