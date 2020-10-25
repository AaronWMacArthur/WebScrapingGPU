import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?d=graphics+cards'

# Opening connection and grabbing HTML
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# does html parsing
page_soup = soup(page_html, "html.parser")

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

# Grabs products
containers = page_soup.findAll("div",{"class":"item-container"})
container = containers[0]

 

for container in containers:
	brand = container.div.div.a.img["title"]


	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping_price = shipping_container[0].text

	print("brand: " + brand)
	print("product_name: " + product_name)
	print("shipping_price: " + shipping_price)

	f.write(brand + "," + product_name.replace(",", "|") + "," + shipping_price + "\n")

f.close()