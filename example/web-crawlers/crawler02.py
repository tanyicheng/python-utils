# 第一个爬虫示例,爬取百度页面

import requests
from bs4 import BeautifulSoup

def get():

    # 请求网页
    response = requests.get("https://www.autohome.com.cn/news/")
    # 设置编码格式
    response.encoding = 'gbk'
    # 页面解析
    soup = BeautifulSoup(response.text, 'html.parser')
    # 找到id="auto-channel-lazyload-article" 的div节点
    div = soup.find(name='div', attrs={'id': 'auto-channel-lazyload-article'})
    # 在div中找到所有的li标签
    li_list = div.find_all(name='li')
    for li in li_list:
        # 获取新闻标题
        title = li.find(name='h3')
        if not title:
            continue
        # 获取简介
        p = li.find(name='p')
        # 获取连接
        a = li.find(name='a')
        # 获取图片链接
        img = li.find(name='img')
        src = img.get('src')
        src = "https:" + src
        print(title.text)
        print(a.attrs.get('href'))
        print(p.text)
        print(src)
        # 再次发起请求，下载图片 ['https://www2.autoimg.cn/newsdfs/g21/M0B/C7/84/120x90_0_autohomecar__ChsEvGA4qVCANo_QAACJlKdI0Vc583.jpg']
        file_name = src
        # 找 images/分隔符，现在地址改了
        # file_name = src.rsplit('images/', maxsplit=1)[0]
        file_name = file_name.split('/')[-1]
        # file_name = src.rsplit('images/', maxsplit=1)[1]
        ret = requests.get(src)
        with open('images/'+file_name, 'wb') as f:
            f.write(ret.content)
        break


get()