import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http://example.com']

    def parse(self, response):
        # XPath 사용
        element = response.xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]')
        if element:
            self.log(f"Element found: {element.get()}")
        else:
            self.log("Element not found")

        # 또는 CSS 선택자 사용
        element_css = response.css('div.some_class div.another_class::text').get()
        if element_css:
            self.log(f"Element found with CSS: {element_css}")
        else:
            self.log("Element not found with CSS")