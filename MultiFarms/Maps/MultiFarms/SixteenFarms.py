from Maps.MultiFarms.MultiFarms import MultiFarms
from StardewValley.Data.SVModels import svmodel


class SixteenFarms(MultiFarms):
    def __init__(self, maps: svmodel):
        super().__init__(maps=maps)

    def contents(self):
        super().contents()