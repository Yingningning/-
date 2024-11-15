import requests
from io import BytesIO
from shutil import copyfileobj
from fake_useragent import UserAgent

proxies = {
    "http": "http://127.0.0.1:7890",
    "https": "http://127.0.0.1:7890",
}
url = r"https://images.idmzj.com/g%2F%E5%85%B3%E4%BA%8E%E5%85%BB%E7%8C%AB%E6%88%91%E4%B8%80%E7%9B%B4%E6%98%AF%E6%96%B0%E6%89%8B%2F%E7%AC%AC216%E8%AF%9D_1715325355%2F01.jpg"
wallpaperId = "64322"
# broswer = create_chrome_driver()
# broswer.get('https://wallhere.com/')
# add_cookies(broswer,'D:\APP\VS CODE\Spider\wallhavencookie.json')
# response = broswer.get(url)
response = requests.get(url,
                        # proxies=proxies,
                        headers={'User-Agent':UserAgent().random,
                                 "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                                "Referer": "https://comic.idmzj.com/guanyuyangmaowoyizhishixinshou/153336.shtml",
                                 },stream=True)

if response:
    with open("dmzj.jpg", "wb") as f:
        f.write(response.content)
        # response.raw.decode_content = True
        # copyfileobj(response.raw, f)
    print("文件下载成功！",response.status_code)
else:
    print("文件下载失败，状态码：", response.status_code)