import tkinter as tk
import requests
from tkinter import font

vyska = 700
sirka = 800

def format_response(pocasi):
    try:
        name = pocasi["name"]
        desc = pocasi["weather"][0]["description"]
        temp = pocasi["main"]["temp"]

        vysledek = f"City: {name} \nConditions: {desc} \nTemperature (°C): {temp}"

    except:
        vysledek = "City not found"

    return vysledek

def get_weather(city):
    weather_key = "ae9b7ca3e56b0d0b0e49509670a313dc"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "metric"}
    response = requests.get(url, params=params)
    pocasi = response.json()

    popis["text"] = format_response(pocasi)

hlavni = tk.Tk()

canvas = tk.Canvas(hlavni, height=vyska, width=sirka)
canvas.pack()

pozadi_obrazek = tk.PhotoImage(file="landscape.png")
pozadi_popis = tk.Label(hlavni, image=pozadi_obrazek)
pozadi_popis.place(x=0,y=0,relwidth=1,relheight=1)

obraz_horni = tk.Frame(hlavni, bg="#ffcc66", bd=20)
obraz_horni.place(relx=0.1, rely=0.1,relheight=0.15, relwidth=0.8)

tlacitko = tk.Button(obraz_horni, font=("Courier", 20), text="Počasí", bg="#66ccff", command=lambda: get_weather(vstup.get()))
tlacitko.place(relx=0, rely=0, relwidth=0.20, relheight=1)

vstup = tk.Entry(obraz_horni, font=("Courier", 20))
#vstup.insert(0,"input here")
vstup.place(relx=0.23, rely=0, relwidth=0.75, relheight=1)

# - - -

obraz_dolni = tk.Frame(hlavni, bg="#ffcc66", bd=10)
obraz_dolni.place(relx=0.1,rely=0.28,relheight=1.00-0.28-0.10, relwidth=0.8)

popis = tk.Label(obraz_dolni, font=("Courier", 20), text="Try: 'Prague', 'Praha', '69420'", bg="#ffeecc")
popis.place(relx=0, rely=0, relwidth=1, relheight=1)

print(tk.font.families())

#34:18

hlavni.mainloop()
