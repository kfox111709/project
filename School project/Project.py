import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("About Me")

name = "Kyle Fox"
age = 14
grade = 9
hobbies = ["Gaming", "coding", "Repairing broken electronics"]

favorite_color = "Lime green/Light blue"
favorite_game = "Minecraft"

skills = ["Python programming", "Fixing computers", "Troubleshooting computers"]

short_term_goal = "Improve my coding skills"
long_term_goal = "Become a Computer repair Technician"

fun_fact = "I have made a game on roblox,  I have also made multiple Discord bots using python. And one of my favorites is my discord bot that plays music from youtube into a discord voice channel"

info = f"""\
Name: {name}
Age: {age}
Grade: {grade}
Hobbies: {', '.join(hobbies)}
Favorite Color: {favorite_color}
Favorite Game: {favorite_game}
Skills: {', '.join(skills)}
Short-term Goal: {short_term_goal}
Long-term Goal: {long_term_goal}
Fun Fact: {fun_fact}
"""

label = tk.Label(root, text="", justify=tk.LEFT, padx=10, pady=10, font=("Minecraft"), wraplength=750)
label.pack()

caption_label = tk.Label(root, text="", font=("Minecraft"))
caption_label.pack(pady=10)

image_label = tk.Label(root)
image_label.pack()

def type_text(text, label):
    displayed_text = ""
    for i, char in enumerate(text):
        displayed_text += char
        label.config(text=displayed_text)
        label.update()
        root.after(50)
    root.after(500, show_caption)

def show_caption():
    caption_label.config(text="Here is a screenshot of 21 lines of my bots code:")
    root.after(2000, show_image)

def show_image():
    img = PhotoImage(file="image/image.png")
    image_label.config(image=img)
    image_label.image = img

def start_typing():
    start_button.config(state=tk.DISABLED)
    root.after(1000, type_text, info, label)

start_button = tk.Button(root, text="Start", command=start_typing, font=("Minecraft"))
start_button.pack(pady=10)

root.mainloop()