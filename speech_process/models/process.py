from pydub import AudioSegment
import io


class SpeechProcessService(object):
    def __init__(self, audio_chunks):
        self.audio_chunks = audio_chunks
        audio_stream = io.BytesIO(audio_chunks)
        self.audio_chunks = AudioSegment.from_file(audio_stream, format="wav")

    def process_chunks(self):
        silence_indices = {}
        for i, chunk in enumerate(self.audio_chunks):
            # Check if the chunk is silent (below the threshold)
            if chunk.dBFS < -45:  # Adjust this threshold according to your audio
                message = f" {False}, Speech not present in chunk {i}"
            else:
                print(True, "Speech detected in chunk")
                message = f" {True}, Speech present in chunk {i}"
            print("message", message,chunk.dBFS)
            silence_indices["message"] = message
        return silence_indices
