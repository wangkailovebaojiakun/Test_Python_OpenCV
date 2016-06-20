#coding:utf-8
import urllib

def getbaidu(a,b,c):
    """call back fun 
    @a:downloaded blok
    @b:size of block
    @c:size of far file
    """
    per = 100.0 * a * b / c
    if per>100:
         per = 100
    print '%.2f%%' %per

url = 'http://www.baidu.com'
local = "/home/wk/WORKSPACE/Python-TEST/Python-Bug/baidu.html"
urllib.urlretrieve(url,local,getbaidu)
