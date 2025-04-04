from controllers.dining import get_dining_with_shortest_lunch_wait
from controllers.dining import get_dining_with_longest_lunch_wait
from controllers.course import get_professor_teaching_course
def chatbox():
    while True:
        print("Welcome to the Chatbot!") 
        input_text = input("You: ")
        if input_text.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("Chatbot: I'm here to help you!")
            if input_text == "Which dining hall has the shortest wait time for lunch":
                result = get_dining_with_shortest_lunch_wait()
                print(f"Chatbot: The dining hall with the shortest wait time for lunch is {result}.")
            elif input_text == "Which dining hall has the longest wait time for lunch":
                
                result = get_dining_with_longest_lunch_wait()
                print(f"Chatbot: The dining hall with the longest wait time for lunch is {result}.")
            elif  input_text.startswith("Which professor teaches"):
                course_code = input_text.split("teaches")[-1].strip()
                result = get_professor_teaching_course(course_code)
                print(f"Chatbot: The professor teaching {course_code} is {result}.")
                


# Calling to main box
if __name__ == "__main__":
    chatbox()