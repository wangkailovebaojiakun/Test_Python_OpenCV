#coding:utf-8
import re
import urllib
import cv2

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
#get image
def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist
#save image
def saveImg(imglist):

    local = "/home/wk/WORKSPACE/Python-TEST/Python-Bug/getimg"
    x = 0
    for imgurl in imglist:
        filename = local +str(x) +".jpg"
        print filename
        urllib.urlretrieve(imgurl,filename)
        x+=1

html = getHtml("http://tieba.baidu.com/p/4530493052")
saveImg(getImg(html))
