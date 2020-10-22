# -*- coding: utf-8 -*-
import unittest
from gilded_rose import GildedRose
from create_item import ItemCreate

create_item = ItemCreate()


class GildedRoseTest(unittest.TestCase):
    def test_reg_sell_in(self):
        items = [create_item.create("Elixir of the Mongoose", 5, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)

    def test_reg_quality(self):
        items = [create_item.create("Elixir of the Mongoose", 5, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(29, items[0].quality)

    def test_reg_quality_passed(self):
        items = [create_item.create("Elixir of the Mongoose", 0, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(28, items[0].quality)

    def test_reg_quality_low(self):
        items = [create_item.create("Elixir of the Mongoose", 5, -10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_brie_sell_in(self):
        items = [create_item.create("Aged Brie", 5, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
    
    def test_brie_quality(self):
        items = [create_item.create("Aged Brie", 5, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(41, items[0].quality)

    def test_brie_quality_max(self):
        items = [create_item.create("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_brie_quality_over(self):
        items = [create_item.create("Aged Brie", 5, 75)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_brie_quality_low(self):
        items = [create_item.create("Aged Brie", 5, -5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_sulfuras_sell_in(self):
        items = [create_item.create("Sulfuras", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("N/A", items[0].sell_in)

    def test_sulfuras_quality(self):
        items = [create_item.create("Sulfuras", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_quality_low(self):
        items = [create_item.create("Sulfuras", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_quality_over(self):
        items = [create_item.create("Sulfuras", 10, 130)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_conjured_quality(self):
        items = [create_item.create("Conjured Mana Cake", 6, 15)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)       

    def test_conjured_quality_low(self):
        items = [create_item.create("Conjured Stamina Pancakes", 12, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_quality(self):
        items = [create_item.create("Backstage passes to a TAFKAL80ETC concert", 18, 48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(49, items[0].quality)

    def test_backstage_quality_over(self):
        items = [create_item.create("Backstage passes to a TAFKAL80ETC concert", 18, 95)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_backstage_soon(self):
        items = [create_item.create("Backstage passes to a TAFKAL80ETC concert", 10, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(32, items[0].quality)

    def test_backstage_very_soon(self):
        items = [create_item.create("Backstage passes to a TAFKAL80ETC concert", 5, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(33, items[0].quality)

    def test_backstage_expired(self):
        items = [create_item.create("Backstage passes to a TAFKAL80ETC concert", -1, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
