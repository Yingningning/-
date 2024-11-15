from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
time.sleep(3)
inp = browser.find_element_by_xpath('//*[@id="kw"]')
inp.send_keys('初音未来')
time.sleep(3)
so = browser.find_element_by_xpath('//*[@id="su"]')
so.click()
time.sleep(3)
browser.quit()