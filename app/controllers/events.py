import json

def dining_data():

    with open(r"c:\Users\rafae\code\hack2025\data\dining_json.txt", "r") as file:
        dining_data = json.load(file)
    return dining_data