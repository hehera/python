
import requests
from lxml import etree
HEADERS= {
'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",

}
room_url='https://www.douyu.com/7782656'
print("get_page_in函数执行--获取一页中的一个主播信息")
print(room_url)
response= requests.get(room_url,headers=HEADERS)


html=etree.HTML(response.content)
print(html)
DY_ERROR='无'
#print(html)
#1.分类

garde = html.xpath('//a[@class="AnchorLevelTip-levelIcon"]/text()[2]')
for x in garde:
    print("asd")
    print(x)




try:
    print("主播等级", garde)
except IndexError:
    print(print("主播等级", DY_ERROR))