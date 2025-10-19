from StardewValley.Data.SVModels import svmodel
from StardewValley.Data import LocationsData, Position, CreateOnLoad
from Maps.MixFarms import MixFarms

class Mining(MixFarms):
    def __init__(self, maps: svmodel):
        self.dataLoc=maps.mod.sdk("Data", "Locations")
        super().__init__(maps=maps)
    
    def contents(self):
        super().contents()

        self.addTranslation(default="Hilltop Farm", pt="Fazenda na Colina")
        self.addFarmLocation(location_name_map="Farm_Hilltop")