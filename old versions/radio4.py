import requests
import tkinter as tk
import webbrowser
import datetime


def get_stations_by_genre(genre):
    url = f"http://all.api.radio-browser.info/json/stations/bytagexact/{genre}"
    response = requests.get(url)
    stations = response.json()

    return stations


def play_station(url):
    webbrowser.open(url)


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


def clear_genre_entry(genre_entry):
    genre_entry.delete(0, tk.END)


def update_clock(clock_label):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %d-%m-%Y")
    clock_label.config(text=f"{current_time}\n {current_date}")
    clock_label.after(1000, update_clock, clock_label)


def main():
    window = tk.Tk()
    window.title("Foxy Radio Selection")
    window.geometry("900x679")

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

    window.mainloop()


if __name__ == "__main__":
    main()
