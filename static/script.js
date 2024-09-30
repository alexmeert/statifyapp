document.addEventListener('DOMContentLoaded', function() {
    // Fetch Top Tracks
    fetch('/top_tracks')
        .then(response => response.json())
        .then(data => {
            const topTracksDiv = document.getElementById('top-tracks');
            let topTracks = data.top_tracks.map(track => `<li>${track.name} by ${track.artists[0].name}</li>`).join('');
            topTracksDiv.innerHTML = `<h2>Top Tracks</h2><ul>${topTracks}</ul>`;
        })
        .catch(error => console.error('Error fetching top tracks:', error));

    // Fetch Top Artists
    fetch('/top_artists')
        .then(response => response.json())
        .then(data => {
            const topArtistsDiv = document.getElementById('top-artists');
            let topArtists = data.top_artists.map(artist => `<li>${artist.name}</li>`).join('');
            topArtistsDiv.innerHTML = `<h2>Top Artists</h2><ul>${topArtists}</ul>`;
        })
        .catch(error => console.error('Error fetching top artists:', error));

    // Fetch Top Albums
    fetch('/top_albums')
        .then(response => response.json())
        .then(data => {
            const topAlbumsDiv = document.getElementById('top-albums');
            if (data.top_albums_message) {
                topAlbumsDiv.innerHTML = `<h2>Top Albums</h2><p>${data.top_albums_message}</p>`;
            } else {
                let topAlbums = data.top_albums.map(album => `<li>${album.name}</li>`).join('');
                topAlbumsDiv.innerHTML = `<h2>Top Albums</h2><ul>${topAlbums}</ul>`;
            }
        })
        .catch(error => console.error('Error fetching top albums:', error));
        
});

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyB-kVfZeq66lsB_S9u7OocxemRt_swDmak",
  authDomain: "statify-7ac33.firebaseapp.com",
  projectId: "statify-7ac33",
  storageBucket: "statify-7ac33.appspot.com",
  messagingSenderId: "516951776763",
  appId: "1:516951776763:web:304bdfbe378f1ef7873f5e",
  measurementId: "G-HHY084D4DW"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);