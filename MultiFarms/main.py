from ModEntry import ModEntry
from StardewValley import Manifest

manifest=Manifest(
    Name="MultiFarms",
    Author="alichan",
    Version="0.4",
    Description="Add multi Farms to Stardew Valley",
    UniqueID="alichan.MultiFarms"
)
mod=ModEntry(manifest=manifest)

mod.write()
