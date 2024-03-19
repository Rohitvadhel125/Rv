import requests
import win32com.client as win
city = input("enter city name:\n")
url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"
r = requests.get(url)
print(r.text)
speak = win.Dispatch("SAPI.SpVoice")
text = input("enter the text:")
speak.Speak(r.text)


