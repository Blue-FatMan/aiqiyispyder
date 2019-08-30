import scrapy
from movie.items import MovieItem

class PanjueshuSpider(scrapy.Spider):
    name='aiqiyi'
    allowed_domains=['iqiyi.com']
    # start_urls=['http://www.iqiyi.com']

    def start_requests(self):
        url = 'http://list.iqiyi.com/www/1/----------2---11-1-1-iqiyi--.html'
        yield scrapy.Request(url=url, callback=self.get_link)


    def get_link(self,response):
        print('-------------------------------')
        # print(response.text)
        links = response.xpath('/html/body/div[@class="mod-page"]/a/@href').extract()
        # print(len(links))
        # print(links)
        for url in links[:2]:
            yield scrapy.Request(url=response.urljoin(url), callback=self.get_movelink)


    def get_movelink(self,response):
        item = MovieItem()
        obj = response.xpath('/html/body/div[3]/div/div/div[3]/div/ul/li')
        for sel in obj:
            title = sel.xpath('div[2]/div[1]/p/a/text()').extract()
            href = sel.xpath('div[2]/div[1]/p/a/@href').extract()
            mainpeople = sel.xpath('div[2]/div[2]/em/a/text()').extract()
            # print (hrefs)
            item["title"] = title[0]
            item["mainpeople"] = ','.join([x.replace('\r\n', '').strip() for x in mainpeople])
            item["url"] = ''.join(href).strip().split('#')[0]
            # print(response.url)
            # print(title)
            # print(href)
            yield item