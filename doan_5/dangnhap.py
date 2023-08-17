from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

sdt = "0327216383"
password = "thuynga2108"

url = "https://accounts.chotot.com/login"

driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()

#  đăng nhập sai số điện thoại và để trống trường password
def dangnhap_ca1():
    phone1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/div[2]/div/input')
    phone1.send_keys('0302938493')
    sleep(2)
    pass1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/div[3]/div/input')
    pass1.send_keys()
    sleep(1)
    btdangnhap1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/button')
    btdangnhap1.click()
    sleep(8)

    driver.refresh()
    return
dangnhap_ca1()

# nhập đúng số đt, sai trường password
def dangnhap_ca2():
    phone2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/div[2]/div/input')
    phone2.send_keys(sdt)
    sleep(2)
    pass2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/div[3]/div/input')
    pass2.send_keys('tdncbjkdh')
    sleep(1)
    btdangnhap2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/button')
    btdangnhap2.click()
    sleep(8)
    driver.refresh()

dangnhap_ca2()



# kiểm tra tài khoản bị vô hiệu hoá
def dangnhap_ca3():
    phone3 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/div[2]/div/input')
    phone3.send_keys('0388827206')
    sleep(2)
    pass3 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/div[3]/div/input')
    pass3.send_keys('772200')
    sleep(1)
    btdangnhap3 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/button')
    btdangnhap3.click()
    sleep(8)
    driver.refresh()
dangnhap_ca3()

# bấm quên mật khẩu
def dangnhap_ca4():
    phone4 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/div/p[1]/a')
    phone4.click()
    sleep(2)
    pass4 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/form/div/div/input')
    pass4.send_keys('0327216383')
    sleep(3)
    btdangnhap4 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/form/button')
    btdangnhap4.click()
    sleep(8)
    driver.refresh()

dangnhap_ca4()

# đăng nhập đúng số điện thoại và password
def dangnhap_ca5():
    phone5 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/div[2]/div/input')
    phone5.send_keys(sdt)
    sleep(3)
    pass5 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/div[3]/div/input')
    pass5.send_keys(password)
    sleep(1)
    btdangnhap5 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div/form/button')
    btdangnhap5.click()
    sleep(10)

dangnhap_ca5()

# đăng xuất
def dangxuat():
    driver.find_element(By.ID, 'btnundefinedundefined').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="__next"]/header/div/div[2]/div[1]/div/div/div/div/div[22]/a').click()
    sleep(10)

dangxuat()


driver.close()
