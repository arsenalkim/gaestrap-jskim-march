import os

import webapp2
import jinja2
import dicts

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class MyAppHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Homepage(MyAppHandler):
    def get(self):
        self.render('index.html')

class Match(MyAppHandler):
    def get(self):
        self.render("match.html")

class Players(MyAppHandler):
    def get(self):
        self.render("players.html")

class Schedule(MyAppHandler):
    def get(self):
        self.render("about.html")


app = webapp2.WSGIApplication([('/', Homepage),                              
								('/match', Match),
								('/players', Players),
								('/schedule', Schedule),
                               ],
                              debug=True)
