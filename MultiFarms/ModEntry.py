from re import I
from StardewValley import EditData, Manifest, Helper, ContentPatcher

from Maps.Maps import Maps


class ModEntry(Helper):
    def __init__(self, manifest:Manifest):
        super().__init__(
            manifest=manifest, modFramework=ContentPatcher(manifest=manifest)
        )
        self.contents()
    
    def contents(self):
        # Add your contents here
        Maps(self)

        self.content.registryContentData(
            EditData(
                LogName="Enable GreenHouses",
                Target="Data/Buildings",
                Fields={
                    "Greenhouse":{
                        "Builder":"Robin",
                        "BuildCondition":"PLAYER_HAS_MAIL Host ccPantry,BUILDINGS_CONSTRUCTED Target Cabin,CAN_BUILD_FOR_CABINS Greenhouse" 
                    }
                }
            )
        )
        

        

        

        

