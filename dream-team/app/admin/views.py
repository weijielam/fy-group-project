# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from flask_mail import Mail, Message


from . import admin
from forms import EventForm
from .. import db
from app import mail
from ..models import Event, GuestList, User

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

# Event Views

@admin.route('/events', methods=['GET', 'POST'])
@login_required
def list_events():
    """
    List all events
    """
    check_admin()

    events = Event.query.all()

    return render_template('admin/events/events.html',
                           events=events, title="Events")

@admin.route('/events/add', methods=['GET', 'POST'])
@login_required
def add_event():
    """
    Add an event to the database
    """
    check_admin()

    add_event = True

    form = EventForm()
    if form.validate_on_submit():
        event = Event(name=form.name.data, timeD = form.timeD.data, location = form.location.data,
                                description=form.description.data)
        try:
            # add event to the database
            db.session.add(event)
            db.session.commit()
            flash('You have successfully added a new event.')
        except:
            # in case event name already exists
            flash('Error: event name already exists.')

        # redirect to events page
        return redirect(url_for('admin.list_events'))

    # load event template
    return render_template('admin/events/event.html', action="Add",
                           add_event=add_event, form=form,
                           title="Add Event")

@admin.route('/events/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_event(id):
    """
    Edit an event
    """
    check_admin()

    add_event = False

    event = Event.query.get_or_404(id)
    form = EventForm(obj=event)
    if form.validate_on_submit():
        event.name = form.name.data
        event.timeD = form.timeD.data
        event.location = form.location.data
        event.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the event.')

        # redirect to the events page
        return redirect(url_for('admin.list_events'))

    form.description.data = event.description
    form.name.data = event.name
    form.timeD.data = event.timeD
    form.location.data = event.location
    return render_template('admin/events/event.html', action="Edit",
                           add_event=add_event, form=form,
                           event=event, title="Edit Event")

@admin.route('/events/invitelist/<int:id>', methods=['GET', 'POST'])
@login_required
def invite_event(id):
    """
    Edit an event
    """
    check_admin()

    users = User.query.all()

    
    return render_template('admin/events/invitelist.html', action="Invite",                      
                           users=users, title="Invite List")

@admin.route('/events/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_event(id):
    """
    Delete am event from the databasew
    """
    check_admin()

    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    flash('You have successfully deleted the event.')

    # redirect to the events page
    return redirect(url_for('admin.list_events'))

    return render_template(title="Delete Event")


@admin.route('/mailinglist', methods=['GET', 'POST'])
@login_required
def mailinglist():
    """
    List all events
    """
    check_admin()

    events = Event.query.all()
    users = User.query.all()

    return render_template('admin/mailinglist/mailinglist.html',
                           users=users, title="mailinglist")



@admin.route('/mailinglist/send', methods=['GET', 'POST'])
@login_required
def send_email():
    users = User.query.all()
    with mail.connect() as conn:
        for user in users:
            message = '...'
            subject = "hello, %s" % user.username
            msg = Message(recipients=[user.email],
                            sender="weijielam@gmail.com",
                          body=message,
                          subject=subject)

            conn.send(msg)

        return "Sent"

@admin.route('/events/guestlist/<int:id>', methods=['GET', 'POST'])
@login_required
def event_guestlist(id):
    """
    View the guest list for an event
    """
    check_admin()
    guests = []
    add_event = False

    guestList = GuestList.query.filter_by(event_id=id).all()
    for guest in guestList:
        guests.append(User.query.get_or_404(guest.guest_id))

    return render_template('admin/events/guestList.html', action="View",
                           guests=guests, title="Guest List")

