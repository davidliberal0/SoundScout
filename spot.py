import os
from dotenv import load_dotenv
import requests
import base64

load_dotenv()

# hold credentials - store in seperated .env file -
# uniquely identifies app making requests
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Base64 encode the client ID and client secret
client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
client_credentials_base64 = base64.b64encode(client_credentials.encode())


# client_id & client_secret  ---request---> Access Token


# function for getting token
def get_token():
    # Request the access token
    token_url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {client_credentials_base64.decode()}'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(token_url, data=data, headers=headers)

    if response.status_code == 200:
        access_token = response.json()['access_token']
        print("Access token obtained successfully.")
        return access_token
    else:
        print("Error obtaining access token.")
        exit()
    


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    # get first artist that appears in the search
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = requests.get(query_url, headers=headers)
    json_result = result.json()
    print(json_result)


token = get_token()

search_for_artist(token, "khalid")
