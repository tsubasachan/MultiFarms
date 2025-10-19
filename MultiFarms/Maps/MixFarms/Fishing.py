from StardewValley.Data.SVModels import svmodel
from StardewValley.Data import LocationsData, Position, CreateOnLoad
from Maps.MixFarms import MixFarms

class Fishing(MixFarms):
    def __init__(self, maps: svmodel):
        super().__init__(maps=maps)
    
    def contents(self):
        super().contents()

        self.addTranslation(default="Riverland Farm", pt="Fazenda entre Rios")
        self.addFarmLocation(location_name_map="Farm_Riverland")