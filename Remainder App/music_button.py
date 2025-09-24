import pygame
import tkinter as tk

# Initialize pygame mixer
pygame.mixer.init()

# Load the music file
pygame.mixer.music.load("Relax Music.mp3")  # Replace with your music file

# Define the function to create the button
def create_music_button(root):
    # Toggle state for music
    is_playing = {"state": False}

    def toggle_music():
        if is_playing["state"]:
            pygame.mixer.music.stop()
            button.config(text="Play Music")
            is_playing["state"] = False
        else:
            pygame.mixer.music.play()
            button.config(text="Stop Music")
            is_playing["state"] = True

    # Create the button and position it at the bottom right
    button = tk.Button(root, text="Play Music", command=toggle_music, font=("Arial", 12), bg="blue", fg="white",width=20)
    button.place(relx=1.0, rely=1.0, anchor="se")  # Bottom-right corner
