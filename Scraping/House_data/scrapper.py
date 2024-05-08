import requests
from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self):
        self.http_headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        self.url = "https://appbrewery.github.io/Zillow-Clone/"
        self.response = requests.get(url=self.url, headers=self.http_headers)
        self.webpage = self.response.text
        self.soup = BeautifulSoup(self.webpage, "html.parser")
        self.links = [
            link.get("href") for link in self.soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")
        ]
        self.prices = [
            price.text.split('/')[0].replace('+', '').split()[0] for price in
            self.soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
        ]
        self.addresses = [
            ' '.join(address.string.split()).replace("|", '') for address in self.soup.find_all("address")
        ]