import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.midweststeelsupply.com/store/productlist.php'

# Opening connection and grabbing HTML
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# does html parsing
page_soup = soup(page_html, "html.parser")

filename = "steelproduct.csv"
f = open(filename, "w")

headers = "product\n"

f.write(headers)

# Grabs products
containers = page_soup.findAll("div", {"class": "view view-first"})
container = containers[0]

for container in containers:
    product_container = container.a["title"]
    product_name = product_container

    print("product " + product_name)
    f.write(product_name)

f.close()