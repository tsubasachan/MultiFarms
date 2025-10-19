from StardewValley.Data.SVModels.svmodel import svmodel
from StardewValley.Data.SVModels import FarmModel
from StardewValley import EditMap


class MultiFarms(FarmModel):
    def __init__(self, maps: svmodel):
        super().__init__(maps=maps)
    

    def contents(self):
        super().contents()
        self.AddForest()
        
    def AddForest(self):
        from Maps.MultiFarms.data import forestWarp
        self.registryContentData(
            EditMap(
                LogName="Add Tiles To Farm",
                Target=f"Maps/{self.map_name}",
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