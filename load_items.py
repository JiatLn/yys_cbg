import re

def load_bodys(page_num):
    bodys = []
    with open('output/items-%d.txt' % page_num, 'r') as f:
        p1 = re.compile(r'[(](.*?)[)]', re.S)
        items = re.findall(p1, f.read())
        for item in items:
            serverid, game_ordersn = item.split(',')[0], item.split(',')[1][2:-1]
            data = 'serverid={serverid}&ordersn={game_ordersn}&view_loc=all_list%EF%BC%9B1'
            body = data.format(game_ordersn=game_ordersn, serverid=serverid)
            bodys.append(body)
    # print(bodys)
    return bodys




if __name__ == '__main__':
    print(load_items(1)[0])