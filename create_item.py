class RegularItem(object):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f'{self.name}, {self.sell_in}, {self.quality}'

    def update_quality(self):
        """The Quality of an item is never more than 50.
        The Quality of an item is never negative"""
        if 50 > self.quality > 0:
            """Once the sell by date has passed, Quality degrades twice as fast"""
            if self.sell_in <= 0:
                self.quality = self.quality - 2
            else:
                self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1


