import requests
import random
import json

# Function that fetch all the rps objects
def fetch_rps_objects():
    url = "https://rps101.pythonanywhere.com/api/v1/objects/all"
    
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check if the response status is OK (200)
        if response.status_code == 200:
            # Load the JSON response text into a Python dictionary
            data = json.loads(response.text)
            
            # Loop through all data of the response
            for object in data:
                print(f"{object}")
                
            return data
        
    except Exception as e:
        print(f"An Exception Occured {e}")
        return 

# Function to choose the object of p1
def choose_object_p1(objects):
    object_p1 = input(f"\nEnter the object you choose: ").strip().capitalize()
    
    if object_p1 not in objects:
        print(f"Invalid object. Please try again.")
        return choose_object_p1(objects)
    
    return object_p1

# Function to randomly choose the object of computer
def choose_object_computer(objects):
    return random.choice(objects)

# Function of the result of the match 
def fetch_match_result(p1, computer):
    # Pass the return variable of the p1 and computer
    url = f"https://rps101.pythonanywhere.com/api/v1/match?object_one={p1}&object_two={computer}"
    
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Check if the response status is OK (200)
        if response.status_code == 200:
            # Load the JSON response text into a Python dictionary
            data = json.loads(response.text)
            
            # access the value of the key of dict "data"
            print(f"\nWinner: {data["winner"]}\nLoser: {data["loser"]}\nOutcome: {data["outcome"]}")
            
            if p1.capitalize() == data["winner"]:
                print("\nPlayer 1 Wins.")
            elif computer.capitalize() == data["winner"]:
                print(f"\nComputer Wins.")
        
    except Exception as e:
        print(f"An Exception Occured {e}")
        return

def main():
    while True:
        # Get the rps objects
        rps_objects = fetch_rps_objects()
        # Get the return value of p1
        p1 = choose_object_p1(rps_objects).lower()
        # Get the return value of computer
        computer = choose_object_computer(rps_objects).lower()
        
        print(f"\nPlayer 1 choose: {p1.capitalize()}")
        print(f"Computer choose: {computer.capitalize()}")
        
        # Pass the return value to the match reesult
        fetch_match_result(p1, computer)
    
if __name__ == "__main__":
    main()