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
        elif self.quality <= 0:
            self.quality = 0
        else:
            self.quality = 50
            
        self.sell_in -= 1


class ItemCreate(object):
    def create(self, name, sell_in, quality):
        if name == "Aged Brie":
            return AgedBrie(name, sell_in, quality)
        if name == "Sulfuras":
            return Sulfuras(name, sell_in, quality)
        if "Conjured" in name:
            return Conjured(name, sell_in, quality)
        if "Backstage" in name:
            return Backstage(name, sell_in, quality)           
        return RegularItem(name, sell_in, quality)


class AgedBrie(RegularItem):
    """'Aged Brie' actually increases in Quality the older it gets"""
    def update_quality(self):
        if 0 < self.quality < 50:
            self.quality += 1
        elif self.quality <= 0:
            self.quality = 0
        else:
            self.quality = 50

        self.sell_in -= 1


class Sulfuras(RegularItem):
    """'Sulfuras', being a legendary item, never has to be sold. It's Quality is 80 and it never alters"""
    def update_quality(self):
        self.quality = 80
        self.sell_in = "N/A"


class Conjured(RegularItem):
    """'Conjured' items degrade in Quality twice as fast as normal items"""
    def update_quality(self):
        if self.quality > 2:
            self.quality -= 2
        else:
            self.quality = 0

        self.sell_in -= 1


class Backstage(RegularItem):
    """Quality increases by 2 when there are 10 days or less and by 3 when there are 
    5 days or less but Quality drops to 0 after the concert"""
    def update_quality(self):
        if 10 >= self.sell_in > 5:
            self.quality += 2
        elif 5 >= self.sell_in > 0:
            self.quality += 3
        elif self.sell_in < 0:
            self. quality = 0
        else:
            self.quality += 1

        if self.quality > 50:
            self.quality = 50

        self.sell_in -= 1
