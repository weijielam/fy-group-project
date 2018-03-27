# app/home/views.py

from flask import render_template
from flask_login import current_user, login_required
from ..models import Event, GuestList, User, Payments

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

    cash = 0
    cents = 0

    payments = Payments.query.all()
    new_payments = []

    for p in payments:
        cash = cash + (p.amount/100)
        cents = cents + (p.amount%100)
        user = User.query.get_or_404(p.user_id)
        name = user.first_name + ' ' + user.last_name
        if p.amount%100 < 10:
            amt_str = str(p.amount/100) + '.0' + str(p.amount%100)
        else:
            amt_str = str(p.amount/100) + '.' + str(p.amount%100)

        if p.purpose == '-1':
            new_payments.append([name, p.date, p.payment_type, 'General', amt_str])
        else:
            new_payments.append([name, p.date, p.payment_type, Event.query.get_or_404(int(p.purpose)).name, amt_str])

    cash = cash + cents/100
    cents = cents%100

    return render_template('home/admin_dashboard.html', title="Dashboard", cash=cash, cents=cents, payments=new_payments)

@home.route('/user/dashboard')
@login_required
def user_dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/user_dashboard.html', title="Dashboard")
