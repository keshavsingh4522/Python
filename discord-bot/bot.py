import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def ping(ctx):
    await ctx.send('Pong!!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('.weather'):
        print(message.content)
        zip_code = message.content[9:]
        print(zip_code)
        
        weather_json(zip_code)

        # await message.channel.send('Hello!')

def weather_json(zip_code):
# {'coord': {'lon': 80.9949, 'lat': 26.9337}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'base': 'stations', 'main': {'temp': 301.17, 'feels_like': 304.41, 'temp_min': 301.17, 'temp_max': 301.17, 'pressure': 1005, 'humidity': 74, 'sea_level': 1005, 'grnd_level': 992}, 'visibility': 10000, 'wind': {'speed': 3.17, 'deg': 66, 'gust': 5.74}, 'clouds': {'all': 22}, 'dt': 1632761097, 'sys': {'type': 1, 'id': 9176, 'country': 'IN', 'sunrise': 1632702396, 'sunset': 1632745648}, 'timezone': 19800, 'id': 0, 'name': 'Vikas Nagar', 'cod': 200}
    weather_api = '22cc072c163d234122abaa152fa4cd62'
    url = 'https://api.openweathermap.org/data/2.5/weather?zip='+zip_code+',in&appid='+weather_api
    
    json_data = requests.get(url).json()
    print(json_data)
    lat = json_data['coord']['lat']
    lon = json_data['coord']['lon']
    desc = "It Feels Like " +str(json_data['weather'][0]['description'])
    temp = str(json_data['main']['temp']) + "K approx"
    humidity = str(json_data['main']['humidity']) + "%"
    place = json_data['name']
    sunrise = json_data['sys']['sunrise']
    sunset = json_data['sys']['sunset']

    print('lat = ', lat)
    print('lon = ', lon)
    print('desc = ', desc)
    print('temp = ', temp)
    print('humidity = ', humidity)
    print('place = ', place)
    print('sunrise = ', sunrise)
    print('sunset = ', sunset)

token = 'ODkxOTYzMTg0MDgzMjY3NjI0.YVF_cg.PAKWkjOROnZp1AXY8445YndyySc'

bot.run(token)

