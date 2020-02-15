import sys
import yaml

from singleton import Singleton


class GlobalParams(dict, metaclass=Singleton):

    def __init__(self):
        super().__init__()
        self.config_path = sys.argv[-1]
        self.update(self.get_yml_file())

    @staticmethod
    def get_yml_file():
        with open(sys.argv[1]) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        return data
