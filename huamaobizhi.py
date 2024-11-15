import requests
from lxml import etree
import os
import time
from fake_useragent import UserAgent
from urllib.parse import urlparse,parse_qs,urlencode
import random
from tqdm import tqdm

class huamao_pic(object):
    def __init__(self):
        self.search_url = "https://huamaobizhi.com/search/"
        self.dir = "./huamao/"
        self.tag = input('search tag:')
    def get_headers(self):
        headers = {
            'User-Agent':UserAgent().random
        }
        return headers
    
    def get_search_url(self):
        tag = str(self.tag)
        tag = requests.utils.quote(tag)
        params = {
            'search_tag':tag
        }
        file_path = self.dir + '/{}/page_urls.txt'.format(self.tag)
        if not os.path.exists(file_path):
            response = requests.get(url=self.search_url,
                                    headers=self.get_headers(),
                                    params=params).text
            html = etree.HTML(response)
            num = str(html.xpath('//div[@class="title"]/p/text()')[0])
            num = num.split("，")[0]
            print(num)
            links = html.xpath('//ul[@class="pagination top"]/li')
            dir_path = self.dir + '/{}'.format(self.tag)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            urls = []
            for i,link in enumerate(links[1:-1]):
                url = link.xpath('./a/@href')[0]
                url = 'https://huamaobizhi.com/search/' + url
                if i==0:
                    parsed_url = urlparse(url=url)
                    query_params = parse_qs(parsed_url.query)
                    query_params['page'] = [str(1)]
                    updated_query = urlencode(query_params,doseq=True)
                    # new_url = 'https://huamaobizhi.com/？' + updated_query
                    new_url = parsed_url._replace(query=updated_query).geturl()
                    urls.append(new_url)
                    urls.append(url)
                else:
                    urls.append(url)
            with open(dir_path + '/page_urls.txt','w') as f:
                for line in urls:
                    f.write(line+'\n')
            return(file_path)
        else:
            print('page_urls.txt existing')
            return file_path
    
    def get_img_ids(self):
        headers = self.get_headers()
        file_path = self.dir + '/{}'.format(self.tag) + '/img_ids.txt'
        ids = []
        if not os.path.exists(file_path):
            with open(self.dir + '/{}'.format(self.tag) + '/page_urls.txt','r') as f:
                page_urls = [line.strip() for line in f]
            for page_url in page_urls:
                respones = requests.get(url=page_url,headers=headers).text
                html = etree.HTML(respones)
                divs = html.xpath('//div[@class="images-card"]')
                for div in divs:
                    href = div.xpath('./a/span/@data-imgid')
                    if href:
                        ids.append(href)
            with open(file_path,'w') as f:
                for id in ids:
                    f.write(str(id) + '\n')
        else:
            print('img_ids.txt existing')           

    def save_img(self):
        with open(self.dir + '/{}'.format(self.tag) + '/img_ids.txt','r') as f:
            img_ids = [id.strip() for id in f]
        i = 0
        for img_id in img_ids:
            url = "https://huamaobizhi.com/normal-download/"
            wallpaperId = img_id[2:-2]
            time_seconds = 30
            max_stale_periods = 3
            stale_periods = 2

            if os.path.exists(self.dir + '/{}/{}.png'.format(self.tag,img_id)):
                print('{} existing'.format(wallpaperId))
            else:
                desc = 'downloading {}'.format(wallpaperId)
                chunk_size = 256 * 1024
                progress_bar = tqdm(initial=0,unit='B',unit_divisor=1024,unit_scale=True,desc=desc)
                while True:
                    response = requests.post(url=url, data={"wallpaperId": wallpaperId}, stream=True,headers=self.get_headers())
                    if response.status_code == 200:
                        download_status = 1
                        response = response.iter_content
                        with open(self.dir + '/{}/{}.png'.format(self.tag,img_id),'wb') as f:
                            start_time = time.time()
                            for chunk in response(chunk_size=chunk_size):
                                if chunk:
                                    f.write(chunk)
                                    previous_downloaded_bytes = f.tell()
                                    progress_bar.update(len(chunk))
                                    if time.time() - start_time >= time_seconds:
                                        current_position = f.tell()
                                        download_bytes = current_position - previous_downloaded_bytes
                                        if download_bytes <= 0:
                                            print("stop,remove and retrying")
                                            os.remove(self.dir + '/{}/{}.png'.format(self.tag,img_id))
                                            download_status = 0
                                            time.sleep(random.randint(1,2))
                                            break    
                            progress_bar.close()                                        
                        if download_status ==1:
                            print('{} Save Success'.format(wallpaperId))
                            i = i+1
                            time.sleep(random.randint(1,2))
                            break
                    else:
                        print('Status code {} received, retrying...'.format(response.status_code))
                        time.sleep(random.randint(1,2))
                    
        print('all:{} get done'.format(i))
    
    def run(self):
        self.get_search_url()
        self.get_img_ids()
        self.save_img()

if __name__=="__main__":
    huamao = huamao_pic()
    huamao.run()




