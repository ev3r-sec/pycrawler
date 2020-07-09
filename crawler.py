#!/usr/bin/env python
#-*- coding:utf-8 -*-
#author: ev3r

import requests
import re
from bs4 import BeautifulSoup
import argparse
s = requests.session()

url = "http://www.baidu.com"

wordlist = []

depthneed = 2

def findtext(url, keyword, depth):
    global wordlist
    response = s.get(url)
    htmlpage = response.text
    soup = BeautifulSoup(htmlpage, features="lxml")
    apage = soup.findAll('a')
    word = soup.findAll(keyword)
    for i in word:
        wordcontent = i.get_text()
        wordlist.append(wordcontent)
    wordlist = list(set(wordlist))

    try:
        urllist = [i['href'] for i in apage if i['href'][0] != 'j']
        if len(urllist) and depth < depthneed:
            for urll in urllist:
                findtext(urll, keyword, depth+1)
    except:
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str)
    parser.add_argument("keyword", type=str)
    parser.add_argument("depth", type=int)
    args = parser.parse_args()
    #  f = re.findall(c.text, urlre)
    depthneed = args.depth
    try:
        findtext(args.url, args.keyword, 0)
        print(wordlist)
        #  for i in wordlist:
            #  print(i.decode())
    
    except:
        pass
