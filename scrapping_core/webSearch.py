from scrapping_core.scrap import Scrap
from flask import jsonify


class WebSearch:
    def __init__(self, sites):
        self.__sites = sites

    def search(self, query):
        results = []
        for site in self.__sites:
            # if site == 'Kabum':
            #     continue
            page = Scrap(site)
            page = page.get_instance()
            res = page.search(query)
            if site == 'Kabum' and res['content']['props']['pageProps']['data']['catalogServer']['data']:
                items = res['content']['props']['pageProps']['data']['catalogServer']['data']
                items_formatted = []
                for item in items:
                    items_formatted.append({
                        "nome_item": item['name'],
                        "valor_item": item['price'],
                        "valor_c_desconto": item['priceWithDiscount'],
                        "description": item['description'],
                        "link": f"{page.url}/produto/{item['code']}/{item['friendlyName']}"
                    })
                results.append({"Kabum": {"items": items_formatted}})
            elif site == 'Oficinadosbits':
                items_formatted = []
                for index, product in enumerate(res['content']):
                    product_id = f"widget_tools__product_detail_list_{index + 1}"
                    product_detail_list = product.find('div', id=product_id)
                    items_formatted.append({
                        "nome_item": product.find('a', class_='link-name').get_text(strip=True),
                        "valor_item": float(product_detail_list.get('data-preco-de').replace(".", "").replace(",", ".")),
                        "valor_c_desconto": float(product_detail_list.get('data-preco-por').replace(".", "").replace(",", ".")),
                        "description": product.find('a', class_='link-name').get_text(strip=True),
                        "link": f"{page.url}{product.find('figure', class_='container_general').find('a').get('href')}"
                    })
                results.append({"OficinaDosBits": {"items": items_formatted}})
            else:
                results.append([f"{site}: failed"])

        return results
