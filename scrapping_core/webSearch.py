from scrapping_core.scrap import Scrap


class WebSearch:
    def __init__(self, sites):
        self.__sites = sites

    def search(self, query):
        results = []
        for site in self.__sites:
            if site == 'Oficinadosbits':
                continue
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
            elif site == 'Pichau':
                print(res)
            else:
                results.append([f"{site}: failed"])

        return results
