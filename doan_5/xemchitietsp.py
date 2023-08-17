from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

url = 'https://www.chotot.com/mua-ban-thu-cung'

driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()
sleep(2)

link = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div[1]/div[2]/main/div[1]/div[3]/div/div[1]/ul[1]/div[1]/li/a/div[2]/div/h3')
link.click()
sleep(15)
driver.close()

