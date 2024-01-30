Youtube Video Downloader with Flask

This is a simple web application built with Flask that allows you to download YouTube videos. The application provides a user-friendly interface where you can input a YouTube video URL, get information about the video, and download it in MP4 format.

Prerequisites
Before you start, make sure you have the following installed on your machine:

1. Python
2. Flask
3. pytube (YouTube video downloader library)

Installation
1. Clone the repository:
git clone https://github.com/yechika/yt_dwnldr
cd your-repo

2. Install the required dependencies:
pip install Flask pytube

Usage
1. Run the Flask application:
python app.py
2. Open your web browser and go to http://127.0.0.1:5000/.
3. Input a YouTube video URL in the provided form and submit.
4. Optionally, choose the desired video quality.
5. Click the "Download" button, and the video will be saved in the #Download folder.

project-root/
|-- templates/
|   |-- index.html
|-- static/
|   |-- style.css
|-- app.py
|-- #Download/
|-- README.md

Notes
The application uses Flask for the web framework and pytube to interact with the YouTube API.
The #Download folder is created in the project root to store the downloaded videos.
The Flask application serves the web interface, and the downloaded videos are saved in the #Download folder.

Disclaimer
This project is for educational purposes only. Make sure to comply with YouTube's terms of service and respect the intellectual property rights of content creators.
Feel free to contribute, report issues, or suggest improvements!
