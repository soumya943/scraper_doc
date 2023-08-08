import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
desired_version = "93.0.4577.63"  # Replace with the version that matches your Chrome browser
# Replace with the actual path
chrome_driver_path = f'/path/to/chromedriver_{desired_version}'  
s = Service(chrome_driver_path)
chrome_options = Options()
chrome_options.headless = False 

driver = webdriver.Chrome(service=s, options=chrome_options)
url = "https://www.expert.de/shop/unsere-produkte/haushalt-kuche/waschen-trocknen-bugeln-nahen/waschmaschinen/32008151057-wg44g000ex-waschmaschine.html"
driver.get(url)
time.sleep(5)
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')

text = soup.get_text()

text=list(filter(None,[chunk for chunk in text.splitlines()]))
text=''.join(chunk for chunk in text if chunk!=" ")
print(text)