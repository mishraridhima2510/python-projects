import json
from urllib.request import urlopen
from urllib.parse import quote


def get_weather(city):
    city = quote(city)

    url = f"https://wttr.in/{city}?format=j1"

    try:
        with urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))

        current = data["current_condition"][0]

        print("\n🌦️ WEATHER REPORT")
        print("=" * 40)
        print(f"City        : {city}")
        print(f"Temperature : {current['temp_C']}°C")
        print(f"Feels Like  : {current['FeelsLikeC']}°C")
        print(f"Humidity    : {current['humidity']}%")
        print(f"Wind Speed  : {current['windspeedKmph']} km/h")
        print(f"Condition   : {current['weatherDesc'][0]['value']}")

    except Exception as error:
        print(f"❌ Unable to fetch weather data: {error}")


def main():
    print("=" * 40)
    print("       🌦️ WEATHER API")
    print("=" * 40)

    city = input("Enter city name: ").strip()

    if not city:
        print("❌ City name cannot be empty.")
        return

    get_weather(city)


if __name__ == "__main__":
    main()
