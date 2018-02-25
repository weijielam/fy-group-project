# app/admin/email.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import DepartmentForm
from .. import db
from ..models import Department

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

# Department Views

@admin.route('/mailinglist/send', methods=['GET', 'POST'])
@login_required
def send_email(id):
   users = ['weijielam@gmail.com, teefyl@tcd.ie, berryp@tcd.ie']
   with mail.connect() as conn:
    for user in users:
        message = '...'
        subject = "hello, %s" % user.name
        msg = Message(recipients=[user.email],
                      body=message,
                      subject=subject)

        conn.send(msg)

    return "Sent"   
