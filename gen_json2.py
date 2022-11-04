import json, os, glob, random, hashlib
from datetime import datetime
from pprint import pprint as pp
 
NAME = "The Keys"
DESC = "Key of 7 Angels X 7 Devils collection. This is key for get WL to 7 Angels X 7 Devils. Every ranks haven't same WL. 609 collectible keys."
IMG = "https://diewland.github.io/the-keys/assets/{}.png"
ENGINE = "Jigsaw Engine"

SRC_PATH = "./temp/*/*.png"
OUTPUT_DIR = "./json2"
SHUFFLE_TIME = 99

# init chunk data
chunk = [ p for p in glob.glob(SRC_PATH) ]

# pick first and last items from chunk
item_first = "./temp/Ultra Rare/TheKeys#0.png"
item_last = "./temp/Ultra Rare/TheKeys#608.png"
chunk.remove(item_first)
chunk.remove(item_last)

# shuffle
for rnd in range(1, SHUFFLE_TIME+1):
    random.shuffle(chunk)

# rebuild chunk
chunk = [ item_first, item_last ] + chunk

# craft metadata
metadata = []
for id, p in enumerate(chunk):
    name = "{} #{}".format(NAME, id)
    img_name = IMG.format(hashlib.md5(p.encode('utf-8')).hexdigest())
    rarity = p.split('/')[2]
    o = {
        "name": "***",
        "description": DESC,
        "image": "***",
        "attributes": [
            {
              "trait_type": "Rarity",
              "value": "***",
            },
        ],
        "compiler": ENGINE,
    }
    o["name"] = name
    o["image"] = img_name
    o["attributes"][0]["value"] = rarity
    metadata.append(o)

#pp(metadata)

# write to file
for id, row in enumerate(metadata):
    with open("./{}/{}.json".format(OUTPUT_DIR, id), "w") as f:
        json.dump(row, f, ensure_ascii=False)
