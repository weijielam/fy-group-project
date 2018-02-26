# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for,request
from flask_login import current_user, login_required
from flask_mail import Mail, Message
from . import admin
from forms import EventForm, GuestListForm
from email import EmailForm
from forms import EventForm, AdminAccessForm

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

    not_invited = []
    already_invd = False

    users = User.query.all()
    guests = GuestList.query.filter_by(event_id=id).all()

    for user in users:
        already_invd = False
        for guest in guests:
            if user.id == guest.guest_id:
                already_invd = True
        if not already_invd:
            not_invited.append(user)

    
    return render_template('admin/events/invitelist.html', action="Invite",                      
                           users=not_invited, eid=id, title="Invite List")

@admin.route('/events/needs/<int:eid>/<int:uid>', methods=['GET', 'POST'])
@login_required
def needs_event(eid, uid):
    """
    Needs for a user
    """
    check_admin()
    add_event = False

    
    form = GuestListForm()
    user = User.query.get_or_404(uid)
    form = GuestListForm(obj=user)
    if form.validate_on_submit():
       
        user.needs = form.needs.data
        db.session.commit()
        flash('You have successfully edited a users needs.')

        # redirect to the events page
        return redirect(url_for('admin.event_guestlist', id=eid))

    user.needs = form.needs.data 
    return render_template('admin/events/userneeds.html', action="Needs",                      
                           id =eid, user=user, form=form, title="needs")

@admin.route('/events/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_event(id):
    """
    Delete am event from the databasew
    """
    check_admin()

    event = Event.query.get_or_404(id)
    guests = GuestList.query.filter_by(event_id=event.id).all()

    for guest in guests:
        if guest.event_id == event.id:
            db.session.delete(guest)
            db.session.commit()

    db.session.delete(event)
    db.session.commit()
    flash('You have successfully deleted the event.')

    # redirect to the events page
    return redirect(url_for('admin.list_events'))

    return render_template(title="Delete Event")

# Mailing List
# Display Mailing List Page
@admin.route('/mailinglist', methods=['GET', 'POST'])
@login_required
def mailinglist():

    check_admin()
    users = User.query.all()

    form = EmailForm()
    if form.validate_on_submit():
        subject = form.subject.data 
        body    = form.body.data
        try:
            flash('Email sent to mailing list')
            # send email
            mailinglist_email(subject, body)
            
            return redirect(url_for('admin.mailinglist'))
        except:
            # in case email fails
            flash('ERROR')

        # redirect to events page
    return render_template('admin/mailinglist/mailinglist.html',
                           form = form, users=users, title="mailinglist")

# send email to all users in mailing list
@admin.route('/mailinglist/send', methods=['GET', 'POST'])
@login_required
def mailinglist_email(subject, body):
    users = User.query.all()
    with mail.connect() as conn:
        for user in users:
            msg = Message(recipients=[user.email], sender="fygptest@gmail.com",
                          body=body, subject=subject)
            
            conn.send(msg)

        return "Sent"

# Send mass email to users with message
@login_required
def send_email_to_users(users, message, subject):
    with mail.connect() as conn:
        for user in users:
            message = message
            subject = subject
            msg = Message(recipients=[user.email], sender="fygptest@gmail.com",
                            body = message, subject = subject)
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
    event = Event.query.get_or_404(id)


    guestList = GuestList.query.filter_by(event_id=id).all()
    for guest in guestList:
        guests.append(User.query.get_or_404(guest.guest_id))
   


    return render_template('admin/events/guestList.html', action="View",
                           guests=guests, event=event, id=id, title="Guest List")



@admin.route('/events/removeguest/<int:eid>/<int:gid>', methods=['GET', 'POST'])
@login_required
def remove_guest(eid, gid):
    """
    Remove a guest from an event
    """
    check_admin()

    guestList = GuestList.query.filter_by(event_id=eid).all()
    for guest in guestList:
        print("guest.guest_id: " + str(guest.guest_id))
        print("gid: " + str(gid))
        if guest.guest_id == gid:
            db.session.delete(guest)
            db.session.commit()
            
    flash('You have successfully removed a user from the event.')

    # redirect to the events page
    return redirect(url_for('admin.event_guestlist', id=eid))

    return render_template(title="Removed Guest")


@admin.route('/events/addguest/<int:eid>/<int:gid>', methods=['GET', 'POST'])
@login_required
def add_guest(eid, gid):
    """
    Add a guest to an event
    """
    check_admin()

    guest = GuestList(guest_id=gid, event_id=eid, is_attending=1)

    db.session.add(guest)
    db.session.commit()
            
    flash('You have successfully added a user to the event.')

    # redirect to the events page
    return redirect(url_for('admin.invite_event', id=eid))
    return render_template(title="Added Guest")


@admin.route('/userlist', methods=['GET', 'POST'])
@login_required
def userlist():
    """
    List all events
    """
    
    check_admin()

    form = AdminAccessForm()
    if form.validate_on_submit():
        email_of_user= form.email.data
        print("The email you entered", email_of_user)
        user = User.query.filter_by(email=email_of_user).all()
        user[0].is_admin=1
        db.session.commit()

    events = Event.query.all()
    users = User.query.all()

    


    return render_template('admin/userlist/userlist.html',
                           users=users, title="User List", form=form)    
