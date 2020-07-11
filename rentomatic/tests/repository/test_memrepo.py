import pytest
import uuid

from rentomatic.domain.room import Room
from rentomatic.repository.memrepo import MemRepo


@pytest.fixture(scope='module')
def room_dicts_factory():
    def _room_dict(size, price, longitude, latitude, code=uuid.uuid4()):
        return {
            'code': code,
            'size': size,
            'price': price,
            'longitude': longitude,
            'latitude': latitude
        }

    yield _room_dict


@pytest.fixture(scope='module')
def rooms_dicts(room_dicts_factory):
    room_1 = room_dicts_factory(size=215, price=39, longitude=-0.09998975,
                                latitude=51.75436293)
    room_2 = room_dicts_factory(size=405, price=66, longitude=0.18228006,
                                latitude=51.74640997)
    room_3 = room_dicts_factory(size=56, price=60, longitude=0.27891577,
                                latitude=51.45994069)
    room_4 = room_dicts_factory(size=93, price=48, longitude=0.33894476,
                                latitude=51.39916678)

    return [room_1, room_2, room_3, room_4]


def test_repository_list_without_parameters(rooms_dicts):
    repo = MemRepo(rooms_dicts)
    rooms = [Room.from_dict(i) for i in rooms_dicts]

    assert repo.list() == rooms
