import json
import requests

def send_post_requests(data_list, url):
  for item in data_list:
    response = requests.post(url, json={"data": item})  # Send POST request with JSON data
    if response.status_code == 200:
      print(f"Successfully sent data for object: {item}")
    else:
      print(f"Error sending data for object: {item}. Status code: {response.status_code}")

# Replace with the path to your JSON file
masterItem="products"
json_file_path = masterItem+"Ex.json"
post_url = "http://localhost:3000/master/"+masterItem

try:
  with open(json_file_path, "r") as f:
    data_list = json.load(f) 
  

  # Send POST requests for each object
  send_post_requests(data_list, post_url)

except FileNotFoundError:
  print(f"Error: JSON file '{json_file_path}' not found.")
except json.JSONDecodeError:
  print(f"Error: Could not parse the JSON file '{json_file_path}'.")
except Exception as e:
  print(f"An unexpected error occurred: {e}")
