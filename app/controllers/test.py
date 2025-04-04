from mongoquery import Query
import json

def get_all_courses():
    
    with open(r"c:\Users\rafae\code\hack2025\data\courses_json.txt", "r") as file:
        courses_data = json.load(file)

    # Proper use of $exists
    query = Query({"title": {"$exists": True}})
    all_courses = [course for course in courses_data if query.match(course)]

    # Print each course
    for course in all_courses:
        print(course)

if __name__ == "__main__":
    get_all_courses()
