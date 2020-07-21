# -*- encoding: utf-8 -*-
'''
@File    :   top10.py
@Time    :   2020/07/21 14:58:07
@Author  :   wheat
@Version :   1.0
@Email   :   wheat0908@gmail.com
'''

# here put the import lib
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
#定义user_agent
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
cookie = 'uuid_n_v=v1; uuid=165B23F0B6E111EA9B3075693A212BAFE4BE70CB6B8F49A09C663184ECBA4F6B; _csrf=8ca27885cc7988243e1a912bc0b8b3343a5b17b36201685389210d0c4f57095a; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_cuid=172eb7e9fb273-0f6f77dbf11517-f7d123e-1fa400-172eb7e9fb3c8; _lxsdk=165B23F0B6E111EA9B3075693A212BAFE4BE70CB6B8F49A09C663184ECBA4F6B; mojo-uuid=c0ebaf63df5f6e71c426b133df429079; mojo-session-id={"id":"ddd3c048566b8b2d411a4fdaa643dc5f","time":1593088844322}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593088844,1593089550; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593089854; __mta=251551289.1593088843792.1593089847689.1593089854611.7; mojo-trace-id=11; _lxsdk_s=172eb7e9fb4-3b1-1f5-167%7C%7C18'

#模拟header
header = {'user-agent': user_agent, 'Cookie': cookie}
#请求地址
myurl = 'https://maoyan.com/films?showType=3'
#request获取网页信息
response = requests.get(myurl, headers=header)
bs_info = bs(response.text, 'html.parser')
movie_list=[]
#获取top10的影片信息
for items,tags in enumerate(bs_info.find_all('div', attrs={'class':'movie-item-hover'})):
    name = tags.find(class_='name').text
    movie_type = tags.find_all(class_='movie-hover-title')[1].text[5:].strip()
    release_time = tags.find(class_='movie-hover-brief').text[7:].strip()
    movie_list.append((name,movie_type,release_time))
    if items == 9 :
        break

top10= pd.DataFrame(movie_list)
top10.to_csv("top10.csv",encoding="utf-8")