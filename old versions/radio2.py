import requests
import tkinter as tk
import webbrowser


# function to retrieve radio stations based on a given genre
def get_stations_by_genre(genre):
    url = f"http://all.api.radio-browser.info/json/stations/bytagexact/{genre}"
    response = requests.get(url)
    stations = response.json()

    return stations


# function to play a selected radio station in the default web browser
def play_station(url):
    webbrowser.open(url)


# function to search for radio stations based on the entered genre
def search_stations():
    global genre_entry, station_list

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


# function to clear the genre entry field
def clear_genre_entry():
    global genre_entry

    genre_entry.delete(0, tk.END)


# main function to create and run the programm
def main():
    global genre_entry, station_list

    window = tk.Tk()
    window.title("Foxy Radio Selection")
    window.geometry("900x500")  # set window size to 900x500

    # load background image
    bg_image = tk.PhotoImage(file="images/background.png")
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.lower()

    # create a label for the genre entry field
    genre_label = tk.Label(window, text="Enter genre:", font=("Lucida Handwriting", 16))
    genre_label.grid(row=0, column=0, padx=10, pady=10)

    # create an entry field for the user to enter a genre
    genre_entry = tk.Entry(window)
    genre_entry.grid(row=0, column=1, padx=10, pady=10)

    # create a button to search for radio stations
    search_button = tk.Button(
        window, text="Search", font=("Lucida Handwriting", 18), command=search_stations
    )
    search_button.grid(row=0, column=2, padx=10, pady=10)

    # create a button to clear the genre entry field
    clear_button = tk.Button(
        window, text="Clear", font=("Lucida Handwriting", 16), command=clear_genre_entry
    )
    clear_button.grid(row=0, column=3, padx=10, pady=10)

    # create a label for instructions
    instructions_label = tk.Label(
        window,
        text="<<Welcome to Foxy Radio Selection App.>>\nEnter a genre and click Search to find radio stations. Double-click on a station to play it.",
        font=("Lucida Handwriting", 16),
    )
    instructions_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    # create a listbox to display the results
    station_list = tk.Listbox(window, height=20, width=100)
    station_list.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    window.mainloop()


if __name__ == "__main__":
    main()
