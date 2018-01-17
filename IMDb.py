#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-01-16 13:28:57
# Project: IMDb

from pyspider.libs.base_handler import *
import re


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.imdb.com/search/title?count=100&title_type=feature,tv_series,tv_movie&ref_=nv_ch_mm_2',
                   callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('* h3[class] a[href]').items():
            self.crawl(each.attr.href, callback=self.detail_page)
        for i in response.doc('div[class="desc"] a[class="lister-page-next next-page"]').items():
            self.crawl(i.attr.href, callback=self.index_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('h1[itemprop]').text(),
            "Director": response.doc('span[itemprop="director"] a').text(),
            "Starts": response.doc("span[itemprop='actors'] a").text(),
            "XXXX": response.doc("span[itemprop='actors']").html(),
        }
