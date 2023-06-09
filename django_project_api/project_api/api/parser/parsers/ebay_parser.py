from api.parser.parser import Parser
from bs4 import BeautifulSoup
from logger.logger import *

class EbayParser(Parser):

    @wrap(entering, exiting)
    def parse(self, page):
        """ Parse information from Ebay HTML """

        soup = BeautifulSoup(page, "html.parser")

        ebay_products = []

        all_items = soup.find_all(class_= "s-item s-item__pl-on-bottom")
        
        if len(all_items) == 0:
            all_items = soup.find_all(class_= "s-item__info clearfix")
            
            for item in all_items:  

                try:
                    product = (item.parent.parent.find(class_="s-item__title")).get_text()
                    if product == 'Shop on eBay':
                        continue
                    price = item.parent.parent.find(class_ = "s-item__price").get_text()
                    price = price.replace('USD', '')
                    price = price.replace('MX', '')
                    price = price.replace('$', '')
                    price = price.replace(',', '')
                    price = price.replace('N', '')
                    price = price.replace('COP', '')
                    price = price.replace('MEX', '')
                    price = price.replace('ARS', '')
                    price=(price.split())[0]
                    link_img = (item.parent.parent.find("img"))["src"]
                    link_url = item.parent.parent.find("a")['href']
                    ebay_products.append({
                    "product" : product,
                    "price" : price,
                    "link_img" : link_img,
                    "link_url" : link_url,
                    "origin" : "Ebay"
                    })
                except:
                    pass
            
        for item in all_items:  

            try:
                product = (item.find(class_="s-item__title")).get_text()
                if product == 'Shop on eBay':
                    continue
                price = item.find(class_ = "s-item__price").get_text()
                price = price.replace('USD', '')
                price = price.replace('MX', '')
                price = price.replace('$', '')
                price = price.replace(',', '')
                price = price.replace('N', '')
                price = price.replace('COP', '')
                price = price.replace('MEX', '')
                price = price.replace('ARS', '')
                price=(price.split())[0]
                link_img = (item.find("img"))["src"]
                link_url = item.find("a")['href']
                ebay_products.append({
                "product" : product,
                "price" : price,
                "link_img" : link_img,
                "link_url" : link_url,
                "origin" : "Ebay"
                })
            except:
                pass

        return ebay_products


# def price_validation(self, products):
#         invalid_price_products = []
#         pattern = re.compile(r"\d{1,3}[\s\,\d]\d{1,3}[\s\,\d]\d{1,3}\.\d{1,3}|\d{1,3}\.\d{1,3}|\d{1,3}[\s\,\d]\d{1,3}\.\d{1,3}")
#         for product in products[:]:
#             matches = pattern.findall(product['price'])
#             if matches:
#                 matches = matches[0].replace('\xa0', "")
#                 matches = matches.replace(',', "")
#                 product['price'] = matches
#             else:
#                 invalid_price_products.append(product)
#                 products.remove(product)
