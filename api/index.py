from flask import Flask, Response, send_file, request
app = Flask(__name__)

import os, json
import yt_dlp, imageio_ffmpeg

class Logger:
    def debug(self, msg):
        pass

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

@app.route('/api/yt_dlp/download_info')
def download_info():
    link = request.args.get('link')

    with yt_dlp.YoutubeDL() as ytdlp:
        info_dict = ytdlp.extract_info(link, download=False)

    return Response(json.dumps(info_dict), 200)

@app.route('/api/yt_dlp/download')
def download():
    link = request.args.get('link')
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

    opts = {
        'outtmpl': '/tmp/%(title)s.%(ext)s',
        'ffmpeg_location': ffmpeg,
        'logger': Logger()
    }

    with yt_dlp.YoutubeDL(opts) as ytdlp:
        info_dict = ytdlp.extract_info(link, download=True)
        file_path = ytdlp.prepare_filename(info_dict)
        filename = os.path.basename(file_path)
    
    return send_file(file_path, download_name=filename, as_attachment=True)