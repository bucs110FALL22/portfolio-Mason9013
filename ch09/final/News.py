import requests

class NewsAPI():
    def __init__(self, country):
      '''
      This function takes country and gets its news
      args: (str) The country
      return: none
      '''
      self.country = country
      self.news_url = 'https://newsdata.io/api/1/news'
      self.params = {'apikey':'pub_14521c0852c3ba8a9bbfd370da3fee7d11166', 'country':self.country}

    

    def get_news(self):
      '''
      This function returns the news of the country in its langauge
      args: none
      return: (str) The news (in a very unreadable format)
      '''
      response = requests.get(self.news_url, params=self.params)
      data = response.json()
      return data
      
      
  
