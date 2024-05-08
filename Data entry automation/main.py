from bs4 import BeautifulSoup
import requests


sheets_link = "https://docs.google.com/forms/d/e/1FAIpQLSdl8xbBF_de10E3XRjHmrn45V3kpaqhyHYiHHH_-WMNwtNNbA/viewform?usp=sf_link"
website_link = "https://appbrewery.github.io/Zillow-Clone/"

header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    "Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8,hi;q=0.7"
}

#  use beautifulSoup to extract data
response = requests.get(website_link, headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")

# // get all prices
prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
all_prices = [price.getText().replace("/mo", "").split("+")[0] for price in prices]
# print(all_prices)
# print(len(all_prices))


# // get all addresses
addresses = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
all_addresses = [add.getText().replace(" | ","").strip() for add in addresses]
# print(all_addresses)
# print(len(all_addresses))


# // get all links
links = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
all_links = [link["href"] for link in links]
# print(all_links)
# print(len(all_links))


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option(name="detach", value=True)
driver = webdriver.Edge(options=edge_options)

for n in range(0, len(all_prices)):
    driver.get(sheets_link)
    time.sleep(3)

    address = driver.find_element(by=By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    submit_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()