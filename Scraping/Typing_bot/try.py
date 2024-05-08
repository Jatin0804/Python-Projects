from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

edge_options = Options()
edge_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
edge_path = 'msedgedriver.exe'
service = Service(executable_path=edge_path)
driver = webdriver.Edge(service = service)
driver.get('https://bing.com')

element = driver.find_element(By.ID, 'sb_form_q')
element.send_keys('WebDriver')
element.submit()

time.sleep(10)
driver.close()
driver.quit()