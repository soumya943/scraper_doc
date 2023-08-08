# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup

# # Set up Chrome driver
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.set_window_size(1200, 800)

# # Open Google homepage
# driver.get('https://www.google.com')

# name = 'parth techcronus'

# # Find the search input field by its name attribute
# search_input = driver.find_element(By.NAME, 'q')
# search_input.send_keys(name)
# search_input.send_keys(Keys.ENTER)

# # Wait for the page to load
# driver.implicitly_wait(2)

# # Find the search results links and click the first link
# search_results = driver.find_elements(By.XPATH, '//div[@class="yuRUbf"]/a')
# if len(search_results) >= 1:
#     search_results[0].click()

# # Get the page source
# html_content = driver.page_source

# # Close the browser
# driver.quit()

# # Parse the HTML content
# soup = BeautifulSoup(html_content, 'html.parser')

# # Extract information from the page
# title = soup.title.string
# my_list = title.split(" - ")
# result = {
#     "Name": my_list[0],
#     "Designation": my_list[1],
#     "Company": my_list[2]
# }
# print(result)

#=============================== function base =================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service

def scrape_google_result(name):
    try:
        # Set up Chrome driver
        data=ChromeDriverManager().install()
        
        s= Service(data)#('/home/het-tbs/.wdm/drivers/chromedriver/linux64/105.0.5195.52/chromedriver')
        driver = webdriver.Chrome(service = s)    
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver.set_window_size(1200, 800)

        # Open Google homepage
        driver.get('https://www.google.com')

        # Find the search input field by its name attribute
        search_input = driver.find_element(By.NAME, 'q')
        search_input.send_keys(name)
        search_input.send_keys(Keys.ENTER)

        # Wait for the page to load
        driver.implicitly_wait(5)

        # Find the search results links and click the first link
        search_results = driver.find_elements(By.XPATH, '//div[@class="yuRUbf"]/a')
        if len(search_results) >= 1:
            search_results[0].click()

        # Get the page source
        html_content = driver.page_source

        # Close the browser
        driver.quit()

        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract information from the page
        title = soup.title.string
        # print(title,'------------')
        my_list = title.split(" - ")
        result = {
            "Name": my_list[0],
            "Designation": my_list[1],
            "Company": my_list[2]
        }

        return result

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Usage example
name = 'Rishi joshi techcronus'
result = scrape_google_result(name)
if result:
    print(result)

#==============Example++++++++++++++
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup

# def scrape_google_result(name):
#     try:
#         # Set up Chrome driver with headless option
#         options = Options()
#         options.add_argument('--headless')
#         data = ChromeDriverManager().install()
#         s = Service(data)
#         driver = webdriver.Chrome(service=s, options=options)

#         # Open Google homepage
#         driver.get('https://www.google.com')

#         # Find the search input field by its name attribute
#         search_input = driver.find_element(By.NAME, 'q')
#         search_input.send_keys(name)
#         search_input.send_keys(Keys.ENTER)

#         # Wait for the page to load
#         driver.implicitly_wait(5)

#         # Find the search results links and click the first link
#         search_results = driver.find_elements(By.XPATH, '//div[@class="yuRUbf"]/a')
#         if len(search_results) >= 1:
#             search_results[0].click()

#         # Get the page source
#         html_content = driver.page_source

#         # Close the browser
#         driver.quit()

#         # Parse the HTML content
#         soup = BeautifulSoup(html_content.decode('utf-8'), 'html.parser')
#         print(soup,'-----------------3')

#         # Extract information from the page
#         title = soup.title.string
#         # print(title,'-----------------4')
#         my_list = title.split(" - ")
#         result = {
#             "Name": my_list[0],
#             "Designation": my_list[1],
#             "Company": my_list[2]
#         }

#         return result

#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None

# # Usage example
# name = 'parth techcronus'
# result = scrape_google_result(name)
# if result:
#     print(result)