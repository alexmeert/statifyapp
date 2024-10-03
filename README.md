# Statify

Statify is a web application that allows users to track their Spotify listening habits, including their top tracks, artists, and albums. By integrating with the Spotify API, Statify provides users with an engaging platform to explore their music preferences and analyze their listening patterns over time.

## Features

- Spotify Authentication: Secure login via Spotify to personalize data.
- Top Music Stats: Displays user’s top tracks, artists, and albums.
- Time Range Filters: Filter stats based on short-term, medium-term, and long-term data.
- Responsive Design: Optimized for both desktop and mobile viewing.

## Technologies Used

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS (with responsive design)
- **Environment Variables:** Loaded using `python-dotenv`
- **API Requests:** Handled with the `requests` library
- **IDE:** I recommend using Visual Studio Code

## Requirements

To run this application, ensure you have the following installed:

- Python 3.8 or higher
- Flask
- Requests
- python-dotenv

## Installation

# 1. Clone the repository: 
- git clone https://github.com/alexmeert/statifyapp.git
- cd statifyapp

# 2. Set up an environment:
- Crete a file in your statify directory named ".env"
- This is where you'll add your environment variables
  
# 3. Install the required packages:
- pip install -r requirements.txt

# 4. Set up your environment variables:
- Go to the Spotify for Developers Website: https://developer.spotify.com
- Login with your Spotify account
- Click on your icon in the top right hand corner
- Click on dashboard
- Create a project
- Click on the project and then click settings
- Copy the client id and paste it as a string for your CLIENT_ID variable
- Below the client ID click on view client secret and paste the string into your .env file
- Your CLIENT_SECRET and APP_SECRET_KEY will both be set to the client secret
- Save your files

- CLIENT_ID = 'your_spotify_client_id'
- CLIENT_SECRET = your_spotify_client_secret
- APP_SECRET_KEY = your_app_secret_key

# 5. Run the application
- In the command prompt or your chosen IDE's terminal type `python app.py`
- CTRL + Click on either of the localhost links
- Login with Spotify
- See your stats!

## Feedback

If you need any assistance setting up Statify, please don't hesitate to reach out! Suggestions, questions, comments, and advice for improving are all welcome. Thank you for using Statify!
