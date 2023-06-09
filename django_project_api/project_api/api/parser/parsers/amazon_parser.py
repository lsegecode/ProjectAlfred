from api.parser.parser import Parser
from bs4 import BeautifulSoup
from logger.logger import *

class AmazonParser(Parser):
    
    @wrap(entering, exiting)
    def parse(self, page):
        """ Parse information from Amazon HTML """
        soup = BeautifulSoup(page, "html.parser")
        
        amazon_products = []

        all_items = soup.find_all(attrs = {'data-component-type':"s-search-result"})

        if len(all_items) == 0:
            
            all_items = soup.find_all(class_ = "s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin s-latency-cf-section s-card-border")
            
            for item in all_items:  

                try:
                    product = (item.parent.parent.parent.find(attrs= {"class" : ["a-size-base-plus a-color-base a-text-normal","a-size-mini a-color-base a-text-normal","a-size-base-mini a-color-base a-text-normal","a-size-base a-color-base a-text-normal", "a-size-medium a-color-base a-text-normal"]})).get_text()
                    price = str(item.parent.parent.parent.find("span", {'class' : "a-price-whole"}))+str(item.find(class_="a-price-fraction"))
                    price = price.replace('<span class="a-price-decimal">', '')
                    price = price.replace('<span class="a-price-whole">', '')
                    price = price.replace('<span class="a-price-fraction">', '')
                    price = price.replace('</span>', '')
                    price = price.replace(',', '')
                    if price == 'NoneNone':
                        continue
                    link_img = (item.parent.parent.parent.find("img"))["src"]
                    link_url = "https://www.amazon.com" + item.parent.parent.parent.find("a", class_ = "a-link-normal s-no-outline", href = True)['href']
                    amazon_products.append({
                    "product" : product,
                    "price" : price,
                    "link_img" : link_img,
                    "link_url" : link_url,
                    "origin" : "Amazon"
                    })
                except:
                    pass
        
        for item in all_items:  

            try:
                product = (item.find(attrs= {"class" : ["a-size-base a-color-base a-text-normal", "a-size-mini a-color-base a-text-normal", "a-size-base-mini a-color-base a-text-normal","a-size-base-plus a-color-base a-text-normal", "a-size-medium a-color-base a-text-normal"]})).get_text()
                price = str(item.find("span", {'class' : "a-price-whole"}))+str(item.find(class_="a-price-fraction"))
                price = price.replace('<span class="a-price-decimal">', '')
                price = price.replace('<span class="a-price-whole">', '')
                price = price.replace('<span class="a-price-fraction">', '')
                price = price.replace('</span>', '')
                price = price.replace(',', '')
                if price == 'NoneNone':
                        continue
                link_img = (item.find("img"))["src"]
                link_url = "https://www.amazon.com" + item.find("a", class_ = "a-link-normal s-no-outline", href = True)['href']
                amazon_products.append({
                "product" : product,
                "price" : price,
                "link_img" : link_img,
                "link_url" : link_url,
                "origin" : "Amazon"
                })
            except:
                pass

        return amazon_products
