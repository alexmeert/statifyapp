# Statify

Statify is a web application that allows Spotify users to gain insights into their listening habits. Users can view their time spent listening, most played albums, top 5 songs, and filter their statistics by time periods (week, month, year, or all time). The application is built using the Spotify API to display personalized listening data.


# Features
Time Spent Listening: Get a breakdown of the time spent listening to music on Spotify.
Top Albums and Songs: Discover your most played albums and top 5 songs.
Time Filters: View your stats by week, month, year, or all-time.
Interactive UI: Easy-to-use interface with detailed stats.
Demo
Check out a live demo here.

# Installation
To get a local copy up and running, follow these simple steps:

# Prerequisites
You need to have Node.js installed.
You will need a Spotify Developer account to get your API credentials.
Spotify API Setup
Go to the Spotify Developer Dashboard.
Create a new application to get your CLIENT_ID and CLIENT_SECRET.
Set up the redirect URI for your application (usually http://localhost:3000 during development).

# Installation Steps
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/statify.git
Navigate to the project directory:
bash
Copy code
cd statify
Install dependencies:
bash
Copy code
npm install
Create a .env file in the root of your project and add the following:
bash
Copy code
SPOTIFY_CLIENT_ID=your-client-id
SPOTIFY_CLIENT_SECRET=your-client-secret
REDIRECT_URI=http://localhost:3000/callback
Run the development server:
bash
Copy code
npm start
Visit http://localhost:3000 in your browser.
Usage
Log in with your Spotify account.
View your stats such as time spent listening, top albums, and top songs.
Filter the data by time (week, month, year, or all-time).
Technologies Used
React: Frontend framework.
Spotify API: For accessing user listening data.
Node.js: Backend server.
CSS: Styling the interface.

Feel free to reach out if you have any questions or want to contribute!
