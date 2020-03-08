import requests
import sys
sys.path.append(r'D:\Users\chenwen1\Anaconda3\Lib\site-packages')
from lxml import etree
import csv
with open('python.csv', mode='a',newline='') as f:
    csvwriter = csv.writer(f, dialect='excel')
    csvwriter.writerow(['工作名字', '公司名字', '地址', '薪水'])
for i in range(1, 2):
    url = 'https://search.51job.com/list/040000,000000,0000,00,9,99,python,2,{}.html'.format(i)
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    response1 = response.text
    html = etree.HTML(response1)
    work_name = html.xpath('//div[@id="resultList"]/div[@class="el"]/p/span/a/@title')
    company_name = html.xpath('//div[@id="resultList"]/div[@class="el"]/span[@class="t2"]/a/@title')
    position = html.xpath('//div[@id="resultList"]/div[@class="el"]/span[@class="t3"]/text()')
    salary = html.xpath('//div[@id="resultList"]/div[@class="el"]/span[@class="t4"]/text()')
    for a, b, c, d in zip(work_name, company_name, position, salary):
        with open('python.csv', mode = 'a',newline='') as f:
            csvwriter = csv.writer(f, dialect='excel')
            csvwriter.writerow([a,b,c,d])






