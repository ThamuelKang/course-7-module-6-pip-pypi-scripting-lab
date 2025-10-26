from datetime import datetime
import os
import requests


def generate_log(data):
    # Validate input is a list
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    
    # Generate filename with underscore
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write the provided data to file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    generate_log(None)
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
