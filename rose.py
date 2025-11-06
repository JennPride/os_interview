
class GuildedRose:

    PASS = "Backstage passes"
    BRIE = "Aged Brie"
    SULFURAS = "Sulfuras"
    MANA_CAKE = "Mana_Cake"
    DEFAULT = "Default"

    SPECIAL_CASES = [PASS, BRIE, SULFURAS, MANA_CAKE]

    LESS_THAN_EQUAL_TO_DAILY_QUALITY_CHANGE = {
        BRIE: {
            50: 1,
            0: 2,             
        },
        SULFURAS: {
            80: 0,
        },
        PASS: {
            50: 1,
            10: 2,
            5: 3,
            0: 0,
        },
        DEFAULT: {
            0: -1,
        },
        MANA_CAKE: {
            50: 2,
            0: -2,
        }
    }

    ZERO_QUALITY_PAST_SELLBY = [PASS]
    NO_CHANGE = [SULFURAS]

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            item_type = item.type

            if item_type not in self.SPECIAL_CASES:
                item_type = self.DEFAULT

            if item_type in self.NO_CHANGE:
                continue

            if item.sell_by_days == 0 and item_type in self.ZERO_QUALITY_PAST_SELLBY:
                item.quality = 0
                continue
            
            daily_change = self.LESS_THAN_EQUAL_TO_DAILY_QUALITY_CHANGE[item_type]
            quality_change = 0
            for threshold in sorted(daily_change.keys()):
                if item.sell_by_days <= threshold:
                    quality_change = daily_change[threshold]
                    break
            new_quality = max(0, min(50, item.quality + quality_change))
            item.quality = new_quality

            if item.sell_by_days > 0:
                item.sell_by_days -= 1


class Item:
    def __init__(self, type: str, sell_by_days: int, quality: int):
        if not isinstance(type, str):
            raise TypeError("type must be a string")
        if not isinstance(sell_by_days, int):
            raise TypeError("sell_by_days must be an int")
        if not isinstance(quality, int):
            raise TypeError("quality must be an int")
        self.type = type
        self.sell_by_days = sell_by_days
        self.quality = quality

    def __repr__(self) -> str:
        return f"Item(type={self.type!r}, sell_by_days={self.sell_by_days}, quality={self.quality})"
