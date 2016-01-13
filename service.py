import json

import webapp2

class HelloWorld(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        name = self.request.get('name')
        obj = {
            'hello': name,
            'world': name,
          }
        self.response.out.write(json.dumps(obj))