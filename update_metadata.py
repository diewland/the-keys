import json
from pprint import pprint as pp

for id in range(0, 608+1):
    path = "./json/{}.json".format(id)

    # load json
    data = json.load(open(path))
    attrs = data["attributes"]
    rarity = attrs[0]["value"]

    if rarity == "Normal":
        attrs.append({
            "trait_type": "WL 7Angelsx7Devils",
            "value": "1",
        })
    elif rarity == "Rare":
        attrs.append({
            "trait_type": "WL 7Angelsx7Devils",
            "value": "2",
        })
    elif rarity == "Super Rare":
        attrs.append({
            "trait_type": "WL 7Angelsx7Devils",
            "value": "2 (you can choose 1Angel and 1Devil)",
        })
    elif rarity == "Ultra Rare":
        attrs.append({
            "trait_type": "WL 7Angelsx7Devils",
            "value": "2 (you can choose 1Angel and 1Devil)",
        })
        attrs.append({
            "trait_type": "WL The land",
            "value": "1",
        })
    else:
        raise Exception("unknown rarity: {}".format(rarity))

    #pp(data)

    with open(path, "w") as f:
        json.dump(data, f)
