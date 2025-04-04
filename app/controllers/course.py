import json
from mongoquery import Query

def course_data():
    with open(r"c:\Users\rafae\code\hack2025\data\courses_json.txt", "r") as file:
        return json.load(file)

def get_professor_teaching_course(course_name: str) -> str:
    data = course_data()

    # Query for matching course code (e.g., "CS152")
    query = Query({"code": course_name.upper()})
    filtered = [item for item in data if query.match(item)]

    # Return professor(s)
    if not filtered:
        return "No professor found for that course."

    # Some courses might have multiple professors
    professors = set(item["professor"] for item in filtered if "professor" in item)
    return ", ".join(sorted(professors))

if __name__ == "__main__":
    print(get_professor_teaching_course("CS160"))  # Example test case
