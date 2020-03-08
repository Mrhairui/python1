import requests
import re
'''
# response = requests.get('https://video.pearvideo.com/mp4/adshort/20200229/cont-1657104-14963950_adpkg-ad_hd.mp4')
# with open ('aa.mp4', mode = 'wb') as f:
#     f.write(response.content)   # 视屏使用content
'''
'''
response = requests.get('https://www.pearvideo.com/video_1657104')
response = response.text
bb = re.findall(r'srcUrl="(.*?)"', response, re.S)[0]  # re.S是匹配整个字符串而不是一行行的匹配
name = re.findall(r'<title>(.*?)</title>', response, re.S)[0]
response = requests.get(bb)
with open (name+'.mp4', mode = 'wb') as f:
    f.write(response.content)   # 视屏使用content
'''
url = requests.get('https://www.pearvideo.com/category_130')
url = url.text
url_list = re.findall('<a href="(video_\d{7})" class="vervideo-lilink actplay">', url, re.S) # 忽略换行符
for url in url_list:
    response = requests.get('https://www.pearvideo.com/' + url)
    response = response.text
    bb = re.findall(r'srcUrl="(.*?)"', response, re.S)[0]  # re.S是匹配整个字符串而不是一行行的匹配
    name = re.findall(r'<title>(.*?)</title>', response, re.S)[0]
    response = requests.get(bb)
    with open(name + '.mp4', mode='wb') as f:
        f.write(response.content)  # 视屏使用content


print(url_list)
