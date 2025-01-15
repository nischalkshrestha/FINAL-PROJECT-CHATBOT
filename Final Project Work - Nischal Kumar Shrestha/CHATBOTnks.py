import random
import json

def welcome_banner():
    """Welcome Banner"""

    print("\n\n==================================================")
    print("   WELCOME TO THE POPPLETON UNIVERSITY CHATBOT       ")
    print("==================================================\n")

def greet_user():
    """Greets the user and asks for their name."""

    username = input("Hello! What's your name? ")
    print(f"Hello '{username}', nice to meet you! ")
    return username

def get_agent():
    """Chooses a random agent name from a list and displays it."""

    agent = ["GIAN", "POPPLE", "NOBITA", "DORAEMON","POPPU"]
    agent_name = random.choice(agent)
    print("___________________________________________________________________________________________\n")
    print(f"My name is '{agent_name}', and I'm here to answer your questions! \n")
    return agent_name

def load_responses(file_path):
    """Loads responses from a JSON file."""

    with open(file_path, 'r') as file: 
        return json.load(file)

def store_conversation(username, user_input, response):
    """Logs the conversation to a file."""

    with open('chat_botnks.txt', 'a') as log_file: #Append Mode to keep adding data
        log_file.write(f"------------------ Conversation Log ------------------\n")
        log_file.write(f"User '{username}': {user_input}\n")
        log_file.write(f"Agent: {response}\n")
        log_file.write(f"------------------------------------------------------\n\n")

def respond_to_user(user_input, agent_name, username, responses):
    """Responds to the user's input based on keywords in the JSON file."""

    user_input = user_input.lower() #Lowercase

    for keyword, keyword_responses in responses.items():
        if keyword in user_input:
            response = random.choice(keyword_responses)
            store_conversation(username, user_input, response)  # Log the question and answer
            return f"{agent_name}: {response}\n"
    
    # If no keyword matches, return a random generic response
    random_responses = [
        f"{agent_name}: I'm sorry {username}, can you clarify?\n",
        f"{agent_name}: Sorry, I'm not sure about that {username}. Ask me something else!\n",
        f"{agent_name}: Let me think... Sorry, I don't know that one also!\n"
    ]
    response = random.choice(random_responses)
    store_conversation(username, user_input, response)  # Log the question and answer
    return response

def chat_bot():
    """Runs the chatbot program."""

    welcome_banner()
    username = greet_user()
    agent_name = get_agent()

    # Load responses from JSON file
    responses = load_responses('responses.json')

    print(f"What do yo want to know about Poppleton University. Please feel free to ask me anything :)")
    print("___________________________________________________________________________________________\n")

    while True:
        user_input = input(f"{username}: ")

        # Check for exit commands
        if user_input in ["bye", "exit", "quit", "leave", "end", "byebye","no"]:
            print(f"{agent_name}: It was great chatting with you, {username}! Have a wonderful day!\n\n")
            store_conversation(username, user_input, f"{agent_name}: It was great chatting with you, {username}! Have a wonderful day!")  # Log exit
            break

        response = respond_to_user(user_input, agent_name, username, responses)
        print(response)

chat_bot()
