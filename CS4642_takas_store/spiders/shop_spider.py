import scrapy


class RestaurantsSpider(scrapy.Spider):
    name = "shop"
    # count = 0
    urls = [
        'https://takas.lk/electronics-computers/mobile-phones.html?limit=all',
        # 'https://takas.lk/e-tel-f10-sport-mobile-phone.html',
        'https://takas.lk/offers/televisions.html?limit=all&utm_campaign=quicknav&utm_medium=header&utm_source=quicknavbar',
    ]

    def start_requests(self):
        # urls = [
        #     'https://takas.lk/electronics-computers/mobile-phones.html?limit=all',
        #     # 'https://takas.lk/e-tel-f10-sport-mobile-phone.html',
        # ]
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print('...................................................................................')
        # print(response.url)
        # print('...................................................................................')
        if self.urls[0] in response.url or self.urls[1] in response.url:
            # print("-----------------------ok")
            links = response.xpath('//h2[@class="product-name "]/a/@href').extract()
            # print(links)
            for link in links:
                yield scrapy.Request(link, callback=self.parse)
        else:
            # if self.count >= 5:
            #     return
            # self.count = self.count + 1
            title = response.xpath('//div[@class="product-name"]/h1/text()').extract_first()
            availability = response.xpath('//p[@class="availability in-stock"]/span/text()').extract_first()
            price = response.xpath('//span[@class="price"]/text()').extract_first()
            deliveryEstimate = response.xpath('//li[@id="island-delivery"]/text()').extract_first()
            shortDescription = response.xpath('//div[@class="short-description"]/div[@itemprop="description"]/ul/li[position()>=1]/text()').extract_first()
            Description  = response.xpath('//div[@class="box-collateral box-description"]/div/ul/li[position()>=1 and position()<5]/text()').extract()
            warantyType = response.xpath('//li[@data-code="warranty_all_products"]/div[@class="data"]/text()').extract()
            warantyPeriod = response.xpath('//li[@data-code="warranty_length"]/div[@class="data"]/text()').extract()
            color = response.xpath('//li[@data-code="color"]/div[@class="data"]/text()').extract()
            weight = response.xpath('//li[@data-code="weight"]/div[@class="data"]/text()').extract()


            yield {
                'title': title,
                'availability':availability,
                'price':price,
                'deliveryEstimate':deliveryEstimate,
                'shortDescription':shortDescription,
                'Description':Description,
                'warantyType':warantyType,
                'warantyPeriod':warantyPeriod,
                'color':color,
                'weight':weight
            }
            # links = response.xpath('//h2[@class="product-name"]/a/@href').extract()
            # for link in links:
            #     yield scrapy.Request(link, callback=self.parse)

