# app/user/views.py
from flask import abort, flash, redirect, render_template, url_for,request
from flask_login import current_user, login_required
from flask_mail import Mail, Message
from . import user
from forms import paymentForm
import datetime

from .. import db
from app import mail
from ..models import Event, GuestList, User, Payments
from PIL import Image 
import stripe
import os
stripe_keys = {
  'secret_key': os.environ['SECRET_KEY'],
  'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

##### view details of specific event#####
@user.route('/user/events/view/<int:id>', methods=['GET', 'POST'])
@login_required
def view_event(id):
    """
    view an event
    """

    event = Event.query.get_or_404(id)
   
    return render_template('user/viewevent.html', action="View",
                           id =id, event=event, title="View Event")


##### view list of all events #####
@user.route('/user/events', methods=['GET', 'POST'])
@login_required
def list_events():
    """
    List all events
    """

    events = Event.query.all()

    return render_template('user/events.html',
                           events=events, title="Events")


##### display menu for event #####
@user.route('/user/events/menus/<int:id>', methods=['GET', 'POST'])
@login_required
def event_menus(id):
    """
    View the menus for an event
    """

    event_id = Event.query.filter_by(id=id).all()
    menu_path = event_id[0].menus
    if menu_path != 'menus/':
        im = Image.open((menu_path))
        im.show()

    return render_template('user/menus.html', action="View",
                            id =id, title="Menu")

##### view guestlist for specific event #####
@user.route('/user/events/guestlist/<int:id>', methods=['GET', 'POST'])
@login_required
def event_guestlist(id):
    """
    View the guest list for an event
    """
    guests = []
    event = Event.query.get_or_404(id)

    guestList = GuestList.query.filter_by(event_id=id).all()
    for guest in guestList:
	if not guest.is_attending:	
	        guests.append(User.query.get_or_404(guest.guest_id))

    return render_template('user/guestList.html', action="View",
                           guests=guests, gl=guestList, id=id, title="Guest List")


##### view RSVP list for specific event #####
@user.route('/user/events/RSVPlist/<int:id>', methods=['GET', 'POST'])
@login_required
def event_RSVPlist(id):
    """
    View the RSVP list for an event
    """
    guests = []
    add_event = False
    event = Event.query.get_or_404(id)


    guestList = GuestList.query.filter_by(event_id=id).all()
    for guest in guestList:
        if guest.is_attending == True:
            guests.append(User.query.get_or_404(guest.guest_id))

    return render_template('user/RSVPList.html', action="View",
                           guests=guests, gl=guestList, id=id, title="Guest List")


##### View event Live Counter ####

@user.route('/user/events/livecount/<int:id>', methods=['GET', 'POST'])
@login_required
def event_livecount(id):
    """
    view event Live Count
    """

    add_event = False
    event = Event.query.get_or_404(id)
   
    return render_template('user/livecount.html', action="View",
                           id =id, event=event, title="Live Count")

@user.route('/user/payment', methods=['GET', 'POST'])
@login_required
def payment():

    all_events = Event.query.all()
    event_drop_list = [(-1, 'General')]

    for e in all_events:
        event_drop_list.append((e.id, 'Event: ' + e.name))

    form = paymentForm()
    form.purpose.choices = event_drop_list 

    if form.validate_on_submit():
        print('we did it')
        dol_amt=int(form.dol_amount.data)
        cent_amt=int(form.cent_amount.data)
        pay_type=form.pay_type.data
        whole_amt=(dol_amt*100)+cent_amt
        purpose = form.purpose.data
        # flash('Please enter numerical amount.')
        return redirect(url_for('user.payment_redirect', amt=whole_amt, pay_type=pay_type, purpose=purpose))

    return render_template('payment/payment.html', form=form)


@user.route('/user/payment_redirect/<int:amt>/<string:pay_type>/<string:purpose>', methods=['GET', 'POST'])
@login_required
def payment_redirect(amt, pay_type, purpose):

    return render_template('payment/payment_redirect.html', key=stripe_keys['publishable_key'], 
        amt=amt, pay_type=pay_type, purpose=purpose)


@user.route('/user/charge/<int:amt>/<string:pay_type>/<string:purpose>', methods=['GET', 'POST'])
@login_required
def charge(amt, pay_type, purpose):

    now = datetime.datetime.now()
    payment = Payments(amount=amt, user_id=current_user.id, payment_type=pay_type, purpose=purpose, date= now.strftime("%d-%m-%Y"))
    db.session.add(payment)
    db.session.commit()

    customer = stripe.Customer.create(
        email='customer@example.com',
        source=request.args.get('stripeToken')
        # source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amt,
        currency='usd',
        description='Dream team Charge'
    )

    user_name = current_user.first_name + ' ' + current_user.last_name

    return render_template('payment/charge.html', amount=amt/100, cents=amt%100, pay_type=pay_type, purpose=purpose, user_name=user_name)


















