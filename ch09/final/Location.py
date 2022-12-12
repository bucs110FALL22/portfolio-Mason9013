import requests

class LocationAPI():
    def __init__(self, latitude, longitude):
      '''
      This function takes longitute and latitude and finds location
      args: (int) The long and lat values
      return: none
      '''
      self.latitude = latitude
      self.longitude = longitude
      self.location_url = 'https://api.geodatasource.com/v2/city'
      self.params = {'key':'0Q25E3YF0CBFP2SV0NHKBDARZXJF2ZHP', 
      'lat':self.latitude, 'lng':self.longitude}


    
    def get_location(self):
        response = requests.get(self.location_url, params=self.params)
        data = response.json()
        return data['country']
      
'''
This function takes location and returns a country
args: none
return: (str) country 
'''