import json
from mongoquery import Query

def dining_data():
    with open(r"c:\Users\rafae\code\hack2025\data\dining_json.txt", "r") as file:
        return json.load(file)

def get_dining_with_shortest_lunch_wait() -> str:
    data = dining_data()

    
    query = Query({"wait_time_lunch": {"$exists": True}})
    filtered = [item for item in data if query.match(item)]

    
    shortest = min(filtered, key=lambda x: x["wait_time_lunch"])

    
    return shortest["name"]
def get_dining_with_longest_lunch_wait() -> str:
    data = dining_data()

    
    query = Query({"wait_time_lunch": {"$exists": True}})
    filtered = [item for item in data if query.match(item)]

    
    longest= max(filtered, key=lambda x: x["wait_time_lunch"])

    
    return longest["name"]

if __name__ == "__main__":
    #test
    print(get_dining_with_longest_lunch_wait()) 
