import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

CHUNK_SIZE_MS = 20  # Chunk size in milliseconds
CHUNK_RATE = 16000  # Sample rate in Hz


class ChunkService(object):
    def __init__(self, audio_file = None):
        if not audio_file:
            audio_file = "assignment_audio.wav"
        self.audio_file = audio_file

    def validate_input_file(self):
        if not os.path.exists(self.audio_file):
            raise Exception("Input file not found")

        if not self.audio_file.endswith(".wav"):
            raise Exception("Input file is not a WAV file")

    def convert_to_chunks(self):
        audio = AudioSegment.from_file(self.audio_file)
        # Split audio on silence into chunks
        chunks = split_on_silence(
            audio,
            min_silence_len=CHUNK_SIZE_MS,  # Minimum silence length to split on (in milliseconds)
            silence_thresh=-45 # Adjust this threshold according to your audio
        )

        return chunks

    def convert_chunks_to_bytearray(self):
        bytearrays = []
        chunks = self.convert_to_chunks()
        for chunk in chunks:
            # Export the chunk as a bytearray
            bytearray_chunk = bytearray(chunk.export(format="wav").read())
            # bytearray_chunk = chunk.export(format="wav").read()
            bytearrays.append(bytearray_chunk)

        return bytearrays
