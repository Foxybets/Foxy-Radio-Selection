import pytest
from project import get_stations_by_genre, get_weather, search_stations

# Test get_stations_by_genre function
def test_get_stations_by_genre():
    genre = "rock"
    stations = get_stations_by_genre(genre)
    assert isinstance(stations, list)
    assert len(stations) > 0

# Test get_weather function
def test_get_weather():
    weather_data = get_weather("7035e16a4c557d2b0aba5937df50a409")
    assert weather_data is not None
    assert "main" in weather_data
    assert "weather" in weather_data
    assert "wind" in weather_data




    

def main():
    #test_search_stations()
    test_get_weather()
    test_get_stations_by_genre()


if __name__ == "__main__":
    main()