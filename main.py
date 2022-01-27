import requests
import json

with open("city.txt", "r") as imegrada:
    try:
        ime = imegrada.read()
    except Error as er:
        print(er)

print(ime)

r1 = requests.get(
    'http://api.openweathermap.org/data/2.5/weather?q=' + ime + ',&appid=53428c410e91b12f9199fd56515ea70c')
web1 = r1.text

r = requests.get(
    'http://api.openweathermap.org/data/2.5/weather?q=' + ime + ',&appid=53428c410e91b12f9199fd56515ea70c')
web = r.json()
print(web1)
temp1 = float(web['main']['temp'])  # temperatura
temp2 = (temp1 - 273.15) * 1.8 + 32
temp3 = (temp2 - 32) / 1.8
print(temp3)
prit = float(web['main']['pressure'])  # pritisak
print(prit)
payload = {' weather': 'description'}
r1 = requests.get(
    'http://api.openweathermap.org/data/2.5/weather?q=' + ime + ',&appid=53428c410e91b12f9199fd56515ea70c',
    params=payload)

text_json = json.loads(r1.text)
print(text_json['weather'])
for weather in text_json['weather']:  # izvlaci opis vremena
    koma = (weather['description'])

print(web)
cordi1 = float(web['coord']['lon'])  # kordinata 1
print(cordi1)
cordi2 = float(web['coord']['lat'])  # kordinata 2
print(cordi2)
humi = web['main']['humidity']
print(humi)
temp4 = float(web['main']['feels_like'])  # temperatura daje osecaj
temp5 = (temp4 - 273.15) * 1.8 + 32
temp6 = (temp5 - 32) / 1.8
print(temp6)
sunce1 = float(web['sys']['sunrise'])  # izlazak sunca
print(sunce1)
sunce1 = float(web['sys']['sunrise'])  # zalazak sunca
print(sunce1)
fh = open('temp.dat', 'w')
fh.write(f"Temperatura u celzijusima iznosi: {temp3}\n")
fh.write(f"Vlaznost vazduha u procentima iznosi: {humi}\n")
fh.write(f"Temperatura daje osecaj kao da je: {temp6}\n")
fh.write(f"Pritisak vazduha iznosi: {prit}\n")
fh.write(f"Kordinata 1: {cordi1}\n")
fh.write(f"Kordinata 2: {cordi2}\n")
fh.write(f"Opis vremena: {koma}\n")
fh.close()
fh1 = open('temp1.txt', 'w')
fh1.write(f"Temperatura u celzijusima iznosi: {temp3}\n")
fh1.write(f"Vlaznost vazduha u procentima iznosi: {humi}\n")
fh1.write(f"Temperatura daje osecaj kao da je: {temp6}\n")
fh1.write(f"Pritisak vazduha iznosi: {prit}\n")
fh1.write(f"Kordinata 1: {cordi1}\n")
fh1.write(f"Kordinata 2: {cordi2}\n")
fh1.write(f"Opis vremena: {koma}\n")
fh1.close()
imegrada.close()
