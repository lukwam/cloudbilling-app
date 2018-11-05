"""Cloud Accounts App"""

import webapp2


class MainPage(webapp2.RequestHandler):
    """MainPage class."""

    def get(self):
        """Return the main page."""
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
