""" import requests

# Documentation: https://www.reddit.com/dev/api/
# Endpoint: https://www.reddit.com/r/{subreddit}/.json
subreddit = "python"
url = f"https://www.reddit.com/r/{subreddit}/.json"

response = requests.get(url)
data = response.json()
print(data)  # This will print the JSON response containing posts from the Python subreddit
 """

import requests
import time
import json
import csv

subreddit = "python"
url = f"https://www.reddit.com/r/{subreddit}/.json"

def get_data_with_backoff(url):
    response = requests.get(url)
    if response.status_code == 429:
        print("Rate limit exceeded. Waiting before retrying...")
        time.sleep(30)  # Wait for 60 seconds before retrying
        return get_data_with_backoff(url)  # Retry the request
    elif response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

data = get_data_with_backoff(url)
if data:
    #print(data)
    # Save JSON data to data.json
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    print("JSON data saved to data.json")

    # Save CSV data to data.csv
    with open("data.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        # Write header
        writer.writerow(["Title", "Author", "Score"])
        # Write data
        for post in data["data"]["children"]:
            title = post["data"]["title"]
            author = post["data"]["author"]
            score = post["data"]["score"]
            writer.writerow([title, author, score])
    print("CSV data saved to data.csv")

