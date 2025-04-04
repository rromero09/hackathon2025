import json
def recreation_data():
    with open(r"c:\Users\rafae\code\hack2025\data\recreation_json.txt", "r") as file:
        recreation_data = json.load(file)
    return recreation_data
    
    
