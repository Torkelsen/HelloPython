from selenium import webdriver
from selenium.webdriver.chrome.service import Service

CHROMEDRIVER_PATH = 'chromedriver-win64/chromedriver.exe'

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get('https://demoqa.com/login')

input("Press a key to close the browser")
driver.quit()