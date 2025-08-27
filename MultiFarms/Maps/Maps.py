from StardewValley.Data.SVModels import Maps as MapsModel
from StardewValley import Helper, EditMap, ToArea, MapTiles, EditData, WarpPosition

from StardewValley.Data.XNA import Position

from Maps.MultiFarms import MultiFarms

class Maps(MapsModel):
    def __init__(self, mod: Helper):
        super().__init__(mod)
        self.mod.assetsFileIgnore=[
            "Maps/paths.png",
            "Maps/spring_outdoorsTileSheet.png",
            "Maps/spring_outdoorsTileSheet2.png",
            "Maps/spring_outdoorTileSheet_extra.png"
        ]
    
    def contents(self):
        super().contents()

        MultiFarms(
            maps=self,
            mapName="FourFarms"
        )

        MultiFarms(
            maps=self,
            mapName="EightFarms"
        )

        MultiFarms(
            maps=self,
            mapName="TwelveFarms"
        )

        MultiFarms(
            maps=self,
            mapName="SixteenFarms"
        )


        self.mod.content.registryContentData(
            EditMap(
                LogName="Edit Map Waps",
                Target="Maps/BusStop",
                AddWarps=[
                    WarpPosition(9, 22, "Farm", 350, 17),
                    WarpPosition(9, 23, "Farm", 350, 17),
                    WarpPosition(9, 24, "Farm", 350, 17)                    
                ]
            ),
            contentFile=self.__class__.__name__
        )

        forestWarp={
            "FourFarms":(0, 76),
            "EightFarms":(0, 136),
            "TwelveFarms":(0, 196),
            "SixteenFarms":(0, 256)
        }
        
        for farmName, (x, y) in forestWarp.items():
            self.mod.content.registryContentData(
                EditMap(
                    LogName="Edit Warps to Forest",
                    Target="Maps/Forest",
                    AddWarps=[
                        WarpPosition(67, -1, "Farm", x, y),
                        WarpPosition(68, -1, "Farm", x, y),
                        WarpPosition(69, -1, "Farm", x, y),
                        WarpPosition(70, -1, "Farm", x, y),
                        WarpPosition(71, -1, "Farm", x, y),
                        WarpPosition(72, -1, "Farm", x, y)                    
                    ],
                    When={
                        "FarmName": farmName
                    }
                ),
                contentFile=self.__class__.__name__
            )