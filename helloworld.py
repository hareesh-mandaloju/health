import webapp2
import os
import google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
