import json
import os

TOKEN_SIZE = 609
START_ID = 0
OUTPUT_DIR = "./json"

NAME = "The Keys"
DESC = "Key of 7 Angels X 7 Devils collection. This is key for get WL to 7 Angels X 7 Devils. Every ranks haven't same WL. 609 collectible keys."
IMG = "https://diewland.github.io/the-keys/assets/99b77c8123e50e8b0a8d420e7a0fab6f.png"
ATTRS = [
    {
      "trait_type": "Rarity",
      "value": "Unrevealed",
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
    metadata["image"] = IMG
    with open("./{}/{}.json".format(OUTPUT_DIR, START_ID + id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
