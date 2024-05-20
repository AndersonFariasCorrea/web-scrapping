from bs4 import BeautifulSoup
import requests
# import scrapping_core.scrapAbstract as scrapAbstract
import json


class Kabum:
    def __init__(self):
        self.url = 'https://www.kabum.com.br'
        self.contents = []

    def search(self, query):
        if not query:
            return False
        res = requests.get(f"{self.url}/busca/{query}")
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
        content = soup.find(id="__NEXT_DATA__")
        if content:
            return self.__format_contents(content.text)
        else:
            return ''

    def __format_contents(self, content):
        if content is None or content == '':
            return '{}'

        return json.loads(content)
