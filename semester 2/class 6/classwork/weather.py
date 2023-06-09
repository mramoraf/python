import requests



def parse_weather(city: str):
    api_key = '1a83f6c534ec655b6dd15a83443667e6'
    url = f'https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}'
    response = requests.get(url)



    return response.json()



    # return response.text


if __name__ == '__main__':
    city = input('Enter your city: ')
    
    weather = parse_weather(city)['main']
    temp = weather['temp'] - 273

    
    
    print(f'City - {city}\nTemperature - {round(temp)}')


