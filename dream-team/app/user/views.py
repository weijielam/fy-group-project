# app/user/views.py
from flask import abort, flash, redirect, render_template, url_for,request
from flask_login import current_user, login_required
from flask_mail import Mail, Message
from . import user

from .. import db
from app import mail
from ..models import Event, GuestList, User
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

@user.route('/payment')
def index():
    return render_template('payment/index.html', key=stripe_keys['publishable_key'])

@user.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    amount = 500

    customer = stripe.Customer.create(
        email='customer@example.com',
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('payment/charge.html', amount=amount)


















