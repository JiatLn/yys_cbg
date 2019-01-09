import json
import requests
import math
import pickle
from time import sleep
import time




game_ordersn = "201812101501616-10-Z4LTRHR8OE9WH"
serverid = 10

detail_url = 'https://yys.cbg.163.com/cgi/api/get_equip_detail'
headers = {
    'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
    'Accept - Encoding':'gzip, deflate',
    'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
    'Connection':'Keep-Alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host':'zhannei.baidu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
}
data = 'serverid={serverid}&ordersn={game_ordersn}&view_loc=all_list%EF%BC%9B1'
body = data.format(game_ordersn=game_ordersn,serverid=serverid)


# def get_detail_json(serverid, game_ordersn):
#     detail_url = 'https://yys.cbg.163.com/cgi/api/get_equip_detail'
#     data = 'serverid={serverid}&ordersn={game_ordersn}&view_loc=all_list%EF%BC%9B1'
#     body = data.format(game_ordersn=game_ordersn,serverid=serverid)
#     try:
#         response = requests.post(detail_url, data=body, headers=headers)
#         print(type(response.text))
#         if response:
#             json_obj = json.loads(response.text, encoding='utf-8')
#             # print(json_obj)
#             # 先保存，后续再解析
#             # parse_detail(json_obj)
#             # equip_desc_obj = json.loads(json_obj['equip']['equip_desc'])
#             with open('%s.txt' % game_ordersn, 'a') as f:
#                 f.write(str(json_obj))
#                 print("Let me sleep for 300 seconds.")
#                 sleep(300)
#     except Exception as e:
#         print('页面请求出错', str(game_ordersn))
#         raise e


def get_detail_json(body):
    try:
        filename = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        response = requests.post(detail_url, data=body, headers=headers)
        # print(response.text)
        if response:
            json_obj = json.loads(response.text, encoding='utf-8')
            # 先保存，后续再解析
            # parse_detail(json_obj)
            # equip_desc_obj = json.loads(json_obj['equip']['equip_desc'])
            print(body)
            with open('output_json/%s.json' % filename, 'w') as f:
                json.dump(json_obj, f)
                print('save at output_json/%s.json' % filename)
    except Exception as e:
        print('页面请求出错', str(game_ordersn))
        raise e


def get_serverid_and_game_ordersn(page_num):
    items = []
    url = 'https://yys.cbg.163.com/cgi/api/role_search?view_loc=all_list&order_by=selling_time%20DESC&page=' + str(page_num)
    print('正在抓取第%d页...'% page_num)
    # while len(items) == 0:
        # try:

    response = requests.get(url, timeout=10, headers=headers)
    if response:
        json_obj = json.loads(response.text)
        # print(json_obj)
        # totalNum = json_obj['total_num']
        # pageNum = math.ceil(totalNum / 15)
        parse_index(json_obj, items)
    else:
        print('page of', page_num, ' is none')
        # except Exception as e:
        #     print("Connection refused by the server..")
        #     print("Let me sleep for 3 seconds")
        #     print("ZZzzzz...")
        #     sleep(3)
        #     print("Was a nice sleep, now let me continue...")
        #     continue
    # response = requests.get(url, timeout=10)    # 不使用代理
    print("Let me sleep for 60 seconds.")
    sleep(60)
    return items




def parse_index(json_obj, items):
    # items is a list of (serverid, game_ordersn)
    for data in json_obj['result']:
        serverid = data['serverid']
        game_ordersn = data['game_ordersn']
        items.append((serverid, game_ordersn))
    return items



if __name__ == '__main__':
    items = []
    for i in range(1, 11):
        items = get_serverid_and_game_ordersn(i, items)
    print(items)