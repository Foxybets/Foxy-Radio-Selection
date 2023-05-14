import requests
import tkinter as tk
import webbrowser
import datetime
#import tkinter.ttk as ttk

def get_stations_by_genre(genre):
    url = f'http://all.api.radio-browser.info/json/stations/bytagexact/{genre}'
    response = requests.get(url)
    stations = response.json()

    return stations

def play_station(url):
    webbrowser.open(url)

def search_stations():
    global genre_entry, station_list

    genre = genre_entry.get()
    stations = get_stations_by_genre(genre)

    station_list.delete(0, tk.END)

    if stations:
        for station in stations:
            name = station['name']
            url = station['url']
            station_list.insert(tk.END, name)
            station_list.bind("<Double-Button-1>", lambda event, url=url: play_station(url))
    else:
        station_list.insert(tk.END, "No stations found for this genre")

def clear_genre_entry():
    global genre_entry

    genre_entry.delete(0, tk.END)


def update_clock():
    global clock_label
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %d-%m-%Y")
    clock_label.config(text=f"{current_time}\n {current_date}")
    clock_label.after(1000, update_clock)



def main():
    global genre_entry, station_list, clock_label

    window = tk.Tk()
    window.title("Foxy Radio Selection")
    window.geometry("900x679") 

    bg_image = tk.PhotoImage(file="images/background.png")
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.lower()

    genre_label = tk.Label(window, text="Enter genre:", font=("Lucida Handwriting", 16))
    genre_label.grid(row=0, column=0, padx=10, pady=10)

    genre_entry = tk.Entry(window)
    genre_entry.grid(row=0, column=1, padx=10, pady=10)

    search_button = tk.Button(window, text="Search",font=("Lucida Handwriting", 18), command=search_stations)
    search_button.grid(row=0, column=2, padx=10, pady=10)

    clear_button = tk.Button(window, text="Clear", font=("Lucida Handwriting", 15), command=clear_genre_entry)
    clear_button.grid(row=0, column=1, padx=0, pady=10, sticky="e")

    #genres = ["Acid Jazz", "Acid Rock", "Alternative", "Ambient", "Americana", "Avant Garde", "Bachata", "Big Band", "Bluegrass", "Blues", "Bossa Nova", "Cajun", "Calypso", "Caribbean", "Celtic", "Chamber", "Chant", "Chillout", "Choral", "Christian", "Classical", "Classic Rock", "Comedy", "Contemporary", "Country", "Cumbia", "Dance", "Darkwave", "Death Metal", "Disco", "Drum and Bass", "Dub", "Easy Listening", "Electronic", "Emo", "Experimental", "Folk", "Funk", "Gangsta", "Garage Rock", "Gospel", "Gothic", "Grindcore", "Grunge", "Hard Rock", "Hardcore", "Heavy Metal", "Hip Hop", "House", "Indie", "Industrial", "Instrumental", "J-Pop", "Jazz", "Jungle", "Latin", "Lounge", "Merengue", "Metal", "Minimal", "New Age", "Noise", "Opera", "Orchestral", "Piano", "Polka", "Pop", "Progressive", "Psychedelic", "Punk", "R&B", "Rap", "Reggae", "Reggaeton", "Rhythm and Blues", "Rock", "Rockabilly", "Salsa", "Samba", "Ska", "Smooth Jazz", "Soft Rock", "Soul", "Soundtrack", "Southern Rock", "Spanish", "Symphonic", "Synthpop", "Tango", "Techno", "Trance", "Trip Hop", "World", "Zydeco"]


    
    #genre_dropdown = ttk.Combobox(window, values=genres)
    #genre_dropdown.grid(row=0, column=1, padx=10, pady=10)

    instructions_label = tk.Label(window, text="<<Welcome to Foxy Radio Selection App.>>\nEnter a genre and click Search to find radio stations. Double-click on a station to play it.", font=("Lucida Handwriting", 16))
    instructions_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    station_list = tk.Listbox(window, height=20, width=100)
    station_list.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    clock_label = tk.Label(window, text="", font=("Lucida Handwriting", 16))
    clock_label.grid(row=3, column=3, columnspan=4, padx=20, pady=10)
    update_clock()

    window.mainloop()

if __name__ == "__main__":
    main()
