import json
from mongoquery import Query

def dining_data():
    with open(r"c:\Users\rafae\code\hack2025\data\dining_json.txt", "r") as file:
        dining_data = json.load(file)
    return dining_data

def study_spaces_data():
    with open(r"c:\Users\rafae\code\hack2025\data\study_spaces_json.txt", "r") as file:
        study_spaces_data = json.load(file)
    return study_spaces_data

def get_highest_occupancy_at_19() -> str:
    data = study_spaces_data()

    
    query = Query({"avg_occupancy_weekday": {"$exists": True}})
    filtered = [item for item in data if query.match(item)]

    # Get the item with the highest occupancy at index 11 (19:00)
    busiest = max(
        filtered,
        key=lambda x: int(x["avg_occupancy_weekday"].split(",")[11]) # since values are split in comas T.T
    )

    return busiest["name"]

if __name__ == "__main__":
    print(get_highest_occupancy_at_19())  # Should return: Library