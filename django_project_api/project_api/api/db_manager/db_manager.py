from api.models import Product, Search
from django.utils import timezone
import datetime

DAYS_TO_UPDATE = 4

class DbManager(object):
    def find_term(self, search_term):
        search = Search.objects.filter(name=search_term)
        if len(search) > 0:
            return search
        else:
            return False

    def term_up_today(self, search):
        time_threshold = datetime.datetime.now(tz=timezone.utc) - datetime.timedelta(DAYS_TO_UPDATE)
        search = list(search.filter(created_at__range = [time_threshold, datetime.datetime.now(tz=timezone.utc)]).values())
        if len(search) > 0:
            return search
        else:
            return False

    def find_products(self, search):
        all_products=[]
        ebay_products=[]
        amazon_products=[]
        ali_products=[]
        if search:
            if len(search) > 0:
                products = list(Product.objects.filter(search=search[0]['id']).values())
                
                for p in products:
                    if p['origin'] == 'Ebay':
                        ebay_products.append({'product':p['product'],'price':p['price'], 'link_img':p['link_img'], 'link_url': p['link_url'], 'origin':p['origin']})
                    elif p['origin'] == 'Aliexpress':
                        ali_products.append({'product':p['product'],'price':p['price'], 'link_img':p['link_img'], 'link_url': p['link_url'], 'origin':p['origin']})
                    else:
                        amazon_products.append({'product':p['product'],'price':p['price'], 'link_img':p['link_img'], 'link_url': p['link_url'], 'origin':p['origin']})
                if len(amazon_products) > 0:
                    all_products.append(amazon_products)
                if len(ebay_products) > 0:
                    all_products.append(ebay_products)
                if len(ali_products) > 0:
                    all_products.append(ali_products)
                datos = all_products
            else:
                datos=all_products
            return datos
        else:
            datos={'message': 'Error, no argument passed'}
            return datos

    def delete_search(self, search_term):
        search = list(Search.objects.filter(name=search_term))
        if len(search) > 0:
            Search.objects.filter(name=search_term).delete()
            datos={'message':"success"}
        else:
            datos={'message':  'search term not found'}
        return datos

    def create(self, products, search_term):
        all_products = []
        if len(products) > 0:
            for p in products:
                all_products.extend(p)
        if len(all_products) > 0:
            search = Search.objects.create(name=search_term)
            for p in all_products:
                prod = Product.objects.create(
                    product = p['product'],
                    price = (p['price']),
                    link_img = p['link_img'],
                    link_url = p['link_url'],
                    origin = p['origin'],
                    search = search
                )
            datos={'message':"success"}
        else:
            datos={'message':  'No items passed'}
        return datos
        

