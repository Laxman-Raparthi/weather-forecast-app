#Using command line do "pip install requests pillow"
#Internet connection is required for the program to run
#The maximum capacity is 60 runs/min so try staying below it

from tkinter import *
import tkinter.font as font
import requests
import json
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO

root = Tk()
root.title("Weather Conditions")

myfont = font.Font(family='Helvetica', size=20, weight='bold')
myfontbig = font.Font(family='Helvetica', size=60, weight='bold')
myfontsmall = font.Font(family='Helvetica', size=15)

frame = LabelFrame(root)
frame.pack(padx=10, pady=10)

api_key = "3e048c850e7bcecc34437519ce82156a"
base_url = "https://api.openweathermap.org/data/2.5/weather?"

def submit():
    city = entry.get().strip()
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    complete_url = base_url + "appid=" + api_key + "&q=" + city

    try:
        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return

        cityog = x['name']
        country = x['sys']['country']
        current_temp = round(x['main']['temp'] - 273.15, 1)
        feels_like = round(x['main']['feels_like'] - 273.15, 1)
        weather = x['weather'][0]['main']
        min_temp = round(x['main']['temp_min'] - 273.15, 1)
        max_temp = round(x['main']['temp_max'] - 273.15, 1)
        humidity = x['main']['humidity']
        wind_speed = x['wind']['speed']
        icon_code = x['weather'][0]['icon']

        # Fetch Weather Icon
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        icon_data = icon_response.content
        icon_image = Image.open(BytesIO(icon_data))
        icon_photo = ImageTk.PhotoImage(icon_image)

        top = Toplevel()
        top.title(f"Weather in {cityog}")

        frame2 = LabelFrame(top)
        frame2.pack(padx=10, pady=10)

        label1 = Label(frame2, text=cityog + ", " + country)
        label1['font'] = myfont
        label1.grid(column=0, row=0, pady=5)

        label2 = Label(frame2, text=str(current_temp) + " °C")
        label2['font'] = myfontbig
        label2.grid(column=0, row=1, pady=5)

        frame3 = LabelFrame(frame2)
        frame3.grid(column=0, row=2, pady=10)

        # Show weather icon
        icon_label = Label(frame3, image=icon_photo)
        icon_label.image = icon_photo  # prevent garbage collection
        icon_label.grid(column=0, row=0, pady=2)

        label4 = Label(frame3, text=weather)
        label4['font'] = myfont
        label4.grid(column=0, row=1, pady=2)

        label3 = Label(frame3, text="Feels like: " + str(feels_like) + " °C")
        label3['font'] = myfontsmall
        label3.grid(column=0, row=2, pady=2)

        label5 = Label(frame3, text="Min/Max temp: " + str(min_temp) + "°/" + str(max_temp) + "°")
        label5['font'] = myfontsmall
        label5.grid(column=0, row=3, pady=2)

        label6 = Label(frame3, text="Humidity: " + str(humidity) + "%")
        label6['font'] = myfontsmall
        label6.grid(column=0, row=4, pady=2)

        label7 = Label(frame3, text="Wind Speed: " + str(wind_speed) + " m/s")
        label7['font'] = myfontsmall
        label7.grid(column=0, row=5, pady=2)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Connection Error", "Failed to connect to the server.\nPlease check your internet connection.")

Label(frame, text="Enter City Name:", font=myfont).grid(column=0, row=0, padx=10, pady=10)
entry = Entry(frame)
entry['font'] = myfont
entry.grid(column=0, row=1, padx=10, pady=10, ipadx=50, ipady=5)

button = Button(frame, text="Submit", command=submit)
button['font'] = myfont
button.grid(column=0, row=2, ipadx=20, pady=10)

root.mainloop()
