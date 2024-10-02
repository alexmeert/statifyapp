import os
from dotenv import load_dotenv
import requests
import urllib.parse
from datetime import datetime, timedelta
from flask import Flask, jsonify, redirect, request, session, render_template


app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:5000/callback'

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

# Route for home page with a link to login
@app.route('/')
def index():
    return render_template('index.html')

# Login endpoint
@app.route('/login')
def login():
    scope = 'user-read-private user-read-email user-top-read user-read-recently-played'
    
    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'scope': scope,
        'redirect_uri': REDIRECT_URI,
        'show_dialog': True
    }

    auth_url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"
    
    return redirect(auth_url)

@app.route('/callback')
def callback():
    if 'error' in request.args:
        return jsonify({"error": request.args['error']})
    
    if 'code' in request.args:
        req_body = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
        
        response = requests.post(TOKEN_URL, data=req_body)
        token_info = response.json()
        
        session['access_token'] = token_info['access_token']
        session['refresh_token'] = token_info['refresh_token']
        session['expires_at'] = datetime.now().timestamp() + token_info['expires_in']
        
        return redirect('/top-items')


@app.route('/top-items')
def get_top_items():
    if 'access_token' not in session:
        return redirect('/login')
    
    if datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')
    
    headers = {
        'Authorization': f"Bearer {session['access_token']}"
    }

    user_profile = requests.get(API_BASE_URL + 'me', headers=headers).json()
    username = user_profile.get('display_name')
    user_picture = user_profile.get('images')[0]['url'] if user_profile.get('images') else None

    time_range = request.args.get('time_range', 'short_term')  # default to 'medium_term'
    
    top_tracks = requests.get(API_BASE_URL + f'me/top/tracks?limit=10&time_range={time_range}', headers=headers).json()
    top_artists = requests.get(API_BASE_URL + f'me/top/artists?limit=10&time_range={time_range}', headers=headers).json()
    
    top_albums = []
    album_names = set()  # Keep track of unique album names to avoid duplicates
    offset = 0  # For fetching more tracks if needed

    # Loop through the top tracks and extract album information
    while len(top_albums) < 10 and offset < 150:  # Attempt to get more albums up to 150 tracks
        for item in top_tracks['items']:
            album = item['album']
            album_name = album['name']
            artist_name = ', '.join([artist['name'] for artist in item['artists']])  # Get the artist names
            total_tracks = album['total_tracks']  # Check number of tracks in the album

            # Add album only if it has more than one track and it's not already added
            if total_tracks > 1 and album_name not in album_names:
                top_albums.append({
                    'name': album_name,
                    'images': album['images'],
                    'artist': artist_name
                    })
                album_names.add(album_name)  # Mark the album as added

            # Stop once we have 10 albums
            if len(top_albums) == 10:
                break

        # If less than 10 albums found, fetch more tracks
        if len(top_albums) < 10:
            offset += 50  # Increase offset to get the next set of tracks
            top_tracks_url = API_BASE_URL + f'me/top/tracks?limit=50&offset={offset}&time_range={time_range}'
            top_tracks = requests.get(top_tracks_url, headers=headers).json()

    # If we couldn't find 10 albums, return a message
    if len(top_albums) < 10:
        top_albums_message = "Not enough multi-track albums found."
    else:
        top_albums_message = None
        
    # Only pass the top 10 tracks
    top_tracks_display = top_tracks['items'][:10]

    for artist in top_artists['items']:
        artist['genres'] = ', '.join(artist.get('genres', []))  # Combine genres into a string
    
    # Pass top tracks, top artists, and top albums to the template
    return render_template('top_items.html',
                           username=username,
                           user_picture=user_picture,
                           top_tracks=top_tracks_display, 
                           top_artists=top_artists['items'], 
                           top_albums=top_albums,
                           top_albums_message=top_albums_message,
                           time_range=time_range)


@app.route('/refresh-token')
def refresh_token():
    if 'refresh_token' not in session:
        return redirect('/login')
    
    if datetime.now().timestamp() > session['expires_at']:
        req_body = {
            'grant_type': 'refresh_token',
            'refresh_token': session['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
        
        response = requests.post(TOKEN_URL, data=req_body)
        new_token_info = response.json()
        
        session['access_token'] = new_token_info['access_token']
        session['expires_at'] = datetime.now().timestamp() + new_token_info['expires_in']
        
        return redirect('/top-items')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
