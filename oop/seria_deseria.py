import json
import pickle

data = {'name': 'Alice', 'age': 30, 'city': 'Kampala'}

# serialize the object to a json string
json_string = json.dumps(data)

# ÷write the json string to a file

with open('data.json', 'w') as file:
    json.dump(data, file)
print("Data Serialized\n")

# Deserialization
data = json.loads(json_string)

with open('data.json', 'r') as file:
    data = json.load(file)
print('Deserialized data:', data)

# data = {'name': 'Alice', 'age': 30, 'city': 'Kampalas'}

# Example 1, using the pickle module

# serialize the object

with open('pickle.pkl', 'wb') as file:
    pickle.dump(data, file)

# pickle deserialization

with open('pickle.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
print('pickle deserialization:', loaded_data)


# Task solution
def process_json(data: dict, filename: str) -> dict:
    # serialize to json file
    with open(filename, 'w') as file:
        json.dump(data, file)
    
    # Deserialize from json file
    with open(filename, 'r') as file:
        exercise_data = json.load(file)
        return exercise_data

data = {
    "name": "Ibrahim", "friend": "Mofolashayor", "career": "SWE"
}

filename = "topzee.json"

info = process_json(data, filename)
print("Task Data:", info)