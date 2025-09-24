from tkinter import *
from tkinter import messagebox, simpledialog
from plyer import notification
from datetime import datetime
from threading import Thread
import json
import time
from PIL import Image, ImageTk

class ReminderApp:
    def __init__(self, root):
        
        """
        
        Initialize the Reminder Application
       
         Args:
            root: The main window (Tk instance)
        """
        self.root = root
        self.root.title("Reminder App")
        self.root.geometry("600x500")           # Set window size

        self.reminders_file = "reminders.json"  # Using  json to store data records.
        self.reminders = []
        self.load_reminders()                  # Load existing reminders when app starts

        # UI Setup
        self.setup_ui()

        # Start reminder checking in a separate thread
        self.reminder_thread = Thread(target=self.check_reminders, daemon=True)
        self.reminder_thread.start()

    def setup_ui(self):
        # Default image handling
        try:
            from PIL import Image, ImageTk
            img = Image.open("bell.ico")
            tkimage = ImageTk.PhotoImage(img)
            Label(self.root, image=tkimage).pack()
            self.root.tkimage = tkimage  # To prevent garbage collection of the image
        except (FileNotFoundError, ImportError):
            Label(self.root, text="Reminder Application", font=("Arial", 16)).pack(pady=20)

        Button(self.root, text="Add Reminder", font=("Arial", 12), bg="#528DFF", fg="white", 
               width=20, command=self.add_reminder).pack(pady=10)
        Button(self.root, text="View Reminders", font=("Arial", 12), bg="green", fg="white", 
               width=20, command=self.view_reminders).pack(pady=10)
        Button(self.root, text="Exit", font=("Arial", 12), bg="red", fg="white", 
               width=20, command= self.exit_app).pack(pady=10)


    def exit_app(self):    # Handle application exit with a goodbye message
        exit_app = messagebox.showinfo("EXIT",f"Thank You for using our app!!")
        self.root.destroy()



    def load_reminders(self):  # Load saved reminders from JSON file and convert string dates to datetime objects
        try:
            with open(self.reminders_file, "r") as f:
                self.reminders = json.load(f)
                for r in self.reminders:
                    r["reminder_time"] = datetime.strptime(r["reminder_time"], "%d-%m-%Y %H:%M")
        except FileNotFoundError:
            self.reminders = []

    def save_reminders(self):   # Save reminders to JSON file, converting datetime objects to strings
        reminders_copy = [
            {
                "task_name": r["task_name"],
                "task_msg": r["task_msg"],
                "reminder_time": r["reminder_time"].strftime("%d-%m-%Y %H:%M"),
                "is_recurring": r["is_recurring"]
            }
            for r in self.reminders
        ]
        with open(self.reminders_file, "w") as f:
            json.dump(reminders_copy, f)

    def add_reminder(self):       #Create a new window for adding reminders
        def save_new_reminder():  #Inner function to save the new reminder data
            task_name = title_entry.get()
            task_msg = msg_entry.get()
            date_str = date_entry.get()
            time_str = time_entry.get()

            if not task_name or not task_msg or not date_str or not time_str:  # if empty data show error inform.
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                reminder_datetime = datetime.strptime(f"{date_str} {time_str}", "%d-%m-%Y %H:%M")       # Convert input strings to datetime
                if reminder_datetime <= datetime.now():                                                 # Check  is it the date is passed?
                    messagebox.showerror("Error", "The selected date and time must be in the future.")  # If wrong date show error message.
                    return
                
                # Add new reminder to the list
                self.reminders.append({
                    "task_name": task_name,
                    "task_msg": task_msg,
                    "reminder_time": reminder_datetime,
                    "is_recurring": False
                })
                self.save_reminders()
                messagebox.showinfo("Success", "Reminder added successfully!")  #Every format is correct then save it and display notify.
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid date or time format. Please use DD-MM-YYYY and HH:MM.") # If typing wrong show error.

# New window for Add Reminder -----------------------------------------------------------------------
        
        add_window = Toplevel(self.root)
        add_window.title("Add Reminder")
        add_window.geometry("400x300")


