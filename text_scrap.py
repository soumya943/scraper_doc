from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#path finder
data=ChromeDriverManager().install()
# print(data,'--------1')
s= Service(data)#('/home/het-tbs/.wdm/drivers/chromedriver/linux64/105.0.5195.52/chromedriver')
driver = webdriver.Chrome(service = s)
# driver.maximize_window()
driver.get("https://www.google.com")
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.set_window_size(1200, 800)
# driver.get('https://www.google.com')

name = 'Rishi joshi techcronus'

# Find the search input field by its name attribute
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys(name)
search_input.send_keys(Keys.ENTER)

# Find the search results links and click the second link
search_results = driver.find_elements(By.XPATH, '//div[@class="yuRUbf"]/a')
if len(search_results) >= 2:
    search_results[0].click()
html_content = driver.page_source
# print(html_content)
from bs4 import BeautifulSoup

html_code = html_content
soup = BeautifulSoup(html_code, 'html.parser')
# print(soup.prettify(),'---------------')

description = soup.title.contents
# description = description_meta_tag['content']
my_list = description[0].split(" - ")
# text = ' '.join(my_list)
result={
    "Name":my_list[0],
    "Designation":my_list[1],
    "Company":my_list[2]
}
print(result)

