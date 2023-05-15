#import libraries
import requests
import geocoder
import tkinter as tk
import webbrowser
import datetime

# Retrieves radio stations based on the provided genre
def get_stations_by_genre(genre):
    url = f"http://all.api.radio-browser.info/json/stations/bytagexact/{genre}"
    response = requests.get(url)
    stations = response.json()

    return stations

# Opens the provided URL to play the radio station
def play_station(url):
    webbrowser.open(url)

# Searches for radio stations based on the entered genre
def search_stations(genre_entry, station_list):
    genre = genre_entry.get()
    stations = get_stations_by_genre(genre)

    station_list.delete(0, tk.END)

    if stations:
        for station in stations:
            name = station["name"]
            url = station["url"]
            station_list.insert(tk.END, name)
            station_list.bind(
                "<Double-Button-1>", lambda event, url=url: play_station(url)
            )
    else:
        station_list.insert(tk.END, "No stations found for this genre")

# Clears the genre entry field
def clear_genre_entry(genre_entry):
    genre_entry.delete(0, tk.END)

# Updates the clock label with the current time and date
def update_clock(clock_label):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %d-%m-%Y")
    clock_label.config(text=f"{current_time}\n {current_date}")
    clock_label.after(1000, update_clock, clock_label)

# Retrieves the current weather information using the OpenWeatherMap API
def get_weather(api_key):
    g = geocoder.ip("me")
    lat, lng = g.latlng
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    print(response.text)

    return data


api_key = "7035e16a4c557d2b0aba5937df50a409"

# Displays the current weather information in a separate window
def display_weather():
    weather_data = get_weather(api_key)
    if weather_data:
        temp = weather_data["main"]["temp"]
        condition = weather_data["weather"][0]["description"]
        pressure = weather_data["main"]["pressure"]
        wind_speed = weather_data["wind"]["speed"]
        wind_degree = weather_data["wind"]["deg"]

    if wind_degree is not None:
        directions = [
            "N",
            "NNE",
            "NE",
            "ENE",
            "E",
            "ESE",
            "SE",
            "SSE",
            "S",
            "SSW",
            "SW",
            "WSW",
            "W",
            "WNW",
            "NW",
            "NNW",
        ]
        index = round(wind_degree / (360.0 / len(directions)))
        wind_direction = directions[index % len(directions)]
    else:
        wind_direction = "N/A"

    weather_window = tk.Toplevel()
    weather_window.title("Current Weather")
    weather_window.geometry("250x150")

    temp_label = tk.Label(weather_window, text=f"Temperature: {temp}°C")
    temp_label.pack()

    condition_label = tk.Label(weather_window, text=f"Condition: {condition}")
    condition_label.pack()

    pressure_label = tk.Label(weather_window, text=f"Pressure: {pressure} hPa")
    pressure_label.pack()

    wind_speed_label = tk.Label(weather_window, text=f"Wind Speed: {wind_speed} m/s")
    wind_speed_label.pack()

    wind_direction_label = tk.Label(
        weather_window, text=f"Wind Direction: {wind_direction} ({wind_degree}°)"
    )
    wind_direction_label.pack()

# Main function to set up the GUI and execute the program
def main():
    window = tk.Tk()
    window.title("Foxy Radio Selection")
    window.geometry("870x679")

    bg_image = tk.PhotoImage(file="images/background.png")
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.lower()

    genre_label = tk.Label(window, text="Enter genre:", font=("Lucida Handwriting", 16))
    genre_label.place(x=10, y=10)

    genre_entry = tk.Entry(window)
    genre_entry.place(x=160, y=10)

    search_button = tk.Button(
        window,
        text="Search",
        font=("Lucida Handwriting", 18),
        command=lambda: search_stations(genre_entry, station_list),
    )
    search_button.place(x=365, y=5)

    clear_button = tk.Button(
        window,
        text="Clear",
        font=("Lucida Handwriting", 15),
        command=lambda: clear_genre_entry(genre_entry),
    )
    clear_button.place(x=290, y=5)

    instructions_label = tk.Label(
        window,
        text="<<Welcome to Foxy Radio Selection App.>>\nEnter a genre and click Search to find radio stations. Double-click on a station to play it.",
        font=("Lucida Handwriting", 16),
    )
    instructions_label.place(x=10, y=60)

    station_list = tk.Listbox(window, height=80, width=50)
    station_list.place(x=10, y=120)

    clock_label = tk.Label(window, text="", font=("Lucida Handwriting", 16))
    clock_label.place(x=612, y=120)
    update_clock(clock_label)

    weather_button = tk.Button(
        window,
        text="Show Weather",
        font=("Lucida Handwriting", 15),
        command=display_weather,
    )
    weather_button.place(x=680, y=5)

    window.mainloop()


if __name__ == "__main__":
    main()
