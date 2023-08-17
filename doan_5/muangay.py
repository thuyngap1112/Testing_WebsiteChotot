from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

url1 = 'https://www.chotot.com/mua-ban-dong-ho-thanh-pho-thu-duc-tp-ho-chi-minh/96104709.htm'
driver = webdriver.Chrome()

driver.get(url1)
driver.maximize_window()

sleep(2)
driver.find_element(By.XPATH, '//*[@id="buyNowLink"]').click()
