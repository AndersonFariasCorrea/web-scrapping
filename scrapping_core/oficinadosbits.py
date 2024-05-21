from bs4 import BeautifulSoup
import requests
import json


class Oficinadosbits:
    def __init__(self):
        self.url = 'https://www.oficinadosbits.com.br'
        # self.url = 'https://patoloco.com.br'
        self.contents = []

    def search(self, query):
        if not query:
            return False
        # res = requests.get(f"{self.url}/busca/?buscar-por={query}")
        res = requests.get(f"{self.url}/produto/busca/?q={query}&submit=")
        if res.status_code == 200:
            return {
                'status': res.status_code,
                'content': self.get_contents(res)
            }
        else:
            return {
                'status': res.status_code,
                'content': f"{self.__class__.__name__}: failed"
            }

    def get_contents(self, request_result):
        soup = BeautifulSoup(request_result.content, 'html.parser')
        content = soup.find_all('li', class_='product-item')
        available_products = []
        for product in content:
            if 'unavailable' not in product.get('class', []):
                available_products.append(product)
        return self.__format_contents(available_products)

    def __format_contents(self, content):
        if content is None or content == '':
            return []
        return content
