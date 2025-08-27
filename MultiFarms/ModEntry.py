from StardewValley import Manifest, Helper, ContentPatcher

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

        

        

        

        

