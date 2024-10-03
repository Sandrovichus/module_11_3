def introspection_info(obj):
    return {'type': type(obj),
            'attributes': [element for element in dir(obj) if not callable(getattr(obj, element))],
            'methods': [element for element in dir(obj) if callable(getattr(obj, element))],
            'module': obj.__module__,
            'windows': getattr(obj, 'windows'),
            'doors': getattr(obj, 'doors')}


class House:
    def __init__(self, windows, doors):
        self.windows = windows
        self.doors = doors

    def build(self):
        print(f'House is built with {self.windows} windows and {self.doors} doors!')


my_house = House(5, 2)
my_house.build()

house_info = introspection_info(my_house)
print(house_info)
