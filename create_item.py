from gilded_rose import Item


class RegularItem(Item):
    """I needed Item class to have  update_quality function, but altering with Item class is against the rules"""
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


class ItemCreate(object):
    def create(self, name, sell_in, quality):
        return RegularItem(name, sell_in, quality)
