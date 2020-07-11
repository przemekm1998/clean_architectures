import pytest
import uuid
from rentomatic.domain.room import Room


@pytest.fixture(scope='module')
def room_dict():
    def _room_dict(code):
        room_dict = {'code': code,
                     'size': 200,
                     'price': 10,
                     'longitude': -0.09998975,
                     'latitude': 51.7546293}
        return room_dict

    return _room_dict


def test_room_model_init():
    code = uuid.uuid4()
    room = Room(code, size=200, price=10, longitude=-0.09998975, latitude=51.7546293)

    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09998975
    assert room.latitude == 51.7546293


def test_room_model_from_dict(room_dict):
    code = uuid.uuid4()
    room = Room.from_dict(room_dict(code))

    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09998975
    assert room.latitude == 51.7546293


def test_room_model_to_dict(room_dict):
    code = uuid.uuid4()
    rd = room_dict(code)
    room = Room.from_dict(rd)

    assert room.to_dict() == rd


def test_room_model_comparison(room_dict):
    code = uuid.uuid4()
    rd = room_dict(code)
    room1 = Room.from_dict(rd)
    room2 = Room.from_dict(rd)

    assert room1 == room2
