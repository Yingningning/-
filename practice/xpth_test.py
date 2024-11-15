import requests
from lxml import etree
import re
from urllib.parse import unquote
url = 'https://www.vilipix.com/illust/977a1df65dbe48debb3d348bbcd8980bchs'
response = requests.get(url=url,
                        headers={'Host':'www.vilipix.com'}).text
html = etree.HTML(response)
quotes = html.xpath('/html/body/script[1]/text()')[0]
compli = re.compile(r'http:[^\s,;]*?origin[^\s,;]*?\.(?:png|jpg|JPG|PNG)')
urls = re.findall(compli,quotes)
def decode_specific_parts(content):
    # 使用正则表达式匹配 \uxxxx 形式的字符串
    pattern = re.compile(r'(\\u[a-zA-Z0-9]{4})')
    
    # 对匹配到的每一部分进行解码
    def decode_match(match):
        return match.group().encode('utf-8').decode('unicode_escape')
    
    # 替换原字符串中的内容
    return pattern.sub(decode_match, content)

for url in urls:
    ul = decode_specific_parts(url)
# item = {}
# for quote  in quotes:
#     item['text'] = quote.xpath('./span[@class="text"]/text()')
#     item['author'] = quote.xpath('./span/small/text()')
#     tags = quote.xpath('./div[@class="tags"]//text()')
#     for i in range(len(tags)):
#         tags[i] = tags[i].strip()
#     item['tags'] = tags

# nextpage = html.xpath('//li[@class="next"]/a/@href')[0]
print('0')
