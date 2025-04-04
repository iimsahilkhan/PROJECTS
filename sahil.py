import requests  # To make HTTP requests to the weather API
import json  # To handle JSON responses
import pyttsx3  # For text-to-speech conversion

engine = pyttsx3.init() # initializes the text-to-speech engine.
city = input("Enter the Name of City: ")

url = f"http://api.weatherapi.com/v1/current.json?key=9fa6955d9c7e433bb7a81707251103&q={city}"

r = requests.get(url) # requests.get(url) sends an HTTP request to fetch data.

weather_dict = json.loads(r.text) # json.loads() converts the JSON response into a Python dictionary.
                                  # r.text prints the raw JSON response from the API.

w = weather_dict["current"]["temp_c"]  # Extracts current temperature in Celsius
t = weather_dict["current"]["last_updated"]  # Extracts last update time
print(f"The Current Weather in {city} is {w}c\nLast Updated Time is {t}")

engine.say(f"the current weather in {city} is {w} degrees celcius and last updated time is {t}") #prepares the text for speech.
engine.runAndWait() #speaks the text aloud.
