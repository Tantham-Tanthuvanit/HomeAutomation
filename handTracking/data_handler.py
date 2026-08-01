import json
from pathlib import Path

def dumpHands(hands):
    Path("data").mkdir(exist_ok=True)
    with open("./data/hand_data.json", "w", encoding="utf-8") as file:
        json.dump(hands,file,indent=4)