from bs4 import BeautifulSoup
import requests
import scrapping_core.scrapAbstract as scrapAbstract
import json


class Pichau(scrapAbstract.Base):
    def __init__(self):
        self.url = 'https://www.kabum.com.br/busca/'
        self.contents = []

    def search(self, query):
        if not query:
            return False
        res = requests.get(f"{self.url}{query}")
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
        return content

    def __format_contents(self, content):
        if content is None or content == '':
            return '{}'

        return json.loads(content)
