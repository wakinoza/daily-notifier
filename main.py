import requests

def main():
    URL = "https://www.jma.go.jp/bosai/forecast/data/forecast/230000.json"
    response = requests.get(URL)
    response.raise_for_status()

    weather_data = response.json()

    print(type(weather_data))
    print(len(weather_data))
    print(weather_data[0]["reportDatetime"])
    tomorrow_weather = weather_data[0]["timeSeries"][0]["areas"][0]["weathers"][1]
    print(tomorrow_weather)

if __name__ == "__main__":
    main()