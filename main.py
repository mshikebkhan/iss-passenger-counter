import requests
from tkinter import *

API = "http://api.open-notify.org/astros.json"

# ---- GET DATA ---- #
def get_data():
    api_data = requests.get(url=API).json()
    return api_data["number"]

# ---- UPDATE UI ---- #
def update_passengers_num():
    passengers_num = get_data()
    heading.config(text=f"ISS Passengers: {passengers_num}")

# ---- UI SETUP ---- #
window = Tk()
window.title("ISS Passengers")
window.iconbitmap("astronaut.ico")
window.config(padx=50, pady=30)

# Heading
heading = Label(text="ISS Passengers", font=("Ariel", 28, "bold"))
heading.grid(column=0, row=0)

# Canvas
canvas = Canvas(width=300, height=300)
iss_img = PhotoImage(file="iss.png")
canvas.create_image(150, 150, image=iss_img)
canvas.grid(column=0, row=1)


# Buttons
calculate_btn = Button(text="Calculate", command=update_passengers_num)
calculate_btn.grid(column=0, row=2)

window.mainloop()
