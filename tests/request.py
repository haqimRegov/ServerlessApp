import requests

def send_request():
    # Replace "your_endpoint_url" with the actual URL of your endpoint
    endpoint_url = "http://127.0.0.1:5000/add_user"

    # Sample dictionary to send as JSON data
    data_to_send = {
        "nric": "21332100183",
        "username":"Irfan",
        "age":"27",
        "weight": "70",
        "height":"170",
    }

    try:
        # Send a POST request with the JSON data
        response = requests.post(endpoint_url, json=data_to_send)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Request successful!")
            print("Response content:", response.text)
        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions as e:
        print("Error sending request:", e)

# Example usage:
# send_request()

def send_request_getBmi():
    # Replace "your_endpoint_url" with the actual URL of your endpoint
    endpoint_url = "http://127.0.0.1:5000/getBmi/99132300183"

    # Sample dictionary to send as JSON data
    data_to_send = {
        "nric": "92312313132"
    }

    try:
        # Send a POST request with the JSON data
        response = requests.get(endpoint_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Request successful!")
            print("Response content:", response.text)
            print(response.json())
        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions as e:
        print("Error sending request:", e)

# Example usage:
send_request_getBmi()