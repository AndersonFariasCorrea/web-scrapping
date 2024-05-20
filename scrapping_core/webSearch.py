from scrapping_core.scrap import Scrap


class WebSearch:
    def __init__(self, sites):
        self.__sites = sites

    def search(self, query):
        results = []
        for site in self.__sites:
            page = Scrap(site)
            page = page.get_instance()
            res = page.search(query)
            if res.status_code == 200:
                results.append(res)
            else:
                results.append([f"{site}: failed"])

        return results
