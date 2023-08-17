from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

url = 'https://accounts.chotot.com/register'

driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()

# sdt đã tồn tại
def dangki_ca1():
    phone1 = driver.find_element(By.NAME, 'phone')
    phone1.send_keys('0327216383')
    sleep(2)
    pass1 = driver.find_element(By.NAME, 'password')
    pass1.send_keys('12321@')
    sleep(2)
    btdangki1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/button')
    btdangki1.click()
    sleep(7)
    driver.refresh()

dangki_ca1()

# sdt không hợp lệ
def dangki_ca2():
    phone2 = driver.find_element(By.NAME, 'phone')
    phone2.send_keys('03859374782')
    sleep(2)
    pass2 = driver.find_element(By.NAME, 'password')
    pass2.send_keys('554434')
    sleep(2)
    btdangki2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/button')
    btdangki2.click()
    sleep(7)
    driver.refresh()
dangki_ca2()

# sdt đúng, nhập password dưới 5 kí tự
def dangki_ca3():
    phone3 = driver.find_element(By.NAME, 'phone')
    phone3.send_keys('0393984171')
    sleep(2)
    pass3 = driver.find_element(By.NAME, 'password')
    pass3.send_keys('1234')
    sleep(2)
    btdangki3 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/button')
    btdangki3.click()
    sleep(10)
    driver.refresh()

dangki_ca3()

# nhập khoảng trống ở trường mật khẩu
def dangki_ca4():
    phone4 = driver.find_element(By.NAME, 'phone')
    phone4.send_keys('0393984171')
    sleep(2)
    pass4 = driver.find_element(By.NAME, 'password')
    pass4.send_keys('1234       ')
    sleep(2)
    btdangki4 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/button')
    btdangki4.click()
    sleep(10)
    driver.back()

dangki_ca4()

# đăng kí nhập đúng sđt và password
def dangki_ca5():
    phone5 = driver.find_element(By.NAME, 'phone')
    phone5.send_keys('0393984171')
    sleep(2)
    pass5 = driver.find_element(By.NAME, 'password')
    pass5.send_keys('123456')
    sleep(2)
    btdangki5 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/button')
    btdangki5.click()
    sleep(10)
    print('kết thúc')


dangki_ca5()
