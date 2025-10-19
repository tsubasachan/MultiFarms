from StardewValley.Data.SVModels import svmodel
from StardewValley.Data import LocationsData, Position, CreateOnLoad

from Maps.MixFarms import MixFarms

class Island(MixFarms):
    def __init__(self, maps: svmodel):
        super().__init__(maps=maps)
    
    def contents(self):
        super().contents()

        self.addTranslation(default="Beach Farm", pt="Fazenda da Praia")

        self.addFarmLocation(location_name_map="Farm_Beach")

