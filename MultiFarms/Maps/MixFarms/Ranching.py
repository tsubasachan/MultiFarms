from StardewValley.Data.SVModels import svmodel
from StardewValley.Data import LocationsData, Position, CreateOnLoad
from Maps.MixFarms import MixFarms

class Ranching(MixFarms):
    def __init__(self, maps: svmodel):
        self.dataLoc=maps.mod.sdk("Data", "Locations")
        super().__init__(maps=maps)
    
    def contents(self):
        super().contents()

        self.addTranslation(default="Meadowlands Farm", pt="Fazenda dos Prados")
        self.addFarmLocation(location_name_map="Farm_MeadowlandsFarm")