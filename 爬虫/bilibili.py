import requests
import pprint
import re
import time
# requests.packages.urllib3.disable_warnings()
# url = 'https://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&songid=268583242'
# response = requests.get(url, verify=False)
# data = response.json()
# pprint.pprint(data)
# file_link = data['bitrate']['file_link']
# title = data['songinfo']['title']
# print(file_link)
# response = requests.get(file_link)
# with open(title+'.mp3', mode='wb') as f:
#     f.write(response.content)
requests.packages.urllib3.disable_warnings()
response = requests.get('https://music.taihe.com/artist/210120835',verify=False)
song_id = re.findall(r'<a href="/song/(.*?)" .*?>', response.text)
song_id = set(song_id)
print(song_id)
for songid in song_id:
    url = 'https://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&songid={}'.format(songid)
    response = requests.get(url, verify=False)
    data = response.json()
#    pprint.pprint(data)
    file_link = data['bitrate']['file_link']
    title = data['songinfo']['title']
    print(file_link, title)
    response = requests.get(file_link)
    with open(title+'.aac', mode='wb') as f:
        f.write(response.content)
    time.sleep(3)





