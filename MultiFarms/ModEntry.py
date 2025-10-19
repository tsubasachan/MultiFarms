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
                        "BuildCondition":"IS_MULTIPLAYER,BUILDINGS_CONSTRUCTED Target Cabin,CAN_BUILD_FOR_CABINS Greenhouse" 
                    }
                },
                When={
                    "HasFlag: hostPlayer": "ccPantry"
                }
            )
        )
        

        

        

        

