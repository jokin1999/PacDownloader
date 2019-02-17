#!usr/bin/python3
#coding=UTF-8
print('请稍候...')
url = 'https://raw.githubusercontent.com/petronny/gfwlist2pac/master/gfwlist.pac'
print('载入地址完成')
import urllib.request as urllib
import ssl as ssl
print('载入库完成')
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
print('更新完成!')
input('按回车键退出')
