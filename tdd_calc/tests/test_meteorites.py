import pytest

from unittest import mock
from tdd_calc.meteorities import MeteoriteStats


@pytest.fixture(scope='module')
def meteorite_stats():
    m = MeteoriteStats()
    m.get_data = mock.Mock()
    m.get_data.return_value = [
        {
            "fall": "Fell",
            "geolocation": {
                "type": "Point",
                "coordinates": [6.08333, 50.775]
            },
            "id": "1",
            "mass": "21",
            "name": "Aachen",
            "nametype": "Valid",
            "recclass": "L5",
            "reclat": "50.775000",
            "reclong": "6.083330",
            "year": "1880-01-01T00:00:00.000"},
        {
            "fall": "Fell",
            "geolocation": {"type": "Point",
                            "coordinates": [10.23333, 56.18333]
                            },
            "id": "2",
            "mass": "720",
            "name": "Aarhus",
            "nametype": "Valid",
            "recclass": "H6",
            "reclat": "56.183330",
            "reclong": "10.233330",
            "year": "1951-01-01T00:00:00.000"
        }
    ]

    yield m


def test_average_mass(meteorite_stats):
    avgm = meteorite_stats.average_mass(meteorite_stats.get_data())
    
    assert avgm == 370.5
