import scrapy
from ..items import CrawlDataItem


class CrawlSpider(scrapy.Spider):
    name = 'baoDienTu'
    page_number = 2
    start_urls = [
        'https://dantri.com.vn/kinh-doanh/doanh-nghiep/trang-1.htm'
    ]

    def parse(self, response):
        items = CrawlDataItem()
        all_div_quotes = response.css('div.article-content')

        for quotes in all_div_quotes:
            title = quotes.css("h3.article-title a::text").extract()
            url = quotes.css("h3.article-title a::attr(href)").extract()
            description = quotes.css("div.article-excerpt a::text").extract()

            items['title'] = title
            items['url'] = ['https://dantri.com.vn' + url[0]]
            items['description'] = description
            yield items

        next_page = 'https://dantri.com.vn/kinh-doanh/doanh-nghiep/trang-' + str(CrawlSpider.page_number) + '.htm'
        if CrawlSpider.page_number <= 29:
            CrawlSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)


