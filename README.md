# Statify

Statify is a web application that allows users to track their Spotify listening habits, including their top tracks, artists, and albums. By integrating with the Spotify API, Statify provides users with an engaging platform to explore their music preferences and analyze their listening patterns over time.

## Features

- User authentication with Spotify
- Display of user's top tracks, artists, and albums
- Ability to filter listening statistics by different time ranges (short-term, medium-term, long-term)
- A responsive design that works well on both desktop and mobile devices

## Technologies Used

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS (with responsive design)
- **Environment Variables:** Loaded using `python-dotenv`
- **API Requests:** Handled with the `requests` library

## Requirements

To run this application, ensure you have the following installed:

- Python 3.8 or higher
- Flask
- Requests
- python-dotenv

## Installation

1. Clone the repository
  git clone https://github.com/alexmeert/statifyapp.git
  cd statifyapp
2. Set up an environment
3. Install the required packages
  pip install -r requirements.txt
4. Set up your environment variables
  CLIENT_ID=your_spotify_client_id
  CLIENT_SECRET=your_spotify_client_secret
  APP_SECRET_KEY=your_app_secret_key
5. Run the application
   python app.py

## File Structure

## Feedback
