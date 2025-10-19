from StardewValley.Data.SVModels import svmodel
from StardewValley.Data import LocationsData, Position, CreateOnLoad

from Maps.MixFarms import MixFarms

class Foraging(MixFarms):
    def __init__(self, maps: svmodel):
        super().__init__(maps=maps)
    
    def contents(self):
        super().contents()

        self.addTranslation(default="Forest Farm", pt="Fazenda na Floresta")
        self.addFarmLocation(location_name_map="Farm_Forest")