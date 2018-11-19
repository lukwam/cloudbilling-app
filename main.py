"""Cloud Accounts main app."""

# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime

from flask import Flask, render_template
from google.cloud import datastore

datastore_client = datastore.Client()

app = Flask(__name__)


def render_theme(body):
    """Render the main template header and fooder."""
    return render_template(
        'theme.html',
        body=body,
        # is_admin=users.is_current_user_admin(),
        # is_dev=is_dev(),
        # logout_url=users.create_logout_url('/'),
        # request=request,
    )


@app.route('/')
def main_page():
    """Return the main page."""
    body = render_template(
        'index.html',
        # times=times
    )
    return render_theme(body)


@app.route('/accounts')
def accounts_page():
    """Return the accounts page."""
    body = render_template(
        'accounts.html',
    )
    return render_theme(body)


@app.route('/admin')
def admin_page():
    """Return the admin page."""
    body = render_template(
        'admin.html',
    )
    return render_theme(body)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
