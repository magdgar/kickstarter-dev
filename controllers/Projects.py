import datetime
import webapp2
from webapp2_extras import json
import json
import MySQLdb

      # name of the data base

class Projects(webapp2.RequestHandler):

    def get(self):
        db = MySQLdb.connect(host="173.194.246.10",    # your host, usually localhost
                     user="magdalena",         # your username
                     passwd="root",  # your password
                     db="kickstarter")
        cur = db.cursor()
        name = str(self.request.get("name"))
        # Use all the SQL you like
        if name != "":
            cur.execute("SELECT * FROM projects WHERE name = '%s'" % (name))
        else:
            cur.execute("SELECT * FROM projects")
        res = []
        obj = ""
        for row in cur.fetchall():
            obj = {
            'id': row[0],
            'name': row[1],
            'description': row[2],
            'creator': row[3],
            'money': row[4],
            'date': str(row[5])
            }
            res.append(obj)
        db.close()
        self.response.out.write(json.dumps(res))

    def post(self):
        db = MySQLdb.connect(host="173.194.246.10",    # your host, usually localhost
                     user="magdalena",         # your username
                     passwd="root",  # your password
                     db="kickstarter")
        cur = db.cursor()
        name = str(self.request.get("name"))
        desc = str(self.request.get("desc"))
        creator = str(self.request.get("creatorId"))

        cur.execute("INSERT INTO projects(name, description, creator, createdOn) VALUE (%s, %s, %s, %s)" % (name, desc, creator, datetime.datetime.now().time()))

        db.close()



