import requests
from ClientGui.Logging.logger import Logger


class UserLocation:

    def __init__(self):
        self.url = "https://get.geojs.io/v1/ip.json"
        self.request_url = 'https://get.geojs.io/v1/ip/geo/'
        self.region = None
        self.city = None
        self.country = None
        self.longitude = None
        self.latitude = None
        self.continent_code = None
        self.ip = None

    def run(self):
        ip_request = requests.get(self.url)
        my_ip = ip_request.json()['ip']

        geo_request_url = self.request_url + my_ip + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data = geo_request.json()
        self.getData(geo_data)

    def getData(self, data):

        for key, val in data.items():
            if key == "longitude":
                self.longitude = val
            elif key == "city":
                self.city = val
            elif key == "region":
                self.region = val
            elif key == "ip":
                self.ip = val
            elif key == "latitude":
                self.latitude = val
            elif key == "country":
                self.country = val
            elif key == "continent_code":
                self.continent_code = val

        Logger.info("Ip: %s" % self.ip)
        Logger.info("Address: %s, %s, %s, %s" % (self.city, self.region, self.country, self.continent_code))
        Logger.info("Longitude: %s Latitude: %s" % (self.longitude, self.latitude))