#Label and Button in Add Reminder inside ------------------------------------------------------------------------------

        Label(add_window, text="Title:", font=("Arial", 12)).pack(pady=5)
        title_entry = Entry(add_window, width=40)
        title_entry.pack()

        Label(add_window, text="Message:", font=("Arial", 12)).pack(pady=5)
        msg_entry = Entry(add_window, width=40)
        msg_entry.pack()

        Label(add_window, text="Date (DD-MM-YYYY):", font=("Arial", 12)).pack(pady=5)
        date_entry = Entry(add_window, width=20)
        date_entry.pack()

        Label(add_window, text="Time (HH:MM):", font=("Arial", 12)).pack(pady=5)
        time_entry = Entry(add_window, width=10)
        time_entry.pack()

        Button(add_window, text="Save Reminder", font=("Arial", 12), bg="#528DFF", fg="white", 
               command=save_new_reminder).pack(pady=20)
 
    def view_reminders(self):       # Display all reminders and provide edit/delete functionality
        def edit_reminder(index):    #  Handle editing of existing reminders
            reminder = self.reminders[index]
            new_task_name = simpledialog.askstring("Edit Reminder", "Enter new task name:", initialvalue=reminder["task_name"]) #Display new simpledialog to edit task name.
            new_task_msg = simpledialog.askstring("Edit Reminder", "Enter new message:", initialvalue=reminder["task_msg"])     #Display new simpledialog to edit new message.
            new_date = simpledialog.askstring("Edit Reminder", "Enter new date (DD-MM-YYYY):",                                  #Display new simpledialog to edit new date.
                                              initialvalue=reminder["reminder_time"].strftime("%d-%m-%Y"))                      # Follow the format 2-digit day - 2-digit month -  4-digit year .
            new_time = simpledialog.askstring("Edit Reminder", "Enter new time (HH:MM):", 
                                              initialvalue=reminder["reminder_time"].strftime("%H:%M"))          # Follow the format %H: Hour (24-hour clock) as a zero-padded decimal number (e.g., 08 for 8:00 a.m.) %M: Minute as a zero-padded decimal number (e.g., 30)

            if new_task_name and new_task_msg and new_date and new_time:
                try:
                    reminder_time = datetime.strptime(f"{new_date} {new_time}", "%d-%m-%Y %H:%M")       # Validate and update reminder
                    if reminder_time <= datetime.now():
                        messagebox.showerror("Error", "The selected date and time must be in the future.")
                        return

                    reminder["task_name"] = new_task_name
                    reminder["task_msg"] = new_task_msg
                    reminder["reminder_time"] = reminder_time
                    self.save_reminders()
                    messagebox.showinfo("Reminder Edited", "The reminder has been successfully updated.")
                    view_window.destroy()
                    self.view_reminders()  # Refresh the view
                except ValueError:
                    messagebox.showerror("Invalid Time", "The date or time format is invalid. Please use DD-MM-YYYY and HH:MM.")

        def delete_reminder(index):
            self.reminders.pop(index)
            self.save_reminders()
            messagebox.showinfo("Reminder Deleted", "The reminder has been successfully deleted.")
            view_window.destroy()
            self.view_reminders()    # Refresh the view

        # Create window to display reminders
        view_window = Toplevel(self.root)
        view_window.title("View Reminders")
        view_window.geometry("500x400")

        # Show message if no reminders exist
        if not self.reminders:
            Label(view_window, text="No reminders found!", font=("Arial", 14)).pack(pady=20)
            return

        # Display all reminders with edit and delete buttons
        for idx, reminder in enumerate(self.reminders):
            reminder_text = (
                f"Task: {reminder['task_name']}\n"
                f"Message: {reminder['task_msg']}\n"
                f"Time: {reminder['reminder_time'].strftime('%d-%m-%Y %H:%M')}\n"
            )
            Label(view_window, text=reminder_text, justify=LEFT, font=("Arial", 12)).pack(anchor="w", pady=5)

            Button(view_window, text="Edit", bg="#528DFF", fg="white", 
                   command=lambda i=idx: edit_reminder(i)).pack(anchor="w")
            Button(view_window, text="Delete", bg="red", fg="white", 
                   command=lambda i=idx: delete_reminder(i)).pack(anchor="w")

    def check_reminders(self):
        while True:
            now = datetime.now()
            # Check each reminder
            for reminder in self.reminders[:]:        # Use slice copy to safely modify list while iterating
                if reminder["reminder_time"] <= now:  # Show notification for due reminders
                    notification.notify(
                        title=reminder["task_name"],
                        message=reminder["task_msg"],
                        app_icon="bell.ico",  
                        timeout=10
                    )
                    self.reminders.remove(reminder) # Remove the reminder after it's shown
                    self.save_reminders()
            time.sleep(1)                           # Check every second

# Main entry point
if __name__ == "__main__":
    root = Tk()
    app = ReminderApp(root)
    root.mainloop()
pass