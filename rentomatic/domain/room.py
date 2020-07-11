class Room:
    def __init__(self, code, size, price, longitude, latitude):
        self.code = code
        self.size = size
        self.price = price
        self.longitude = longitude
        self.latitude = latitude

    @classmethod
    def from_dict(cls, dictionary):
        return cls(
            code=dictionary['code'],
            size=dictionary['size'],
            price=dictionary['price'],
            latitude=dictionary['latitude'],
            longitude=dictionary['longitude']
        )

    def to_dict(self):
        return {
            'code': self.code,
            'size': self.size,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

    def __eq__(self, other: 'Room'):
        return self.to_dict() == other.to_dict()
