import pytest
from rose import GuildedRose, Item

def test_default_item():
    # Default item decreases quality by 1 when sell_by_days > 0
    item_1 = Item("Random", 0, 10)
    # Should not change
    item_2 = Item("Another", 5, 20)
    g = GuildedRose([item_1, item_2])
    g.update_quality()
    assert item_1.quality == 9
    assert item_2.quality == 20
    assert item_1.sell_by_days == 0
    assert item_2.sell_by_days == 4

def test_aged_brie():
    item_1 = Item(GuildedRose.BRIE, 50, 10)
    item_2 = Item(GuildedRose.BRIE, 0, 10)
    g = GuildedRose([item_1, item_2])
    g.update_quality()
    assert item_1.quality == 11
    assert item_2.quality == 12
    assert item_1.sell_by_days == 49
    assert item_2.sell_by_days == 0

def test_sulfuras():
    item = Item(GuildedRose.SULFURAS, 80, 80)
    g = GuildedRose([item])
    g.update_quality()
    assert item.quality == 80
    assert item.sell_by_days == 80

def test_backstage_passes():
    item_1 = Item(GuildedRose.PASS, 15, 20)
    item_2 = Item(GuildedRose.PASS, 10, 20)
    item_3 = Item(GuildedRose.PASS, 5, 20)
    item_4 = Item(GuildedRose.PASS, 0, 20)
    g = GuildedRose([item_1, item_2, item_3, item_4])
    g.update_quality()
    assert item_1.quality == 21
    assert item_2.quality == 22
    assert item_3.quality == 23
    assert item_4.quality == 0
    assert item_1.sell_by_days == 14
    assert item_2.sell_by_days == 9
    assert item_3.sell_by_days == 4
    assert item_4.sell_by_days == 0

def test_mana_cake():
    item_1 = Item(GuildedRose.MANA_CAKE, 5, 30)
    item_2 = Item(GuildedRose.MANA_CAKE, 0, 30)
    item_3 = Item(GuildedRose.MANA_CAKE, 0, 1)
    g = GuildedRose([item_1, item_2, item_3])
    g.update_quality()
    assert item_1.quality == 32
    assert item_2.quality == 28
    assert item_3.quality == 0
    assert item_1.sell_by_days == 4
    assert item_2.sell_by_days == 0
    assert item_3.sell_by_days == 0
