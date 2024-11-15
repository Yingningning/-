from utils import create_chrome_driver,add_cookies

browser = create_chrome_driver()
browser.get('https://wallhere.com/get/2305312')
# add_cookies(browser,'taobaocookie.json')
# browser.get(r'https://s.taobao.com/search?commend=all&ie=utf8&initiative_id=tbindexz_20170306&page=1&q=%E5%88%9D%E9%9F%B3%E6%89%8B%E5%8A%9E&search_type=item&sourceId=tb.index&spm=a21bo.jianhua%2Fa.201856.d13&ssid=s5-e&tab=all')