import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_name")
args = parser.parse_args()

def process(file_name):
    pools = []

    with open(file_name) as f:
        lines = f.read().splitlines()

    for line in lines:
        item_name, amount, chance = line.split()
        pools.append({
            "rolls": {
                "type": "minecraft:binomial",
                "n": int(amount),
                "p": float(chance),
            },
            "entries": [
                {
                    "type": "minecraft:item",
                    "name": item_name,
                }
            ]
        })

    base, _ext = os.path.splitext(file_name)
    with open(base + ".json", "w") as f:
        json.dump({
            "pools": pools,
        }, f, indent=4)

process(args.file_name)
