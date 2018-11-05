"""Cloud Accounts App main."""

import jinja2
import os
import webapp2

# import google libraries
from google.appengine.api import users
# from googleapiclient.errors import HttpError


# establish the jinja2 environment
jinja = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True,
)


def is_dev():
    """Return true if this is the development environment."""
    dev = False
    if os.environ['SERVER_SOFTWARE'].startswith('Development'):
        dev = True
    return dev


def render_theme(body, request):
    """Render the main template header and footer."""
    template = jinja.get_template('theme.html')
    return template.render(
        body=body,
        is_admin=users.is_current_user_admin(),
        is_dev=is_dev(),
        request=request,
    )


class AccountsPage(webapp2.RequestHandler):
    """AccountsPage class."""

    def get(self):
        """Return the accounts page."""
        template = jinja.get_template('accounts.html')
        body = template.render()
        output = render_theme(body, self.request)
        self.response.write(output)


class AdminPage(webapp2.RequestHandler):
    """AdminPage class."""

    def get(self):
        """Return the admin page."""
        template = jinja.get_template('admin.html')
        body = template.render()
        output = render_theme(body, self.request)
        self.response.write(output)


class MainPage(webapp2.RequestHandler):
    """MainPage class."""

    def get(self):
        """Return the admin page."""
        template = jinja.get_template('index.html')
        body = template.render()
        output = render_theme(body, self.request)
        self.response.write(output)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/accounts', AccountsPage),
    ('/admin', AdminPage),
], debug=True)
