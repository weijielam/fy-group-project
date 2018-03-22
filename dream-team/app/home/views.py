# app/home/views.py

from flask import render_template
from flask_login import current_user, login_required

from . import home

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

# add admin dashboard view
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")

@home.route('/user/dashboard')
@login_required
def user_dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/user_dashboard.html', title="Dashboard")
