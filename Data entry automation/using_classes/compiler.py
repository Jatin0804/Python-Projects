import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSdl8xbBF_de10E3XRjHmrn45V3kpaqhyHYiHHH_-WMNwtNNbA/viewform?usp=sf_link"

class Compiler:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--window-size=2560,1440")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(GOOGLE_FORM_LINK)
        time.sleep(2)

    def fill_form(self, address, price, link):
        address_box = self.driver.find_element(By.XPATH,
                                               value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        address_box.click()
        address_box.send_keys(address)
        price_box = self.driver.find_element(By.XPATH,
                                             value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        price_box.click()
        price_box.send_keys(price)
        link_box = self.driver.find_element(By.XPATH,
                                            value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        link_box.click()
        link_box.send_keys(link)
        button = self.driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")
        button.click()
        another_answer_page = self.driver.find_element(By.CSS_SELECTOR, value="a")
        another_answer_page.click()

