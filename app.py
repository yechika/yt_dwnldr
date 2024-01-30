#leinnn
from flask import Flask, render_template, request, session
from pytube import YouTube
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

download_path = os.path.join(os.getcwd(), '#Download')  #Path/Nama folder atur sendiri

def get_video_info(link):
    try:
        yt = YouTube(link)
        video_info = {
            'title': yt.title,
            'author': yt.author,
            'views': yt.views,
            'length': yt.length,
            'streams': yt.streams.filter(file_extension='mp4')
        }
        return video_info
    except Exception as e:
        return {'error': str(e)}

def download_youtube_video(link, itag):
    try:
        yt = YouTube(link)
        ys = yt.streams.get_by_itag(itag)

        download_path_full = os.path.join(download_path, ys.title + '.mp4')

        print("\nDownloading...")
        ys.download(download_path)
        print("\nDownload completed!!")
    except Exception as e:
        print(f"Error: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    video_info = None
    link = session.get('link', None)

    if request.method == 'POST':
        link = request.form['link']
        session['link'] = link

        if 'itag' in request.form:
            itag = int(request.form['itag'])
            download_youtube_video(link, itag)
        else:
            video_info = get_video_info(link)

    return render_template('index.html', video_info=video_info, link=link)

if __name__ == '__main__':
    app.run(debug=True)
