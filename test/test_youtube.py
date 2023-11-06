# Import the requests library
import requests
from pprint import pprint
# Define a function to check if a YouTube video exists
def youtube_video_exists(video_id):
    # Set response status pattern
    pattern = '"playabilityStatus":{"status":"ERROR","reason":"Video unavailable"'
    # Construct the YouTube video URL
    video_url = f"http://img.youtube.com/vi/{video_id}/0.jpg"
    # Send a GET request to the URL
    response = requests.get(video_url, allow_redirects=False)

    # Return True if the response status code is 200 (OK), False otherwise
    return False if response.status_code == 404 else True

# Define a pytest function to test the youtube_video_exists function
def test_youtube_video_exists():
    # Use the pytest assert statement to check if the function returns True for a valid video ID
    assert youtube_video_exists("dQw4w9WgXcQ") == True
    # Use the pytest assert statement to check if the function returns False for an invalid video ID
    assert youtube_video_exists("invalid") == False
