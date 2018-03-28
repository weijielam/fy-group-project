# Documentation for feature list
0. Login in as Admin
	1. If login, logout at top right hand corner
	2. Click login in the top right hand corner
	3. Enter Email as admin@admin.com
	4. Enter password as admin2018


1. I want to be able to login (change password/create account)

	Create Account:
	
	1. If login, logout at top right hand corner
	2. Click 'Register' from top right hand corner
	3. Enter in credentials in the fields
	4. Click 'Register' at bottom of page

	Change password:
	
	1. Click the "Forgot your password?" button on the login screen.
	2. Enter the email associated with your account. 
	3. Click send email. 
	4. You should then head over to your email to receive a unique password reset url.
	5. Copy and paste this url into your browser and it'll redirect you to the password reset form. 
	6. Enter the new password twice and click reset password. 
	7. Proceed to login with your new password! 

	1a. If you want to change password while logged in
	2a. Nagivate to 'Hi, [user name]' tab on top right corner
	3a. In the change password field enter in your new password and confirm it

2. I want to be able to give admin access to other people
	
	- **REQUIRES ADMIN ACCESS** 
	
	1. Login into your admin account
	2. Navigate to the 'users' tab
	3. Enter the email of the user you wish to grant admin access to and then click grant access. 
	4. The Is Admin? section beside the user should change from true to false. 

4. I would like to be able to create an event

	1. Login in as admin user: admin@admin.com
			     pass: admin2018
	2. Click on the event tab located at the top of the dashboard
	3. Click 'add event' button, and enter the details of the event.
	4. Click submit.

5. I would like to be able to update event information and submit event updates
	
	1. Login in as admin user: admin@admin.com
			     pass: admin2018
	2. Click on the event tab located at the top of the dashboard
	3. Select 'edit' under the 'edit details' column on whichever event you want to edit
	4. edit event and click submit.

6. Keep track of possible/previous guests
	
	1. Login in as admin user: admin@admin.com
			     pass: admin2018
	2. Click on the 'user' tab at the top right of the dashboard
	3. User page will display all registered users with all their information
	4. Click on 'view' under the 'Event History' column to see what events a user has
	   attended and is RSVPed to attend.

8. I want to sent invitations to a mailing list, so that people know to come and that they are invited
	
	REQUIREMENTS:
	- Admin user created
	- User account(s) created
	- Event to be created (**Follow 4. to create an event**)

	1. Login in as admin user: admin@admin.com pass: admin2018
	2. Click on the event tab located at the top of the dashboard
	3. Click on an 'view' under the 'View Event' column for the event you wish to invite people to.
	4. Click on the 'Invite' button under the Invite List column of the event
	5. Select the checkboxes of the guests you wish to invite or select all guests using the 'Select all' box.
	6. Click the 'invite selected' button at the bottom
	7. Each invited guest should get an automated message sent to their email address with a link to the event page
	8. Optional (send email to all users in Guestlist): 
		- Once redirected to events page, click into 'view' for event you have invited people to. 
		- Click on the 'Send Email' button under the Email Guestlist
		- Fill in the subject and message fields for the subject and message you want to send your Mailing List
		- Click the Send button to send email.
	9. Users are then able to view the event and set their RSVP status.


10. I want to see the invite list

	1. Login in as admin user: admin@admin.com
			     pass: admin2018
	2. Click on the event tab located at the top of the dashboard
	3. Click on 'view' under the View Event column on desired event
	4. Click on 'view' under the Guest List Column

11. I want to see guest contact details
	
	1. Login in as admin user: admin@admin.com
			     pass: admin2018
	2. Click on the event tab located at the top of the dashboard
	3. Click on 'view' under the View Event column on desired event
	4. Click on 'view' under the RSVP List column 

12. I need to be able to manage the responses so I can know who is attending
	
	1. Login in as admin user: admin@admin.com
			     pass: admin2018
	2. Click on te events tab at top of page
	3. Click on 'view' under the View Event column on desired event
	4. Click on 'view' under the Guest List column
	5. Click the + button on each user you wish to add
	6. Click return to go back to the event page
	7. Click on 'view' under the RSVP list column
	8. Attendees can be removed from this page by clicking the x button on a given user

