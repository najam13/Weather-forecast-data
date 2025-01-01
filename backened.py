import requests

Api_key = '07e70c01b6e497c2119507a4f7f41891'


def get_data(place, forecast_days=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={Api_key}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="tokyo", forecast_days=3))
