Reminder App

A simple desktop application built with Python and Tkinter that helps users manage their reminders and notifications.
Features

Create reminders with custom titles and messages
Set date and time for notifications
Edit existing reminders
Delete reminders
Desktop notifications when reminders are due
Persistent storage of reminders using JSON
User-friendly graphical interface

Installation
Prerequisites

Python 3.x
pip (Python package installer)

Required Libraries
Install the following Python libraries using pip:

pip install plyer
pip install Pillow

Setup

Clone or download the repository to your local machine
Place a bell icon file named bell.ico in the same directory as the script (or the app will run with text header instead)
Run the application using Python

python reminder_app.py

Usage Guide
Adding a Reminder

Click the "Add Reminder" button
Fill in the required fields:

Title: Name or subject of your reminder
Message: Details or description of the reminder
Date: Enter in DD-MM-YYYY format (e.g., 25-12-2024)
Time: Enter in HH:MM 24-hour format (e.g., 14:30 for 2:30 PM)


Click "Save Reminder" to create the reminder

Viewing Reminders

Click the "View Reminders" button to see all active reminders
Each reminder displays:

Task name
Message
Scheduled date and time



Editing Reminders

In the View Reminders window, click "Edit" next to the reminder you want to modify
Update any of the following:

Task name
Message
Date (DD-MM-YYYY)
Time (HH:MM)


Confirm changes in each dialog box

Deleting Reminders

In the View Reminders window, click "Delete" next to the reminder you want to remove
Confirm the deletion when prompted

Notifications

When a reminder becomes due, a desktop notification will appear
Notifications include:

Reminder title
Message
Icon (if bell.ico is present)


Notifications will appear even if the app is running in the background

Important Notes

All times should be entered in 24-hour format
Dates must be in DD-MM-YYYY format
You cannot set reminders for past dates or times
Reminders are automatically deleted after they are triggered
The app must be running (can be minimized) for notifications to work
All reminders are saved automatically and will persist between app restarts

Troubleshooting

If you don't see the bell icon, ensure bell.ico is in the same directory as the script
If notifications don't appear, check your system's notification settings
If you get a date/time error, ensure you're using the correct format (DD-MM-YYYY for dates, HH:MM for times)

Exiting the App

Click the "Exit" button to close the application
A confirmation message will appear before closing

Data Storage

Reminders are stored in a reminders.json file in the same directory as the script
This file is created automatically when you add your first reminder
Do not modify this file manually to avoid data corruption