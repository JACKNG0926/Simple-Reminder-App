from tkinter import Tk
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Reminder_app import ReminderApp
from PIL import Image, ImageTk
from PIL import Image
from music_button import create_music_button  # Import the music button function


def app2():
    # Open the Reminder App
    reminderapp_window = tk.Toplevel(root)
    ReminderApp(reminderapp_window)

def exit_app():
    messagebox.showinfo("Exit",f"Thank you for using GADGETHUB ")
    root.destroy()


# Create the main application window
root = tk.Tk()
root.title("GADGETHUB MENU")
root.geometry("1200x1000")

img = Image.open("GADGETHUB_LOGO.png")
tkimage = ImageTk.PhotoImage(img)
Label(root, image=tkimage).pack()

# Create the music button
create_music_button(root)



frame2 = tk.Frame(root,width=900, height=10)
frame2.pack()

framelogo = tk.Frame(root,width= 500, height= 70)
framelogo.pack()

frametitle = tk.Frame(root,width=900,height=50)
frametitle.pack()

# Add a title label
title_label = tk.Label(frametitle, text="WELCOME TO GADGETHUB !!", font=("Arial", 24), bg="blue")
title_label.pack()


welcome_label = tk.Label(frametitle, text="We will serve the best to our lovely user!!!", font=("Arial",14), fg= "black")
welcome_label.pack()

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=100)

# Load and resize image

image1 = Image.open("Pomodoro_Timer_logo.jpg").resize((80, 50))  # Replace with your image file
button_image1 = ImageTk.PhotoImage(image1)      

image2 = Image.open("simplebell.jpg").resize((100, 100))  
button_image2 = ImageTk.PhotoImage(image2)

image3 = Image.open("To_Do_List_logo.png").resize((100, 50))  
button_image3 = ImageTk.PhotoImage(image3)

image4 = Image.open("Calendar_logo.png").resize((100, 100))  
button_image4 = ImageTk.PhotoImage(image4)


button2 = tk.Button(button_frame, text="  REMINDER APP", bg="green", fg="white", command=app2,image = button_image2,compound="left", width=185, height=50 ) 
button2.grid(row=1, column=1, padx=10, pady=10)


exit_button = tk.Button(button_frame, text="Exit", bg="red",fg="white", command=exit_app, width=30, height=3)
exit_button.grid(row=3, column=1, padx=10, pady=10)

term_label = tk.Label(root, text = "     Term and Condition: By using this app, you are agree to our terms and conditions.")
term_label.pack()

cons_label = tk.Label(root, text = "    Copyright Reserved: © 2024 GADGETHUB. All right reserved.")
cons_label.pack()

# Run the main application loop
root.mainloop()
