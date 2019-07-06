import json
import multiprocessing
from pathlib import Path

from flask import Flask, send_file

from imagefeed import feed_manager


ROOT_PATH = Path(__file__).parent.parent

app = Flask(__name__)

with open(ROOT_PATH / 'config.json') as f:
    CONFIG = json.load(f)


@app.route('/')
def index():
    return send_file(CONFIG['temp_file'], mimetype='image/png')


def main():
    temp_file = Path(CONFIG['temp_file'])
    if not temp_file.exists():
        temp_file.touch()

    process = multiprocessing.Process(target=feed_manager.capture,
                                      args=[CONFIG['refresh_interval'],
                                            CONFIG['video_capture_index'],
                                            CONFIG['temp_file']])

    process.start()

    app.run(host=CONFIG['host'], port=CONFIG['port'])


if __name__ == '__main__':
    main()