13. As staff, I need to register a guest for one event(including details) so I can track what is needed for the event(dietary, etc)
	
	- **Follow 1. to register a guest on their behalf**
	- **Follow 12. for adding a guest to an event on their behalf**
	
	1. Login in as admin user: admin@admin.com
			     pass: admin2018
	2. Click on the event tab located at the top of the dashboard
	3. Click on 'view' under the View Event column on desired event
	4. Click on 'view' under the RSVP column
	5. Click 'edit needs' under the edit special requirements column
	6. Enter in details and click submit

14. I want to be able to send automated invitations, with link to register for the event

	REQUIREMENTS:
	- Admin user created
	- **Follow 4. to create an event**
	- At least one user account to be created with a valid email address

	1. Login as admin user: admin@admin.com
					pass: admin2018
	2. Click on the event tab located at the top of the dashboard
	3. Click on an 'view' under the View Event column of the events
	4. Click on the 'Invite' button under the Invite List column of the event
	5. Select the checkboxes of the guests of the desired guests to be invited to the event
	6. Once all guests to be invited have been selected click the "Invite Selected" button to send invites
	7. Each invited guest should get an automated message sent to their email address with a link to the event page, user can then set their attendance from the event page


20. I would like to email (legitimately) subscribed users
	
	- **Must have users registered**
	
	1. Login in as admin user: admin@admin.com pass: admin2018
	2. Click on the "Mailing List" tab located at the top of the dashboard
	3. Fill in the subject and message fields for the subject and message you want to send your Mailing List
	4. Click the Send button to send email.

21. I want to be able to contact attendees easily eg. group email
	
	1. Login in as admin user: admin@admin.com pass: admin2018
	2. Click on the event tab located at the top of the dashboard
	3. Click on 'view' under the View Event column on desired event
	3. Click on the "Send Email" button under the Email Guestlist column
	4. Enter in the subject and message you want to send your the Guests in Event Guestlist
	5. Click the Send button to send email to all invited guests.

22. I want to be able to see the rsvp list
	
	1. Login in as admin user: admin@admin.com
			     pass: admin2018
	2. Click on the event tab located at the top of the dashboard
	3. Click on 'view' under the View Event column on desired event
	4. Click on 'view' under the RSVP Column

24. I want to be able to see a report of who is attending an event
	
	1. Login in as admin user: admin@admin.com
			     pass: admin2018
	2. Click on the event tab located at the top of the dashboard
	3. Click on 'view' under the View Event column on desired event
	4. Click on 'view' under the RSVP Column

28. I want to be able to add/remove attendees from the guest list
	
	1. Login in as admin user: admin@admin.com
			     pass: admin2018
	2. Click on events tab at top of page
	3. Click on 'view' under the View Event column on desired event
	4. Click on 'view' under the Guest List column
	5. Click the + button on each user you wish to add
	6. Click the x button on each user you wish to remove

29. I want to create menus
	
	1. Place the menu image in fygroupproject/menus folder
	2. When creating/editing an event, type in the name of the menu in the menu section eg. menu.jpg
	*For an example there is a menu in the menus folder called menu.jpg*

	Viewing a menu associated with an event

	1. Click on events tab at top of page

	2. Click on 'view' under the View Event column on desired event
	3. Click the 'view' button under Menus column 
	4. If there is a menu associated with the event it will open with the default image opener. 

49. I want to be able to see/accept payments
	1. Log in as a user 
	2. Click on the 'Donate' tab at the top
	3. Enter the amount to donate in euros and cents and 
	   the type of donation and purpose (ie is it for a specific event or just a general donation)
	4. Click submit and wait to be redirect to a payment page
	6. Enter in your email plus your credit card detais
	7. Click pay
	8. Admins can see all payments under the 'total raised' tab, See feature 54.


53. Have a tracker/ live count that updates with donations through an event
	1. Login as a User or an Admin
	2. Click on the event tab located at the top of the dashboard
	4. Click on 'Live Count' under the Live Count column on desired event

54. I want to track user amount raised
	1. Login as an admin
	2. Click on the 'Total Raised' tab at the top
	3. Page displays total raised plus payment breakdown


