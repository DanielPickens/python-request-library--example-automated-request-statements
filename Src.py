import requests
response = requests.get('https://www.whateveryouwant.com') print(response)


We can then use this result to create a decision-making function, where a 200 status code means the page is available but a 404 means the page is not found.

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')



Using scrapy:

class SuperSpider(CrawlSpider):
   name = 'extractor'
   allowed_domains = ['www.good.com']
   start_urls = ['https://www.yeah.com/knowledge/technical-seo-library/']
   base_url = 'https://www.yoyo.com'
   def parse(self, response):
       for link in response.xpath('//div/p/a'):
           yield {
               "link": self.base_url + link.xpath('.//@href').get()
           }

#Within Scrapy, you can define a number of instructions such as the name of the domain you would like to crawl, the start URL, and certain page folders the spider is allowed or not allowed to crawl.

Scrapy can be used to extract all of the links on a certain page and store them in an output file, for example.
