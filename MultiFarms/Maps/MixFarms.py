from asyncio import Condition
from StardewValley.Data.SVModels.svmodel import svmodel
from StardewValley.Data.SVModels.Maps import MapsModel
from StardewValley import EditMap, MapTiles, WarpPosition, ToArea
from StardewValley.Data import LocationsData, AdditionalFarmsData, Position, CreateOnLoad


from StardewValley.contentpatcher import EditData, Load, EditMap, MapTiles

class MixFarms(MapsModel):
    def __init__(self, maps: svmodel, mapName):
        super().__init__(map_name=mapName, map_file=f"assets/Maps/{mapName}.tmx", maps=maps)
    
    def addSpawn(self, spawn:list, x:int, y:int):
        spawn.append(
            MapTiles(
                Layer="Back",
                Position=Position(x, y),
                SetProperties={"NoSpawn": "All"}
            )
        )
    
    def contents(self):
        super().contents()

        noSpawnTiles=[]
        #14 16 - 20  21
        for y in range(16,22):
            for x in range(14, 21):
                self.addSpawn(noSpawnTiles, x, y)
        
        #3 9 - 42 13
        for y in range(9,14):
            for x in range(3, 43):
                self.addSpawn(noSpawnTiles, x, y)
        
        #4 8 - 42 8
        for y in range(8,9):
            for x in range(4, 43):
                self.addSpawn(noSpawnTiles, x, y)

        #3 14 - 6 32
        for y in range(14,33):
            for x in range(3, 7):
                self.addSpawn(noSpawnTiles, x, y)

        #0 24 - 2 27
        for y in range(24,28):
            for x in range(0, 3):
                self.addSpawn(noSpawnTiles, x, y)
        
        #0 29 - 2 31
        for y in range(29,32):
            for x in range(0, 3):
                self.addSpawn(noSpawnTiles, x, y)

        self.maps.registryContentData(
            EditMap(
                LogName=f"Editando {self.map_name}",
                Target=f"Maps/{self.map_name}",
                MapTiles=noSpawnTiles
            )
        )

        #Carregando MixFarm2
        self.maps.registryContentData(
            Load(
                LogName=f"Carregando {self.map_name}",
                Target=f"Maps/{self.map_name}2",
                FromFile=self.map_file
            )
        )

        #Protegendo Spawn em MixFarm2
        self.maps.registryContentData(
            EditMap(
                LogName=f"Editando {self.map_name}",
                Target=f"Maps/{self.map_name}2",
                FromFile=f"assets/Maps/Mix_Extra_Farm.tmx",
                ToArea=ToArea(0, 30, 8, 14),
                MapTiles=noSpawnTiles
            )
        )
        
        #Carregando Fazenda Remota
        self.maps.registryContentData(
            Load(
                LogName=f"Carregando {self.map_name}_Combat",
                Target=f"Maps/{self.map_name}_Combat",
                FromFile=self.map_file.replace(self.map_name, f"{self.map_name}_Combat")
            )
        )

        self.maps.registryContentData(
            Load(
                LogName=f"Carregando {self.map_name}_Island",
                Target=f"Maps/{self.map_name}_Island",
                FromFile=self.map_file.replace(self.map_name, f"{self.map_name}_Island")
            )
        )

        dataLoc=self.maps.mod.sdk("Data", "Locations")
        LocationsData(
            key=f"{self.map_name}_Island",
            DisplayName="Farm Island",
            DefaultArrivalTile=Position(64, 15),
            CreateOnLoad=CreateOnLoad(
                MapPath=f"Maps/{self.map_name}_Island",
                AlwaysActive=True
            ),
            CanPlantHere=True,
            CanHaveGreenRainSpawns=True,
            Fish=dataLoc["Farm_Beach"]["Fish"],
            FishAreas=dataLoc["Farm_Beach"]["FishAreas"],
            ArtifactSpots=dataLoc["Farm_Beach"]["ArtifactSpots"],
            MinDailyWeeds=5,
            MaxDailyWeeds=11,
            FirstDayWeedMultiplier= 15,
            MinDailyForageSpawn=1,
            MaxDailyForageSpawn=4,
            MaxSpawnedForageAtOnce= 6,
            ChanceForClay= 0.03,
            FormerLocationNames=[f"Custom_{self.map_name}_Island"]
        ).register(
            LogName=f"Add Location {self.map_name}_Island", 
            Target="Data/Locations",
            mod=self.maps.mod,
            contentFile=self.maps.__class__.__name__
        )

        LocationsData(
            key=f"{self.map_name}_Combat",
            DisplayName="Farm Combat",
            DefaultArrivalTile=Position(64, 15),
            CreateOnLoad=CreateOnLoad(
                MapPath=f"Maps/{self.map_name}_Combat",
                AlwaysActive=True
            ),
            CanPlantHere=True,
            CanHaveGreenRainSpawns=True,
            ArtifactSpots=dataLoc["Farm_Wilderness"]["ArtifactSpots"],
            FishAreas=dataLoc["Farm_Wilderness"]["FishAreas"],
            Fish=dataLoc["Farm_Wilderness"]["Fish"],
            MinDailyWeeds=5,
            MaxDailyWeeds=11,
            FirstDayWeedMultiplier= 15,
            MinDailyForageSpawn=1,
            MaxDailyForageSpawn=4,
            MaxSpawnedForageAtOnce= 6,
            ChanceForClay= 0.03,
            FormerLocationNames=[f"Custom_{self.map_name}_Combat"]
        ).register(
            LogName=f"Add Location {self.map_name}_Combat", 
            Target="Data/Locations",
            mod=self.maps.mod,
            contentFile=self.maps.__class__.__name__
        )
        
        self.maps.registryContentData(
            EditData(
                LogName="Add Map String",
                Target="Strings/1_6_Strings",
                Entries={
                    self.map_name: self.map_name,
                    f"{self.map_name}2": f"{self.map_name}2"
                }
            )
        )

        self.maps.registryContentData(
            Load(
                LogName="Add Farm To Intro Map",
                Target=f"LooseSprites/{self.map_name}Icon",
                FromFile=f"assets/Maps/{self.map_name}Icon.png"
            )
        )

        self.maps.registryContentData(
            Load(
                LogName="Add Farm To Intro Map World",
                Target=f"LooseSprites/{self.map_name}Map",
                FromFile=f"assets/Maps/{self.map_name}Map.png"
            )
        )

        farm_additional=AdditionalFarmsData(
            key=f"{self.maps.mod.content.Manifest.UniqueID}/{self.map_name}",
            Id=f"{self.maps.mod.content.Manifest.UniqueID}/{self.map_name}",
            TooltipStringPath=f"Strings/1_6_Strings:{self.map_name}",
            MapName=self.map_name,
            IconTexture=f"LooseSprites/{self.map_name}Icon",
            WorldMapTexture=f"LooseSprites/{self.map_name}Map",
            SpawnMonstersByDefault=True
        )

        self.maps.registryContentData(
            EditData(
                LogName="Add Farm To tile",
                Target="Data/AdditionalFarms",
                Entries={
                    farm_additional.key: farm_additional.getJson()
                }
            )
        )

        farm_additional2=AdditionalFarmsData(
            key=f"{self.maps.mod.content.Manifest.UniqueID}/{self.map_name}2",
            Id=f"{self.maps.mod.content.Manifest.UniqueID}/{self.map_name}2",
            TooltipStringPath=f"Strings/1_6_Strings:{self.map_name}2",
            MapName=f"{self.map_name}2",
            IconTexture=f"LooseSprites/{self.map_name}Icon",
            WorldMapTexture=f"LooseSprites/{self.map_name}Map",
            SpawnMonstersByDefault=True
        )

        self.maps.registryContentData(
            EditData(
                LogName="Add Farm2 To tile",
                Target="Data/AdditionalFarms",
                Entries={
                    farm_additional2.key: farm_additional2.getJson()
                }
            )
        )