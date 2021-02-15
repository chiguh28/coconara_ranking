import scrapy
from coconara.items import CoconaraItem
from bs4 import BeautifulSoup


class CoconaraRankingSpider(scrapy.Spider):
    name = 'coconara_ranking'
    allowed_domains = ['coconala.com']
    start_urls = ['https://coconala.com/categories/231?ref=header']

    def parse(self, response):
        title = ''
        sub_title = ''
        price = ''
        user = ''

        soup = BeautifulSoup(response.body,"html.parser")

        job_list = soup.find_all("div",class_="c-searchItemCol c-searchItemColContent")

        for job in job_list:

            title_box = job.find('p',class_='c-searchItemColContentHeader_overview')
            if title_box is not None:
                title = title_box.text.replace('\n','')

            sub_title_box = job.find('h3',class_='c-searchItemColContentHeader_catchphrase')
            if sub_title_box is not None:
                sub_title = sub_title_box.text.replace('\n','')

            price_box = job.find('strong')
            if price_box is not None:
                price = int(price_box.text.replace(',',''))

            user_box = job.find('div',class_='c-searchItemColContentFooterInfoUser_name')
            if user_box is not None:
                # userはspanタグの2つ目に格納されている
                user = user_box.find_all('span')[1].get_text()

            yield CoconaraItem(
                title = title,
                sub_title = sub_title,
                price = price,
                user = user
            )
        
        next_page_block = soup.find('a',class_='pagination-next')
        if next_page_block is None:
            return

        next_link = next_page_block['href']
        next_link = response.urljoin(next_link)

        print(f'next crowling:{next_link}')
        # 次のページをリクエストする
        yield scrapy.Request(next_link,callback=self.parse)
