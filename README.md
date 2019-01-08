### project name: yyscbg spider

---

##### point

- Sell list crawl, including the item's serverid and game_ordersn.

- According to the serverid and game_ordersn, into the detail site，crawl account details.

- Further data analysis, then try to design ZY-Mirror.

##### some api we konw

[Account List](https://yys.cbg.163.com/cgi/api/role_search?view_loc=all_list&order_by=selling_time%20DESC&page={page_num})
[Product Details](https://yys.cbg.163.com/cgi/api/get_equip_detail/serverid={serverid}&ordersn={game_ordersn}&view_loc=all_list%EF%BC%9B1)

##### first: create proxy pool

- refer [proxy_pool](https://github.com/jhao104/proxy_pool)