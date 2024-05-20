import importlib
import scrapping_core.kabum
import scrapping_core.oficinadosbits


class Scrap:
    def __init__(self, class_name):
        self.module = importlib.import_module('scrapping_core')
        self.instance = None

        try:
            cls = getattr(self.module, class_name.lower())
            if hasattr(cls, class_name):
                self.instance = getattr(cls, class_name)()
        except ImportError as e:
            print(f"Could not import module scrapping_core: {e}")

    def get_instance(self):
        if self.instance is not None:
            return self.instance
        else:
            return False
