import requests
from tqdm import tqdm

headers = {
    'Referer':'https://v.youku.com/v_show/id_XNjQwMDA1MzczMg==.html?s=acdf7d2eff5f46a9a7bd&spm=a2hjt.13141534.1_3.d_1_6&scm=20140719.apircmd.240015.video_XNjQwMDA1MzczMg==',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',

}

url = 'https://valipl.cp31.ott.cibntv.net/67756D6080932713CFC02204E/030006000064BA0012CA19DCACA654EDECF902-7EBC-4615-985C-B91E16927AF6-00001.ts?ccode=0502&duration=60&expire=18000&psid=c654b4b124b834ca8994286fa2a6ec2c41346&ups_client_netip=3db7cf97&ups_ts=1719298256&ups_userid=&utid=lSUBH0%2FvkncCAXckVikcd9gv&vid=XNTk4NTQxNTQ3Mg%3D%3D&eo=1&t=4faf0fb5af52083&cug=1&fms=5bd395e6e76536dd&tr=60&le=8ead9fdc62e0ccccd77a5cd557e6d9a2&ckt=5&m_onoff=0&rid=200000001DC02D6890F87172EC83BE0E371AA7FC02000000&type=mp4hdv3&bc=2&dre=u37&si=73&dst=1&sm=1&operate_type=1&app_key=24679788&app_ver=9.0.12&vkey=Bd10e0e8283923b293cb830e0db2eb81f'
desc = 'Downloading: '
bar = tqdm(unit_scale=True,desc=desc)
response = requests.get(url=url,headers=headers)
if response:
    with open('youku.mp3','wb') as f:
        response = response.iter_content
        for chunk in response(chunk_size=256 * 1024):
            if chunk:
                f.write(chunk)
                bar.update(len(chunk))
                

