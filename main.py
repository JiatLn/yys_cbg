import sys
from random import randint
from time import sleep


from proxy_pool.FreeProxy import freeProxy, valVer
from yys_cbg import get_serverid_and_game_ordersn


detail_url = 'https://yys.cbg.163.com/cgi/api/get_equip_detail'



if __name__ == '__main__':
    # 账号列表
    items = []
    # 免费代理列表
    # freeProxy_list = freeProxy()
    # 爬n次
    n = 1000
    page = 0
    for i in range(0, n):
        # 随机取一个ip地址
        # print('使用代理', freeProxy_list[i])
        # proxies = {
        #     'http': 'http://' + freeProxy_list[i],
        #     'https': 'https://' + freeProxy_list[i]
        # }
        items += get_serverid_and_game_ordersn(i + 1)
        print('已爬取了%d条记录..' % len(items))
        if len(items) == 45:
            with open('/output/items-%d.txt' % page, 'a') as f:
                f.write(str(items))
                page += 1
                items = []
                print("Let me sleep for 300 seconds.")
                sleep(300)


