import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        with open('frontend/index.html', 'r') as myfile:
            data=myfile.read()

        self.response.write(data)

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)