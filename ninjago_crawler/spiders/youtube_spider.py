from ninjago_crawler.items import VideoItem
import scrapy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class YoutubeSpider(scrapy.Spider):
    name = "youtube"
    allowed_domains = ["youtube.com"]
    start_urls = [
        "https://www.youtube.com/playlist?list=PLE_OfiulStStgPQ3MtbYIyisMyNjGGyh-"
    ]

    def parse(self, response):
        data_list = response.xpath('//tr[@class="pl-video yt-uix-tile "]')

        for data in data_list:
            video = VideoItem()
            video['title'] = data.xpath('.//td[@class="pl-video-title"]/a/text()')[0].extract().replace('\n', '')
            video['video_id'] = data.xpath('.//@data-video-id')[0].extract()
            video['thumbnail_url'] = 'http://i.ytimg.com/vi/%s/default.jpg' % video['video_id']
            video['minute'] = data.xpath('.//td[@class="pl-video-time"]/div/div/span/text()')[0].extract()
            #http://i.ytimg.com/vi/9WHv9Nf9WAA/default.jpg
            yield video
