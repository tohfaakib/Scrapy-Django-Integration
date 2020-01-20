# -*- coding: utf-8 -*-
import scrapy
from scraper.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        for quote_tag in response.css('div.quote'):
            quote = quote_tag.css('span.text::text').get()
            author = quote_tag.xpath('span/small/text()').get()
            tags = quote_tag.css('a.tag::text').extract()
            tags = ", ".join([str(x) for x in tags])

            item = QuotesItem()

            item['quote'] = quote
            item['author'] = author
            item['tags'] = tags

            yield item

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page)
