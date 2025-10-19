from StardewValley.Data.SVModels import svmodel
from StardewValley.Data.SVModels import MapsModel
from StardewValley.Data import LocationsData, Position, CreateOnLoad



class MixFarms(MapsModel):
    def __init__(self, maps: svmodel):
        self.dataLoc=maps.mod.sdk("Data", "Locations")
        mapName=f"Mix_Farm_{self.__class__.__name__}" if self.__class__.__name__ != "Default" else "Mix_Farm"
        super().__init__(map_name=mapName, map_file=f"assets/Maps/{mapName}.tmx", maps=maps)
    
    def addTranslation(self, default:str, pt:str):
        self.maps.mod.translation(language="default", key=f"Mix_Farm_{self.__class__.__name__}", value=default)
        self.maps.mod.translation(language="pt", key=f"Mix_Farm_{self.__class__.__name__}", value=pt)


    
    def addFarmLocation(self, location_name_map:str):
        LocationsData(
            key=f"{self.map_name}",
            DisplayName="{{i18n: Mix_Farm_"+self.__class__.__name__+"}}",
            DefaultArrivalTile=Position(64, 15),
            CreateOnLoad=CreateOnLoad(
                MapPath=f"Maps/{self.map_name}",
                AlwaysActive=True
            ),
            CanPlantHere=True,
            CanHaveGreenRainSpawns=True,
            ArtifactSpots=self.dataLoc[location_name_map]["ArtifactSpots"],
            FishAreas=self.dataLoc[location_name_map]["FishAreas"],
            Fish=self.dataLoc[location_name_map]["Fish"],
            MinDailyWeeds=5,
            MaxDailyWeeds=11,
            FirstDayWeedMultiplier= 15,
            MinDailyForageSpawn=1,
            MaxDailyForageSpawn=4,
            MaxSpawnedForageAtOnce= 6,
            ChanceForClay= 0.03,
            FormerLocationNames=[f"Custom_{self.map_name}"]
        ).register(
            LogName=f"Add Location {self.map_name}", 
            Target="Data/Locations",
            mod=self.maps.mod,
            contentFile=self.map_name
        )
    
    
    def contents(self):        
        super().contents()