from urllib import request,parse
import time
import random
from ua_info import ua_list

#定义一个爬虫类
class TiebaSpider(object):
    #初始化url属性
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?{}'
    #1.请求函数，得到页面，传统三步
    def get_html(self,url):
        req = request.Request(url=url,headers={'User-Agent':random.choice(ua_list)})
        res = request.urlopen(req)
        html = res.read().decode('gbk','ignore')
        return html
    #2.解析函数
    def parse_html(self):
        pass
    #3.保存文件函数
    def save_html(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)
    #4.入口函数
    def run(self):
        name = input('贴吧名：')
        being = int(input('起始页：'))
        end = int(input('终止页：'))
        #+1操作保证能取到整数
        for page in range(being,end+1):
            pn = (page-1)*50
            params = {
                'kw':name,
                'pn':str(pn)
            }
            #拼接地址
            params = parse.urlencode(params)
            url = self.url.format(params)
            #发请求
            html = self.get_html(url=url)
            #定义路径
            filename = '{}-{}页.html'.format(name,page)
            self.save_html(filename=filename,html=html)
            print('第{}页抓取成功'.format(page))
            time.sleep(random.randint(1,2))

#以脚本形式启动
if __name__=='__main__':
    start = time.time()
    spider = TiebaSpider()
    spider.run()
    end = time.time()
    print('执行时间{}'.format(end-start))





        