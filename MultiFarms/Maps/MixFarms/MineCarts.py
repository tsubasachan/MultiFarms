

from ast import Set
from StardewValley import EditData, EditMap, Include, MapTiles
from StardewValley.Data import MinecartsData, Destinations, Position
from StardewValley.Data.SVModels import svmodel


class MineCarts:
    def __init__(self, maps:svmodel):
        self.maps=maps
        self.contents()

    def contents(self):
        self.maps.mod.content.registryContentData(
            Include(
                FromFile=self.__class__.__name__
            )
        )

        from Maps.MixFarms.data import cartsDestins

        mineCartMixFarms=MinecartsData(
            key="MineCartMixFarms",
            Destinations=[]
        )

        
        for mapName, (farmId, TargetLocation, x, y) in cartsDestins.items():
            if mapName!="Mix_Farm2" and mapName!="Mix_Farm3":
                if mapName=="Mix_Farm":
                    mineCartMixFarms.Destinations.append(
                        Destinations(
                            Id=farmId,
                            DisplayName="{{i18n: " + TargetLocation + "}}",
                            TargetLocation=TargetLocation,
                            TargetTile=Position(x, y+1),
                            TargetDirection="right"
                        )
                    )
                else:
                    condition=f"ANY \"FARM_TYPE {self.maps.mod.content.Manifest.UniqueID}/Mix_Farm3\""
                    nFarmId=int(farmId.replace("Farm", ""))
                    if nFarmId<6:
                        condition+=f" \"FARM_TYPE {self.maps.mod.content.Manifest.UniqueID}/Mix_Farm2\""
                    if nFarmId<4:
                        condition+=f" \"FARM_TYPE {self.maps.mod.content.Manifest.UniqueID}/Mix_Farm\""
                    mineCartMixFarms.Destinations.append(
                        Destinations(
                            Id=farmId,
                            DisplayName="{{i18n: " + TargetLocation + "}}",
                            TargetLocation=TargetLocation,
                            TargetTile=Position(x, y),
                            TargetDirection="right",
                            Condition=condition
                        )
                    )

        

        self.maps.mod.content.registryContentData(
            EditData(
                LogName="Add new Mine Cart Mix Farms",
                Target="Data/Minecarts",
                Entries={
                    mineCartMixFarms.key: mineCartMixFarms.getJson()
                }
            ),
            contentFile=self.__class__.__name__
        )