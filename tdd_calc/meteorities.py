from tdd_calc.calc import Calc
import urllib.request
import json


class MeteoriteStats:
    URL = "https://data.nasa.gov/resource/y77d-th95.json"

    def average_mass(self, data):
        c = Calc()
        masses = [float(d['mass']) for d in data if 'mass' in d]

        return c.avg(masses)

    def get_data(self):
        with urllib.request.urlopen(self.URL) as url:
            return json.load(url.read().decode())
