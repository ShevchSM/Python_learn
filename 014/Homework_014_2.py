####################################################################################################
# Задача №2 CLI City
####################################################################################################
from bs4 import BeautifulSoup
import requests
import click
####################################################################################################

####################################################################################################


@click.command()
@click.argument('city')
def main(city):
    my_city = 'city'
    country = 'Country'
    currency = 'USD'
    population = 130000


url = 'https://en.wikipedia.org/wiki/'
# url = 'https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key='

response = requests.get(url)

print(response)

if __name__ == '__main__':
    session = requests.Session()
    # # print(session.headers)
    # session.headers.update(headers)
    # # print(session.headers)
    city = 'Kyiv'
    response01 = requests.get(f'{url}Lists_of_cities_by_country')
    country_list_links = []
    if response01.status_code == 200:
        soup = BeautifulSoup(response01.text, 'html.parser')
        for link_of_country in soup.find_all('b'):
            country_link = link_of_country.a.get('href')
            if 'List_of_ci' in country_link:
                country_list_links.append(country_link[country_link.find('List'):])
        print(country_list_links)

    for list_of_city in country_list_links:
        response02 = requests.get(f'{url}{list_of_city}')
        city_list_links = []
        if response02.status_code == 200:
            soup = BeautifulSoup(response02.text, 'html.parser')
            for link_of_city in soup.find_all(class_="div-col"):
                city_link = link_of_city.a.get('href')
                print(city_link)

