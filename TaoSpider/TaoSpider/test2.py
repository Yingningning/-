from utils import create_chrome_driver
import time
import json

browser = create_chrome_driver()
browser.get('https://wallhere.com/zh/login')
#隐式等待
browser.implicitly_wait(10)
username_input = browser.find_element_by_xpath('//*[@id="signin-form"]/div[1]/input')
username_input.send_keys('506856376@qq.com')
password_input = browser.find_element_by_xpath('//*[@id="signin-form"]/div[2]/input')
password_input.send_keys('hyyldlbhs.1314')
login_button = browser.find_element_by_xpath('//*[@id="signin-form"]/div[3]/button')
login_button.click()

time.sleep(30)
print(browser.get_cookies())
with open('wallhavencookie.json','w') as f:
    json.dump(browser.get_cookies(),f)
