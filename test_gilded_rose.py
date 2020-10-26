import pytest
from gilded_rose import GildedRose
from create_item import ItemCreate

create_item = ItemCreate()


def item_through_days(item_params, days):
    item = create_item.create(*item_params)
    gilded_rose = GildedRose([item])
    for x in range(days):
        gilded_rose.update_quality()
    return item


@pytest.mark.parametrize(
    "item,expected,num_days",
    [
        (("Elixir of the Mongoose", 5, 30), {"sell_in": 4, "quality": 29}, 1),
        (("Elixir of the Mongoose", 0, 30), {"quality": 28}, 1),
        (("Elixir of the Mongoose", 5, -10), {"quality": 0}, 1),
        (("Aged Brie", 5, 40), {"sell_in": 4, "quality": 41}, 1),
        (("Aged Brie", 5, 50), {"quality": 50}, 1),
        (("Aged Brie", 5, 75), {"quality": 50}, 1),
        (("Aged Brie", 5, -5), {"quality": 0}, 1),
        (("Sulfuras", 10, 80), {"sell_in": "N/A", "quality": 80}, 1),
        (("Sulfuras", 10, 20), {"quality": 80}, 1),
        (("Sulfuras", 10, 130), {"quality": 80}, 1),
        (("Conjured Mana Cake", 6, 15), {"sell_in": 5, "quality": 13}, 1),
        (("Conjured Stamina Pancakes", 12, 1), {"sell_in": 11, "quality": 0}, 1),
        (("Backstage passes to a TAFKAL80ETC concert", 18, 48), {"sell_in": 17, "quality": 49}, 1),
        (("Backstage passes to a TAFKAL80ETC concert", 18, 95), {"quality": 50}, 1),
        (("Backstage passes to a TAFKAL80ETC concert", 10, 30), {"sell_in": 9, "quality": 32}, 1),
        (("Backstage passes to a TAFKAL80ETC concert", 5, 30), {"sell_in": 4, "quality": 33}, 1),
        (("Backstage passes to a TAFKAL80ETC concert", -1, 30), {"quality": 0}, 1),

    ],
)
def test_item_one_day_passed(item, expected, num_days):
    item_after_days = item_through_days(item, num_days)
    for key in expected:
        assert getattr(item_after_days, key) == expected[key]


if __name__ == '__main__':
    pytest.main()
