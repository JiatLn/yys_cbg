import re
import sys
import requests
import time
from lxml import etree




def freeProxy():
    """
    快代理 https://www.kuaidaili.com
    :return: proxy_list
    """
    url_list = [
        'https://www.kuaidaili.com/free',
        'https://www.kuaidaili.com/free/inha/2/',
        'https://www.kuaidaili.com/free/inha/3/'
    ]
    proxy_list = []
    try:
        for url in url_list:
            html_tree = getHtmlTree(url)
            ip_list, port_list = html_tree.xpath('//td[@data-title="IP"]'), html_tree.xpath('//td[@data-title="PORT"]')
            for ip, port in zip(ip_list, port_list):
                proxy_list.append('{}:{}'.format(ip.text, port.text))
    except Exception as e:
        pass
    return proxy_list


def getHtmlTree(url):
    """
    获取html树
    :param url:
    :param kwargs:
    :return:
    """



    # delay 2s for per request
    time.sleep(2)

    html = requests.get(url=url).content
    return etree.HTML(html)


def valVer(proxies):
    header = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }
    try:
        requests.get('http://wenshu.court.gov.cn/')
    except:
        print('connect failed')
        return 0
    else:
        print('proxies success')
        return 1



if __name__ == '__main__':
    print(getHtmlTree('https://www.kuaidaili.com/free/').xpath('//td[@data-title="IP"]')[0].text)
    print(freeProxy())