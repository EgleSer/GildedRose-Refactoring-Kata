import pytest
from gilded_rose import GildedRose
from create_item import ItemCreate

create_item = ItemCreate()


def test_reg_sell_in():
    items = [create_item.create("Elixir of the Mongoose", 5, 30)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 4


def test_reg_quality():
    items = [create_item.create("Elixir of the Mongoose", 5, 30)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 29


def test_reg_quality_passed():
    items = [create_item.create("Elixir of the Mongoose", 0, 30)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 28


def test_reg_quality_low():
    items = [create_item.create("Elixir of the Mongoose", 5, -10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality ==  0


def test_brie_sell_in():
    items = [create_item.create("Aged Brie", 5, 40)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 4
   

def test_brie_quality():
    items = [create_item.create("Aged Brie", 5, 40)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 41


def test_brie_quality_max():
    items = [create_item.create("Aged Brie", 5, 50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50


def test_brie_quality_over():
    items = [create_item.create("Aged Brie", 5, 75)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50


def test_brie_quality_low():
    items = [create_item.create("Aged Brie", 5, -5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


def test_sulfuras_sell_in():
    items = [create_item.create("Sulfuras", 10, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == "N/A"


def test_sulfuras_quality():
    items = [create_item.create("Sulfuras", 10, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 80


def test_sulfuras_quality_low():
    items = [create_item.create("Sulfuras", 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 80


def test_sulfuras_quality_over():
    items = [create_item.create("Sulfuras", 10, 130)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 80


def test_conjured_quality():
    items = [create_item.create("Conjured Mana Cake", 6, 15)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 13


def test_conjured_quality_low():
    items = [create_item.create("Conjured Stamina Pancakes", 12, 1)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


def test_backstage_quality():
    items = [create_item.create("Backstage passes to a TAFKAL80ETC concert", 18, 48)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 49


def test_backstage_quality_over():
    items = [create_item.create("Backstage passes to a TAFKAL80ETC concert", 18, 95)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50


def test_backstage_soon():
    items = [create_item.create("Backstage passes to a TAFKAL80ETC concert", 10, 30)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 32


def test_backstage_very_soon():
    items = [create_item.create("Backstage passes to a TAFKAL80ETC concert", 5, 30)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 33


def test_backstage_expired():
    items = [create_item.create("Backstage passes to a TAFKAL80ETC concert", -1, 30)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


def test_backstage_sell_in():
    items = [create_item.create("Backstage passes to a TAFKAL80ETC concert", 5, 30)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 4


if __name__ == '__main__':
    pytest.main()
