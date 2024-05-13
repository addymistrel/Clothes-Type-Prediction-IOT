import requests

# Define Adafruit API endpoint
adafruit_api_url = "https://io.adafruit.com/api/v2"

# Your Adafruit username and AIO key
username = "group_4_cseb1"
aio_key = "aio_FWsB87PoK9SfXXgBbsfNjChwnPhz"

# Function to get details from Adafruit server
def get_details(feed_key):
    # Construct the URL for the feed
    feed_url = f"{adafruit_api_url}/{username}/feeds/{feed_key}"
    
    # Make GET request to retrieve feed details
    response = requests.get(feed_url, headers={"X-AIO-Key": aio_key})
    
    # Check if request was successful
    if response.status_code == 200:
        # Extract and return the feed details
        return response.json()
    else:
        # Print error message if request was unsuccessful
        print(f"Failed to retrieve details for feed '{feed_key}'. Status code: {response.status_code}")
        return None

# Example usage
# if _name_ == "_main_":
#     # Example feed key
#     feed_key = "temperature"
    
#     # Get details for the specified feed
#     feed_details = get_details(feed_key)
    
#     # Print the feed details
#     if feed_details:
#         print("Feed Details:")
#         for k in feed_details:
#             print("{} - {}".format(k,feed_details[k]))