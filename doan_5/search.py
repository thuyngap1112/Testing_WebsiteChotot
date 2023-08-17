from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

url = "https://www.chotot.com/"
driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()

# tìm kiếm đúng tên sản phẩm
def search_1():
    search1 = driver.find_element(By.ID, '__inputItemProps')
    search1.send_keys('laptop')
    sleep(2)
    button1 = driver.find_element(By.XPATH, '//*[@id="autoComplete"]/div/div/div/button')
    button1.click()
    sleep(10)
    driver.get(url)


search_1()

# tìm kiếm kí tự đặc biệt
def search_2():
    search2 = driver.find_element(By.ID, '__inputItemProps')
    search2.send_keys('*')
    sleep(2)
    button2 = driver.find_element(By.XPATH, '//*[@id="autoComplete"]/div/div/div/button')
    button2.click()
    sleep(10)
    driver.get(url)

search_2()

# tìm kiếm chưa nhập đầy đủ tên sản phẩm
def search_3():
    search3 = driver.find_element(By.ID, '__inputItemProps')
    search3.send_keys('lap')
    sleep(2)
    button3 = driver.find_element(By.XPATH, '//*[@id="autoComplete"]/div/div/div/button')
    button3.click()

search_3()

