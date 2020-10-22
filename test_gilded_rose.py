# -*- coding: utf-8 -*-
import unittest
from gilded_rose import GildedRose
from create_item import ItemCreate

create_item = ItemCreate()


class GildedRoseTest(unittest.TestCase):
    def test_reg_sell_in(self):
        items = [create_item.create("Cheese", 5, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)

    def test_reg_quality(self):
        items = [create_item.create("Cheese", 5, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(29, items[0].quality)

if __name__ == '__main__':
    unittest.main()
