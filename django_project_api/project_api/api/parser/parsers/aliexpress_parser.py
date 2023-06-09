from api.parser.parser import Parser
from bs4 import BeautifulSoup
from logger.logger import *

class AliexpressParser(Parser):

    @wrap(entering, exiting)
    def parse(self, page):
        """ Parse information from Aliexpress HTML """
        
        soup = BeautifulSoup(page, "html.parser")
        
        aliexpress_products = []
        
        all_items = soup.find_all(class_ = "_3t7zg _2f4Ho")
        
        if len(all_items) == 0:
            all_items = soup.find_all(class_ = "_3GR-w")
        
            for item in all_items:  

                try:
                    product = (item.parent.find(class_="_18_85")).get_text()
                    price_all = item.parent.find(class_ = "mGXnE _37W_B")
                    price_items = price_all.find_all('span')
                    price = str(price_items[1].get_text())+str(price_items[2].get_text())+str(price_items[3].get_text())
                    price = price.replace('.', '')
                    price = price.replace(',', '.')
                    link_img = "https:" + (item.parent.find("img"))["src"]
                    link_url = "https:" + item.parent['href']
                    aliexpress_products.append({
                    "product" : product,
                    "price" : price,
                    "link_img" : link_img,
                    "link_url" : link_url,
                    "origin" : "Aliexpress"
                    })
                except:
                    pass


        for item in all_items: 

            try:
                product = (item.find(class_="_18_85")).get_text()
                price_all = item.find(class_ = "mGXnE _37W_B")
                price_items = price_all.find_all('span')
                price = str(price_items[1].get_text())+str(price_items[2].get_text())+str(price_items[3].get_text())
                price = price.replace('.', '')
                price = price.replace(',', '.')
                link_img = "https:" + (item.find("img"))["src"]
                link_url = "https:" + item['href']
                aliexpress_products.append({
                "product" : product,
                "price" : price,
                "link_img" : link_img,
                "link_url" : link_url,
                "origin" : "Aliexpress"
                })
            except:
                pass

        return aliexpress_products
