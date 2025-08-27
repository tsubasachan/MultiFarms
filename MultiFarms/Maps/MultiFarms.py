from StardewValley.Data.SVModels.svmodel import svmodel
from StardewValley.Data.SVModels.Maps import MapsModel
from StardewValley import EditMap, MapTiles, WarpPosition
from StardewValley.Data import LocationsData, AdditionalFarmsData, Position

from StardewValley.contentpatcher import EditData, Load, EditMap, MapTiles



class MultiFarms(MapsModel):
    def __init__(self, maps: svmodel, mapName):
        super().__init__(map_name=mapName, map_file=f"assets/Maps/{mapName}.tmx", maps=maps)
    
    def contents(self):
        super().contents()

        
    
        self.maps.registryContentData(
            EditData(
                LogName="Add Map String",
                Target="Strings/1_6_Strings",
                Entries={
                    self.map_name: self.map_name
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

        #set cabins positions

        dataCabins=[(44, 14), (24, 14), (6, 14), (96, 5), (113, 5), (130, 5), (146, 5)]
        tilesFarm=[]
        for idx, (x,y) in enumerate(dataCabins):
            order=idx+1
            positions=[Position(x,y), Position(x+1, y)]
            for pos in positions:
                tilesFarm.append(MapTiles(
                    Layer="Paths",
                    Position=pos,
                    SetProperties={
                        "Order":order
                    }
                ))
        

        #protect paths from drop terrain plants
        protectTiles=[(39, 62), (126,62), (213, 62), (300,62)]
        if self.map_name!="FourFarms":
            protectTiles.extend([(39, 122), (126,122), (213, 122), (300,122)])
        if self.map_name!="FourFarms" and self.map_name!="EightFarms":
            protectTiles.extend([(39, 182), (126,182), (213, 182), (300,182)])
        if self.map_name!="FourFarms" and self.map_name!="EightFarms" and self.map_name!="TwelveFarms":
            protectTiles.extend([(39, 242), (126,241), (213, 241), (300,241)])
        for x0,y0 in protectTiles:
            # Bloco 1: NPCBarrier

            for dx, dy in [(0,0), (3,0)]:
                tilesFarm.append(MapTiles(
                    Layer="Back",
                    Position=Position(x0+dx, y0+dy),
                    SetProperties={
                        "NPCBarrier":"T"
                    }
                ))
            
            # Bloco 2: NPCBarrier + NoSpawn
            for dx, dy in [(1,0), (2,0), (3,1)]:
                tilesFarm.append(MapTiles(
                    Layer="Back",
                    Position=Position(x0 + dx, y0 + dy),
                    SetProperties={"NPCBarrier":"T", "NoSpawn":"All"}
                ))

            # Bloco 3: apenas NoSpawn
            
            tilesFarm.append(MapTiles(
                Layer="Back",
                Position=Position(x0, y0 + 1),
                SetProperties={"NoSpawn":"All"}
            ))
            
            # Bloco 4: repetindo NoSpawn até y=72
            for y in range(63, 73):
                for dx in [1,2]:
                    tilesFarm.append(MapTiles(
                        Layer="Back",
                        Position=Position(x0 + dx, y),
                        SetProperties={"NoSpawn":"All"}
                    ))

        forestWarp={
            "FourFarms":(0, 76),
            "EightFarms":(0, 136),
            "TwelveFarms":(0, 196),
            "SixteenFarms":(0, 256)
        }

        self.maps.registryContentData(
            EditMap(
                LogName="Add Tiles To Farm",
                Target=f"Maps/{self.map_name}",
                MapTiles=tilesFarm,
                MapProperties={
                    "BackwoodsEntry":"40 0",
                    "BusStopEntry": "350 17",
                    "FarmCaveEntry": "34 7",
                    "FarmHouseEntry": "65 15",
                    "FarmHouseFlooring": "90",
                    "FarmHouseFurniture": "1866 9 4 0 424 5 4 0 1680 1 4 0",
                    "FarmHouseStarterGift": "(O)178 15",
                    "FarmHouseStarterSeedsPosition": "4 7",
                    "FarmHouseWallpaper": "34",
                    "FarmHouseStarterGift": "(O)368 9 (O)472 9 (O)475 9",
                    "FarmHouseStarterSeedsPosition": "10 6",
                    "ForestEntry": f"{forestWarp[self.map_name][0]} {forestWarp[self.map_name][1]}",
                    "GrandpaShrineLocation": "8 7",
                    "MailboxLocation" : "69 16",
                    "PetBowLocation": "52 7"                    
                }
            )
        )        