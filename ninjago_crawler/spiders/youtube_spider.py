import scrapy

class YoutubeSpider(scrapy.Spider):
    name = "youtube"
    allowed_domains = ["youtube.com"]
    start_urls = [
        "https://www.youtube.com/playlist?list=PLE_OfiulStStgPQ3MtbYIyisMyNjGGyh-"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
