import requests

class SpotifyApi:

    def __init__(self,genre):        
        self.genre = genre
        self.url_recomend = 'https://api.spotify.com/v1/recommendations?'
        self.CLIENT_ID = 'f4bc7c25fc774b548d099b53071e41df'
        self.CLIENT_SECRET = 'b7f2822f7aab415ca2e2cc6a5d7a8bfb'
        self.AUTH_URL = 'https://accounts.spotify.com/api/token'

    def get_track(self):
        limit=1
        query = f'{self.url_recomend}limit={limit}&seed_genres={self.genre}'

        auth_response = requests.post(self.AUTH_URL, {
            'grant_type': 'client_credentials',
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET,
        })
        auth_response_data = auth_response.json()
        access_token = auth_response_data['access_token']

        headers = {
            'Authorization': 'Bearer {token}'.format(token=access_token)        
        }

        response=requests.get(url=query,headers=headers)
        json_response = response.json()

        if json_response['tracks']:
            for i in json_response['tracks']:
                track=i['name']
                artist=i['artists'][0]['name']
                url=i['external_urls']['spotify']
        else:
            track=('Music genre {0} does not exists in Spotify database'.format(self.genre))
            artist=('Music genre {0} does not exists in Spotify database'.format(self.genre))
            url=('Music genre {0} does not exists in Spotify database'.format(self.genre))
        return track,artist,url   
