from bs4 import BeautifulSoup as bs
import requests
import sys
import json
import urllib2

base_product_url = "http://www.tesco.com/groceries/product/details/?id="
# example id 281814621

sesh = requests.Session()
sesh.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/52.0.2743.116 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8,da;q=0.6'
})

def extract_nutrition(html):
  rows = html.find_all("tr")
  values = [[0 for x in range(3)] for y in range(len(rows))] 

  if (len(rows) == 0):
    return values

  header_row = rows[0]
  headers = header_row.find_all("th")
  values[0][0] = str(headers[0].string)
  values[0][1] = str(headers[1].string)
  values[0][2] = str(headers[2].string)

  for x in range(1, len(rows)):
    row = rows[x]
    row_header = row.find_all("th")
    values[x][0] = str(row_header[0].string)

    row_data = row.find_all("td")
    values[x][1] = str(row_data[0].string)
    values[x][2] = str(row_data[1].string)
  
  return values


def get(product_id):
  # Get web page
  target_url = base_product_url + product_id
  response = sesh.get(target_url)
  soup = bs(response.text, "html.parser")

  name = str(soup.h1.string)
  content_divs = soup.find_all("div", {"class" : "content"})
  nutrition = extract_nutrition(content_divs[3])

  return name, nutrition
