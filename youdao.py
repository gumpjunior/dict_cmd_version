#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import sys
from urllib import urlencode
from pyquery import PyQuery as pq
 
 
base_url = r'http://dict.youdao.com/search?'
 
 
def search(q):
    url = base_url + urlencode({'q': q})
    html = pq(url)
    results = html('div#phrsListTab')
    print '[ %s ]' % q
    for li in results('li'):
        print li.text
    print '------------------------------------\n'
 
 
def main():
    if len(sys.argv) < 2:
        print 'Usage: python youdao.py [word] [word1] ...'
        sys.exit(0)
 
    for q in sys.argv[1:]:
        search(q)
 
 
if __name__ == '__main__':
    main()