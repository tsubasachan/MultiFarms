from StardewValley.Data.SVModels import Maps as MapsModel
from StardewValley import Helper, EditMap, WarpPosition
from regex import E

from Maps.MultiFarms import FourFarms, EightFarms, TwelveFarms, SixteenFarms

from Maps.MixFarms import Default, Combat, Island, Fishing, Foraging, Mining, Ranching, MineCarts

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

        FourFarms(
            maps=self
        )

        EightFarms(
            maps=self
        )

        TwelveFarms(
            maps=self
        )

        SixteenFarms(
            maps=self
        )
        

        Default(
            maps=self
        )

        Island(
            maps=self
        )

        Combat(
            maps=self
        )

        Fishing(
            maps=self
        )

        Foraging(
            maps=self
        )

        Mining(
            maps=self
        )

        Ranching(
            maps=self
        )

        MineCarts(
            maps=self
        )
        

        self.mod.content.registryContentData(
            EditMap(
                LogName="Edit Map Waps",
                Target="Maps/BusStop",
                AddWarps=[
                    WarpPosition(9, 22, "Farm", 350, 17),
                    WarpPosition(9, 23, "Farm", 350, 17),
                    WarpPosition(9, 24, "Farm", 350, 17)                    
                ],
                When={
                    "FarmName": "FourFarms,EightFarms,TwelveFarms,SixteenFarms"
                }
            ),
            contentFile=self.__class__.__name__
        )

        from Maps.MultiFarms.data import forestWarp
        
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
        
        MineCarts(
            maps=self
        )