import json
import uuid
import pytest

from rentomatic.serializers.room_json_serializer import RoomJsonEncoder
from rentomatic.domain.room import Room


@pytest.fixture(scope='module')
def expected_json_factory():
    def _expected_json(code, size, price, longitude, latitude):
        expected_json = f"""
            {{
                "code": "{code}",
                "size": {size},
                "price": {price},
                "longitude": {longitude},
                "latitude": {latitude}
            }}
        """

        return expected_json

    return _expected_json


def test_serialize_domain_room(expected_json_factory):
    code = uuid.uuid4()
    size = 200
    price = 10
    longitude = -0.09998975
    latitude = 51.75436293

    room = Room(code, size, price, longitude, latitude)
    expected_json = expected_json_factory(code, size, price, longitude, latitude)

    json_room = json.dumps(room, cls=RoomJsonEncoder)

    assert json.loads(json_room) == json.loads(expected_json)
