# _*_ coding:utf-8 _*_
import requests
import re


class weblib(object):
    def download(self, url):
        if url is None:
            return None
        user_agent = "Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)"
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None

    def parser_url(self, page_url, response):
        pattern = re.compile(r'((\d+)/)')
        urls = pattern.findall(response)
        if urls is not None:
            return list(set(urls))
        return None
