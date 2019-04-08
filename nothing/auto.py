from selenium import webdriver
import pyautogui
import time
driver = webdriver.Chrome("/home/gaon/Downloads/chromedriver")

driver.implicitly_wait(3)
driver.get('https://static.dms.istruly.sexy/')

driver.find_element_by_xpath('//*[@id="meal"]/div/header/nav/button').click()
driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/input[1]').send_keys('gaon000')
driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/input[2]').send_keys('arin4242')
driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/button').click()
time.sleep(2)
# pyautogui.press('enter')
button = driver.switch_to_alert()
button.accept()
driver.find_element_by_xpath('//*[@id="apply"]/div/div[2]/a[1]/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div[8]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/di'
                             'v[2]/div/div[1]/ul/li[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/table/tr[1]/td[4]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]').click()
time.sleep(2)
button.accept()

