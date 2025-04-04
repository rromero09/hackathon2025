def services_data():
    with open(r"c:\Users\rafae\code\hack2025\data\services_json.txt", "r") as file:
        services_data = json.load(file)
    return services_data
    