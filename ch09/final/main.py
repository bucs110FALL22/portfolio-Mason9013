from Location import LocationAPI
from News import NewsAPI

def main():
    latitude = input("Please enter your latitude: ")
    longitude = input("Please enter your longitude: ")
    location_api = LocationAPI(latitude, longitude)
    country = location_api.get_location()
    news_api = NewsAPI(country)
    news = news_api.get_news()
    print(f"News in {country}:")
    print(news)

main()