from dotenv import load_dotenv
from flask import Flask, request, jsonify

from models.process import SpeechProcessService

app = Flask(__name__)
load_dotenv('.env')


@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"message": "Speech service is up and running"})


@app.route('/process-chunk', methods=['POST'])
def process_chunk():
    # Get the audio file from the request
    chunk_length = 20
    chunk = request.data
    audio_result = SpeechProcessService(chunk).process_chunks()
    return jsonify(audio_result)


if __name__ == '__main__':
    app.run(debug=True, port=9000, host='0.0.0.0')
