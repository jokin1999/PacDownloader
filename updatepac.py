#!usr/bin/python3
# -*- coding: utf-8 -*-

import time
import ssl as ssl
import urllib.request as urllib

VERSION = '1.0.1'
print('version: ' + VERSION)
url = 'https://raw.githubusercontent.com/petronny/gfwlist2pac/master/gfwlist.pac'
# 关闭证书验证
ssl._create_default_https_context = ssl._create_unverified_context
print('获取网络数据中...')
response = urllib.urlopen(url)
pac = response.read().decode('UTF-8')
print('写入本地数据中...')
try:
    with open('pac.txt', 'r+') as f:
        bak = f.read()
except Exception:
    bak = False
if (bak is not False):
    with open('pac.txt.bak', 'w+') as f2:
        f2.write(bak)
with open('pac.txt', 'w+') as f:
    f.write(pac)
print('更新完成，3秒后退出！')
time.sleep(3)
