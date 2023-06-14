# import libraries
import requests
import geocoder
import tkinter as tk
import webbrowser
import datetime
import json
import logging

logging.basicConfig(
    filename="app.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)


with open("config.json") as config_file:
    config = json.load(config_file)
    api_key = config["api_key"]


# Retrieves radio stations based on the provided genre
def get_stations_by_genre(genre):
    url = f"http://all.api.radio-browser.info/json/stations/bytagexact/{genre}"
    logging.info(f"Sending API request to {url}")
    response = requests.get(url)
    stations = response.json()

    return stations


# Opens the provided URL to play the radio station
def play_station(url):
    logging.info(f"Playing radio station: {url}")
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
    try:
        g = geocoder.ip("me")
        lat, lng = g.latlng
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}&units=metric"
        logging.info(f"Sending API request to {url}")
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        logging.debug(f"API response: {data}")
        return data
    except (requests.exceptions.RequestException, ValueError) as e:
        logging.error(f"Error occurred during weather API request: {e}")
        return None


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
            logging.info("Weather information displayed.")
        else:
            wind_direction = "N/A"

        weather_window = tk.Toplevel()
        weather_window.title("Current Weather")
        weather_window.geometry("250x150+697+250")

        temp_label = tk.Label(weather_window, text=f"Temperature: {temp}°C")
        temp_label.pack()

        condition_label = tk.Label(weather_window, text=f"Condition: {condition}")
        condition_label.pack()

        pressure_label = tk.Label(weather_window, text=f"Pressure: {pressure} hPa")
        pressure_label.pack()

        wind_speed_label = tk.Label(
            weather_window, text=f"Wind Speed: {wind_speed} m/s"
        )
        wind_speed_label.pack()

        wind_direction_label = tk.Label(
            weather_window, text=f"Wind Direction: {wind_direction} ({wind_degree}°)"
        )
        wind_direction_label.pack()
    else:
        # Handle the case where an error occurred during the API request
        weather_window = tk.Toplevel()
        weather_window.title("Error")
        weather_window.geometry("200x100")

        error_label = tk.Label(
            weather_window,
            text="An error occurred while fetching weather data.",
            font=("Courier New", 12),
            fg="red",
        )
        error_label.pack()


# Main function to set up the GUI and execute the program
def main():
    window = tk.Tk()
    window.title("Foxy Radio Selection")
    window.geometry("870x679")

    bg_image = tk.PhotoImage(file="images/background.png")
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.lower()

    genre_label = tk.Label(window, text="Enter genre:", font=("Courier New", 16))
    genre_label.place(x=10, y=10)

    genre_entry = tk.Entry(window)
    genre_entry.place(x=160, y=10)

    search_button = tk.Button(
        window,
        text="Search",
        font=("Courier New", 18),
        command=lambda: search_stations(genre_entry, station_list),
    )
    search_button.place(x=365, y=5)

    clear_button = tk.Button(
        window,
        text="Clear",
        font=("Courier New", 15),
        command=lambda: clear_genre_entry(genre_entry),
    )
    clear_button.place(x=290, y=5)

    instructions_label = tk.Label(
        window,
        text="<<Welcome to Foxy Radio Selection App.>>\nEnter a genre and click Search to find radio stations. Double-click on a station to play it.",
        font=("Courier New", 16),
    )
    instructions_label.place(x=10, y=60)

    station_list = tk.Listbox(window, height=80, width=50)
    station_list.place(x=10, y=120)

    clock_label = tk.Label(window, text="", font=("Courier New", 16))
    clock_label.place(x=612, y=120)
    update_clock(clock_label)

    weather_button = tk.Button(
        window,
        text="Show Weather",
        font=("Courier New", 15),
        command=display_weather,
    )
    weather_button.place(x=680, y=5)

    window.mainloop()


if __name__ == "__main__":
    main()
