import json
import os

TOKEN_SIZE = 609
START_ID = 0
OUTPUT_DIR = "./json"

NAME = "The Keys"
DESC = "Key of 7 Angels X 7 Devils collection. This is key for get WL to 7 Angels X 7 Devils. Every ranks haven't same WL. 609 collectible keys."
IMG_0 = "https://diewland.github.io/the-keys/assets/99b77c8123e50e8b0a8d420e7a0fab6f.png"
IMG_1 = "https://diewland.github.io/the-keys/assets/d52c0b8a5ec6f860fc0041d91604aa33.png"
IMG_COVER = IMG_0
ATTRS = [
    {
      "trait_type": "Rarity",
      "value": "***",
    },
]
ENGINE = "Jigsaw Engine"

metadata = {
  "name": "***",
  "description": DESC,
  "image": "***",
  "attributes": ATTRS,
  "compiler": ENGINE,
}

for id in range(0, TOKEN_SIZE):
    metadata["name"] = "{} #{}".format(NAME, id)
    if id == 0:
        metadata["image"] = IMG_0
        metadata["attributes"][0]["value"] = "Ultra Rare"
    elif id == 1:
        metadata["image"] = IMG_1
        metadata["attributes"][0]["value"] = "Ultra Rare"
    else:
        metadata["image"] = IMG_COVER
        metadata["attributes"][0]["value"] = "Unrevealed"
    with open("./{}/{}.json".format(OUTPUT_DIR, START_ID + id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
