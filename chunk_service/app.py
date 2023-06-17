from flask import Flask, request, jsonify

from models.chunks import ChunkService
from models.request import get_chunk_service
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv('.env')


@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"message": "Chunk service is up and running"})


@app.route('/send-chunk', methods=['GET'])
def send_chunk():
    # Get the audio file from the request
    audio_chunks = ChunkService().convert_chunks_to_bytearray()
    result = []
    for chunk in audio_chunks:
        chunk_result = get_chunk_service(chunk)
        result.append(chunk_result)
        # print(chunk_result)
    return jsonify({"message": "Chunk sent successfully", "result": result})




if __name__ == '__main__':
    app.run(debug=True, port=3000)