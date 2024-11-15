from selenium import webdriver
import json


def create_chrome_driver(*,headless=False):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
    # options.add_argument("--enable-features=BrowsingTopicsOmniboxApi,InterestCohortAPI")
    # options.add_experimental_option('excludeSwitches',['enable-automation'])
    # options.add_experimental_option('useAutomationExtension',False)
    options.add_argument(r'--user-data-dir=C:\Users\YNN\AppData\Local\Google\Chrome\User Data')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(options=options)
    browser.execute_cdp_cmd(
        'Page.addScriptToEvaluateOnNewDocument',
        {'source':'Object.defineProperty(navigator,"webdriver",{get: () => undefined})'}
    )
    return browser

def add_cookies(browser,cookie_files):
    with open(cookie_files,'r') as f:
        cookie_list = json.load(f)
        for cookie_dict in cookie_list:
            if cookie_dict['secure']:
                browser.add_cookie(cookie_dict)
                print('cookie添加成功')
