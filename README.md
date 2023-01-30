Shodan API Example
This code example shows how to use the Shodan API to search for information on the Internet. The Shodan API provides access to a search engine that can be used to find devices and services on the Internet.

Requirements
To use this code, you need to have:

A Shodan API key. You can sign up for a free account on the Shodan website.

The requests library installed. You can install it using pip with the following command:

Copy code
pip install requests
Usage
To use the code, follow these steps:

Replace YOUR_SHODAN_API_KEY with your actual Shodan API key.

Change the query variable to the search query you want to make. The search query should be a string that describes what you are looking for. For example, to search for open webcams, you can set the query variable to "webcam".

Run the code. The code will make a GET request to the Shodan API and retrieve the results of the search query. The results will be printed to the console.

Example
Here's an example of how you can use the code to search for open webcams:

python
Copy code
import requests

# Replace YOUR_SHODAN_API_KEY with your actual API key
api_key = "YOUR_SHODAN_API_KEY"

# Set the API endpoint
endpoint = "https://api.shodan.io/shodan/host/search"

# Set the query to search for open webcams
query = "webcam"

# Make the API request
response = requests.get(endpoint, params={"key": api_key, "query": query})

# Check if the API request was successful
if response.status_code == 200:
    # Get the results from the API response
    results = response.json()["matches"]
    # Print the number of results
    print(f"Number of results: {len(results)}")
    # Print information about the first result
    first_result = results[0]
    print("Information about the first result:")
    print(f"IP address: {first_result['ip_str']}")
    print(f"Port: {first_result['port']}")
    print(f"Organization: {first_result['org']}")
    print(f"Location: {first_result['location']}")
else:
    # If the API request was not successful, print an error message
    print("Error accessing the API")
In this example, the code searches for open webcams on the Internet and retrieves information about the results. The information includes the IP address, port, organization, and location of the devices that have open webcams.

Responsible Use
It is important to use the Shodan API responsibly and in accordance with the Shodan API Terms of Service. You should not use the Shodan API to perform actions that could harm others or violate their privacy. You should also respect the terms of service of the websites that you access using the Shodan API.

For more information on how to use the Shodan API responsibly
