from gilded_rose import Item


class RegularItem(Item):
    """I needed Item class to have update_quality function, but altering with Item class is against the rules"""
    def update_quality(self):
        """The Quality of an item is never more than 50.
        The Quality of an item is never negative"""
        if 50 > self.quality > 0:
            """Once the sell by date has passed, Quality degrades twice as fast"""
            if self.sell_in <= 0:
                self.quality -= 2
            else:
                self.quality -= 1
        self.sell_in -= 1


class ItemCreate(object):
    def create(self, name, sell_in, quality):
        if name == "Aged Brie":
            return AgedBrie(name, sell_in, quality)
        if name == "Sulfuras":
            return Sulfuras(name, sell_in, quality)
        return RegularItem(name, sell_in, quality)


class AgedBrie(RegularItem):
    """'Aged Brie' actually increases in Quality the older it gets"""
    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
        self.sell_in -= 1

class Sulfuras(RegularItem):
    """'Sulfuras', being a legendary item, never has to be sold. It's Quality is 80 and it never alters"""
    def update_quality(self):
        self.quality = 80
        self.sell_in = "N/A"
