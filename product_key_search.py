from bs4 import BeautifulSoup as bs
import requests
import json

PER_PAGE = 20

tesco_url = "http://www.tesco.com/groceries/product/browse/default.aspx?N=4294793657&Ne=4294793660"
page_appendage = "&=&Nao="

page1 = "http://www.tesco.com/groceries/product/browse/default.aspx?N=4294793657&Ne=4294793660&=&Nao=0"
page2 = "http://www.tesco.com/groceries/product/browse/default.aspx?N=4294793657&Ne=4294793660&=&Nao=20"

sesh = requests.Session()
sesh.headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
})


def get_page_urls(item_count):

    page_urls_ = []
    for i in range(0, item_count/PER_PAGE):
        page_urls_.append(tesco_url + page_appendage + str(i*PER_PAGE))

    return page_urls_


def get_product_ids(urls):

    product_ids = []

    for url in urls:
        response_ = sesh.get(url)
        soup_ = bs(response_.text, "html.parser")

        product_data = soup_.find_all(attrs={"name": "productdata"})

        product_list = product_data[0]['content'].encode('utf-8').split("|")

        for index in range(len(product_list)-1):
            product_json = json.loads(product_list[index])
            product_ids.append(product_json['productId'])

    return product_ids


def get_ids(base_product_url):

    response = sesh.get(base_product_url)
    soup = bs(response.text, "html.parser")

    total_item_count = int(soup.find_all("span", {"class": "pageTotalItemCount"})[0].text)

    page_urls = get_page_urls(total_item_count)
    ids = get_product_ids(page_urls)

    return ids





