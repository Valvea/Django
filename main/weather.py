import json
import urllib.request


class Weather:
    appid = "&appid=86e2bc0b2caf8a9c933c75044312c5d4"
    id_city = "id=524901"
    lat = 55.75
    lon = 37.62
    list_of_weathers = []
    py_obj = object
    time_morning =''
    time_evening =''



    def __init__(self,from_time="09:00:00",to_time="21:00:00"):
        self.time_morning=from_time
        self.time_evening=to_time
        self.get_reqst()


    def get_weather(self):
        self.create_wiew_of_weather()
        return self.list_of_weathers

    def get_reqst(self):
        r = urllib.request.urlopen(
            f'https://api.openweathermap.org/data/2.5/forecast?lat={self.lat}&lon={self.lon}{self.appid}')
        self.py_obj = json.load(r)

    def refresh_weather(self):
        self.get_reqst()


    def __write_keys__(self):
        it = 0
        if len(self.list_of_weathers)!=0:
            self.list_of_weathers.clear()
        for obj in self.py_obj['list']:
            if self.find_data(obj['dt_txt']) is True:
                self.list_of_weathers.append(it)
            else:
                pass
            it += 1



    def change_time(self,from_='12:00:00',to_='00:00:00'):
        self.time_morning=from_
        self.time_evening=to_




    def find_data(self, string ):
        if string.split(' ')[1] == self.time_evening or string.split(' ')[1] == self.time_morning:
            return True
        else:
            return False

    def create_wiew_of_weather (self):
        self.__write_keys__()
        index = 0
        for i in self.list_of_weathers:
            self.list_of_weathers[index] = {
                "data_time": 'Число ' + self.py_obj['list'][i]['dt_txt'].split('-')[2][:2] + ' / время' +self.py_obj['list'][i]['dt_txt'].split('-')[2][2:8],
                "Tmax": f"{self.py_obj['list'][i]['main']['temp_max']-273.15:.{1}f} ",
                "Tmin": f"{self.py_obj['list'][i]['main']['temp_min']-273.15:.{1}f} ",
                "Wind": self.py_obj['list'][i]['wind']['speed'],
                "Osadky": self.py_obj['list'][i]['weather'][0]['main'],
                "logo": self.py_obj['list'][i]['weather'][0]['icon'],
                "City": "Москва",
            }
            index += 1






