# coding:utf-8
import urllib.request
import re
from selenium import webdriver
from bs4 import BeautifulSoup


class reqdata(object):
    def requrl(self, url):
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322)')
        with urllib.request.urlopen(req) as response:
            data = response.read()
            htmlstr = data.decode()
            return htmlstr
        return None

    def selsm(self, url):
        driver = webdriver.Chrome()
        try:
            driver.get(url)
            em = driver.find_element_by_id('BIZ_hq_historySearch')
            return em.text
        finally:
            driver.quit()

    # 查找匹配信息
    def beasoaplist(self, url):
        html = reqdata().requrl(url)
        sp = BeautifulSoup(html, 'html.parser')
        imglist = sp.find_all('img')
        srclist = list(map(lambda u: u.get('src'), imglist))
        filter_list = filter(lambda p: p.lower().endswith('.png') or p.lower().endswith('.jpg'), srclist)
        return filter_list

    # 截取图片名
    def getname(self, url):
        pos = url.rfind('/')
        return url[pos + 1:]

    def reg(self, url):
        pattern = r'(http|https)://\S+(?:\.png|\.jpg)'
        return re.match(pattern, url)
