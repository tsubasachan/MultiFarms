from StardewValley.Data.SVModels import svmodel
from StardewValley import EditMap, ToArea, Include
from StardewValley.Data import AdditionalFarmsData


from StardewValley.contentpatcher import EditData, Load, EditMap

from Maps.MixFarms import MixFarms

class Default(MixFarms):
    def __init__(self, maps: svmodel):
        super().__init__(maps=maps)
    
    def contents(self):
        self.addTranslation(default="Mix Farm", pt="Fazenda Mix")

        self.maps.mod.translation(language="default", key=f"Farm", value="Host Farm")
        self.maps.mod.translation(language="pt", key="Farm", value="Fazenda do Host")

        self.maps.mod.content.registryContentData(
            Include(
                FromFile=self.map_name
            )
        )

        self.registryContentData(
            Load(
                LogName="Add Farm To Intro Map",
                Target=f"LooseSprites/{self.map_name}Icon",
                FromFile=f"assets/Maps/{self.map_name}Icon.png"
            )
        )

        self.registryContentData(
            Load(
                LogName="Add Farm To Intro Map World",
                Target=f"LooseSprites/{self.map_name}Map",
                FromFile=f"assets/Maps/{self.map_name}Map.png"
            )
        )
        
        self.registryContentData(
                Load(
                    LogName=f"Load Principal Farms",
                    Target=f"Maps/{self.map_name},Maps/{self.map_name}2,Maps/{self.map_name}3",
                    FromFile=self.map_file
                )
            )
        
        self.registryContentData(
            EditMap(
                LogName=f"Edit Area to Maps2 and Maps3 area2",
                Target=f"Maps/{self.map_name}2,Maps/{self.map_name}3",
                FromFile=f"assets/Maps/Mix_Extra_Farm.tmx",
                ToArea=ToArea(0, 30, 8, 14)
            )
        )

        self.registryContentData(
            EditMap(
                LogName=f"Edit Area to Maps2 and Maps3 area2",
                Target=f"Maps/{self.map_name}3",
                FromFile=f"assets/Maps/Mix_Extra_Farm.tmx",
                ToArea=ToArea(0, 40, 8, 14)
            )
        )

        self.registryContentData(
            EditData(
                LogName=f"Add Map String to Farms",
                Target="Strings/1_6_Strings",
                Entries={
                    f"{self.map_name}": f"{self.map_name.replace('_', ' ')}_Adds 2 farms to the map, expanding the space and allowing more people to play on their own farms.",
                    f"{self.map_name}2": f"{self.map_name.replace('_', ' ')}2_Adds 4 farms to the map, expanding the space and allowing more people to play on their own farms.",
                    f"{self.map_name}3": f"{self.map_name.replace('_', ' ')}3_Adds 6 farms to the map, expanding the space and allowing more people to play on their own farms."
                }
            )
        )

        farm_additional=[]
        
        for farmN in ["", "2", "3"]:            
            farm_additional.append(
                AdditionalFarmsData(
                    key=f"{self.maps.mod.content.Manifest.UniqueID}/{self.map_name}{farmN}",
                    Id=f"{self.maps.mod.content.Manifest.UniqueID}/{self.map_name}{farmN}",
                    TooltipStringPath=f"Strings/1_6_Strings:{self.map_name}{farmN}",
                    MapName=f"{self.map_name}{farmN}",
                    IconTexture=f"LooseSprites/{self.map_name}Icon",
                    WorldMapTexture=f"LooseSprites/{self.map_name}Map",
                    SpawnMonstersByDefault=True
                )
            )

        self.registryContentData(
            EditData(
                LogName="Add Farm To tile",
                Target="Data/AdditionalFarms",
                Entries={
                    farm_additional[0].key: farm_additional[0].getJson(),
                    farm_additional[1].key: farm_additional[1].getJson(),
                    farm_additional[2].key: farm_additional[2].getJson()
                }
            )
        )