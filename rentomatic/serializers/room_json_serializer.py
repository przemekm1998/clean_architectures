from json import JSONEncoder
from typing import Any


class RoomJsonEncoder(JSONEncoder):

    def default(self, o: Any) -> Any:
        try:
            to_serialize = {
                'code': str(o.code),
                'size': o.size,
                'price': o.price,
                'latitude': o.latitude,
                'longitude': o.longitude
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
