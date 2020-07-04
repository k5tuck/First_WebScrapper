from urllib.request import urlopen as uopen
from bs4 import BeautifulSoup as soup
import time

graphicurl = "https://www.newegg.com/p/pl?N=100007709%20600030348&page=1"
cpuurl = "https://www.newegg.com/Processors-Desktops/SubCategory/ID-343?Tid=7671"

#Opening GPU site, reading contents, closing site
graphic = uopen(graphicurl)
graphicread = graphic.read()
graphic.close()

#Parsing site to HTML
graphic_soup = soup(graphicread, "html.parser")

#Grabs Product
gcontainers = graphic_soup.findAll("div", {"class": "item-container"})
gcontainer = gcontainers[0]

#Names and Opens File
Gfilename = "GPU Products.csv"
gf = open(Gfilename, "w")

headers = "Brand, Product_name, Price, Shipping_Fee\n"

gf.write(headers)

for gcontainer in gcontainers:
    gbrand = gcontainer.div.div.a.img["title"]
    
    gtitle = gcontainer.findAll("a", {"class":"item-title"})
    gname = gtitle[0].text

    price = gcontainer.findAll("li", {"class": "price-current"})
    dollar = price[0].strong.text
    cents = price[0].sup.text
    #if dollar == 
    currentprice = dollar + cents
    #currentprice = float(currentprice)
    
    shipping = gcontainer.findAll("li", {"class": "price-ship"})
    shippingprice = shipping[0].text.strip()

    print("Brand: " + gbrand)
    print("Name: " + gname)
    print("Price: " + currentprice)
    print("Shipping Fee: " + shippingprice)

    gf.write(gbrand + "," + gname.replace(",", "|") + "," + currentprice.replace(",", " ") + "," + shippingprice + "\n")

    #Moves to Next Page
    #next_button = graphic_soup.find("button", {"class": "btn"}, {"title": "Next"})
    #next_page = next_button
    #time.sleep(4)
    #graphicurl = next_page
    #graphic = uopen(graphicurl)
    #graphicread = graphic.read()
    #graphic.close()
    #graphic_soup = soup(graphicread, "html.parser")
gf.close()


#Opening CPU site, reading contents, closing site
cpu = uopen(cpuurl)
cpuread = cpu.read()
cpu.close()

#Parsing site to HTML
cpu_soup = soup(cpuread, "html.parser")

#Grabs Product
ccontainers = cpu_soup.findAll("div", {"class": "item-container"})
ccontainer = ccontainers[0]

#Names and Opens File
Cfilename = "CPU Products.csv"
cf = open(Cfilename, "w")

headers = "Brand, Product_name, Price, Shipping_Fee\n"

cf.write(headers)

for ccontainer in ccontainers:
    cbrand = ccontainer.div.div.a.img["title"]

    ctitle = ccontainer.findAll("a", {"class": "item-title"})
    cname = ctitle[0].text

    price = ccontainer.findAll("li", {"class": "price-current"})
    dollar = price[0].strong.text
    cents = price[0].sup.text
    currentprice = dollar + cents
    #currentprice = float(currentprice)

    shipping = ccontainer.findAll("li", {"class": "price-ship"})
    shippingprice = shipping[0].text.strip()

    print("Brand: " + cbrand)
    print("Name: " + cname)
    print("Price: " + currentprice)
    print("Shipping Fee: " + shippingprice)

    cf.write(cbrand + "," + cname.replace(",", "|") + "," + currentprice.replace(",", " ")  + "," + shippingprice + "\n")

    #Moves to Next Page
    #next_button = graphic_soup.find("button", {"class": "btn"}, {"title": "Next"})
    #next_page = next_button
    #time.sleep(4)
    #graphicurl = next_page
    #graphic = uopen(graphicurl)
    #graphicread = graphic.read()
    #graphic.close()
    #graphic_soup = soup(graphicread, "html.parser")
cf.close()
