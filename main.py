import requests

# Replace YOUR_SHODAN_API_KEY with your actual API key
api_key = "YOUR_SHODAN_API_KEY"

# Set the API endpoint
endpoint = "https://api.shodan.io/shodan/host/search"

# Set the query to search for anything on the site change the search you would like to make here... "CHANGE_YOUR_QUERY_HERE"
query = "CHANGE_YOUR_QUERY_HERE"

# Make the API request
response = requests.get(endpoint, params={"key": api_key, "query": query})

# Check if the API request was successful
if response.status_code == 200:
    # Get the results from the API response
    results = response.json()["matches"]
    # Print the number of results
    print(f"Number of results: {len(results)}")
    # Print information about the first result
    first_result = results[10]
    print("Information about the first result:")
    print(f"IP address: {first_result['ip_str']}")
    print(f"Port: {first_result['port']}")
    print(f"Organization: {first_result['org']}")
    print(f"Location: {first_result['location']}")
else:
    # If the API request was not successful, print an error message
    print("Error accessing the API")
