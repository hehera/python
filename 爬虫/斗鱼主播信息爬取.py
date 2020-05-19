'''
1.获取所有页
2.获取所有页的斗鱼在线主播房间号
3.逐个进入每个房间号，并获取每个房间号的信息
'''

import requests
from lxml import etree
import time
DY_BW_URL='https://www.douyu.com'#斗鱼的基本网址
DY_ERROR='无'
HEADERS= {
'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
'referer':"https://www.douyu.com/directory/all",
'accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",


}


def get_DY_ROOM_URLS(url):    #打印一页所有斗鱼主播的房间号地址
    print("get_DY_ROOM_URL函数执行--打印一页所有斗鱼主播的房间号地址")
    response =requests.get(url,headers=HEADERS)
    #打印完页面
    html= etree.HTML(response.text)
    room_urls =html.xpath('//li[@class="layout-Cover-item"]//a/@href')

    room_urls=map(lambda url:DY_BW_URL+url,room_urls )#实现获取完整的房间号

    return room_urls

#获取所有页
def get_DY_page():
    pass



def get_DY_page_in(room_url):#获取一页中的一个主播信息
    print("get_page_in函数执行--获取一页中的一个主播信息")
    print(room_url)
    response= requests.get(room_url,headers=HEADERS)
    #text=response.content.decode('utf-8')
    html=etree.HTML(response.text)

    #1.主播名
    get_DY_name(html)
    #2.主播口号
    get_DY_slogan(html)
    #3.主播等级
    get_DY_garde(html)
    #4.分类
    get_DY_classify(html)
    #5.热度
    get_DY_hot(html)
    #5.鱼粮
    get_DY_fishes(html)
    #6.在线友邻
    get_DY_friends(html)
    #7.关注
    get_DY_con(html)
    #8.公告
    get_DY_ann(html)
    #9.贵宾在线人数
    get_DY_vips(html)
    #10.小时榜
    get_DY_hour(html)
    #11.粉丝团总人数
    get_DY_fans(html)
    #12.获取时间
    get_DY_time()



#//a[@class="Title-anchorName"]/@title
#1.主播名
def get_DY_name(html):
    name=html.xpath('//div[@class="Title-anchorName"]/@title')

    try:
        print("主播名",name[0])
    except IndexError:
        print(print("主播名",DY_ERROR))

#2.主播口号
def get_DY_slogan(html):
    slogan=html.xpath('//h3[@class="Title-headlineH2"]/text()')

    try:
        print("主播口号",slogan[0])
    except IndexError:
        print(print("主播名",DY_ERROR))


#3.主播等级
def get_DY_garde(html):
    garde=html.xpath('//a[@class="AnchorLevelTip-levelIcon"]/text()[2]')

    try:
        print("主播等级",garde)
    except IndexError:
        print(print("主播等级",DY_ERROR))


#4.分类
def get_DY_classify(html):

    classify=html.xpath('//div[@class="Title-categoryList clearFix"]//a[@class="Title-categoryItem"]//text()')

    try:
        print("一级分类",classify[0])
    except IndexError:
        print("一级分类",DY_ERROR)

    try:
        print("二级分类",classify[1])
    except IndexError:
        print("三级分类",DY_ERROR)

    try:
        print("三级分类", classify[2])
    except IndexError:
        print("三级分类",DY_ERROR)

#5.热度
def get_DY_hot(html):
    hot=html.xpath('//div[@class="Title-anchorText"]//text()')

    try:
        print("主播热度",hot)
    except IndexError:
        print(print("主播热度",DY_ERROR))

#5.鱼粮
def get_DY_fishes(html):
    fishes = html.xpath('//div[@class="Title-sharkWeightText"]//text()')

    try:
        print("主播鱼粮", fishes)
    except IndexError:
        print(print("主播鱼粮", DY_ERROR))

#6.在线友邻
def get_DY_friends(html):
    friends = html.xpath('//i[@class="Title-anchorFriendNumber"]//text()')

    try:
        print("在线友邻", friends)
    except IndexError:
        print(print("在线友邻", DY_ERROR))

#7.关注
def get_DY_con(html):
    con = html.xpath('//span[@class="Title-followNum"]//text()')

    try:
        print("主播关注", con)
    except IndexError:
        print(print("主播关注", DY_ERROR))

#8.公告
def get_DY_ann(html):
    ann = html.xpath('//div[@class="AnchorAnnounce"]//text()')

    try:
        print("主播公告", ann)
    except IndexError:
        print(print("主播公告", DY_ERROR))
#9.贵宾在线人数
def get_DY_vips(html):
    vips = html.xpath('//div[@class="ChatRank-tabTitle"]//em/text()')

    try:
        print("主播贵宾在线人数", vips)
    except IndexError:
        print(print("主播贵宾在线人数", DY_ERROR))
#10.小时榜
def get_DY_hour(html):
    hour = html.xpath('//span[@class="RankCoverage-order"]//text()')

    try:
        print("主播小时榜", hour)
    except IndexError:
        print(print("主播小时榜", DY_ERROR))
#11.粉丝团总人数
def get_DY_fans(html):
    fans = html.xpath('//span[@class="FansRankBottom-yellow"]//text()')

    try:
        print("主播粉丝团人数", fans)
    except IndexError:
        print(print("主播粉丝团人数", DY_ERROR))
#12.主播个性标签
def get_DY_label(html):
    label = html.xpath('//span[@class="Title-blockInline"]/a[@class="Title-official"]/text()')

    try:
        print("主播个性标签", label)
    except IndexError:
        print(print("主播个性标签", DY_ERROR))
#13.获取时间
def get_DY_time():
    print("获取时的时间:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))





#主函数
if __name__=='__main__':

    url = 'https://www.douyu.com/directory/all'
    #执行前时间
    print("获取前时间:",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    room_urls=get_DY_ROOM_URLS(url)
    #for room_url in room_urls:
     #   print(room_url)
    for room_url in room_urls:
        get_DY_page_in(room_url)
        #break
    #执行后时间
    print("获取后时间:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

















