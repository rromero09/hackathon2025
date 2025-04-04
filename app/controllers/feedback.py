import json
def feedback_data():
    with open(r"c:\Users\rafae\code\hack2025\data\feedback_json.txt", "r") as file:
        feedback_data = json.load(file)
    return feedback_data
    