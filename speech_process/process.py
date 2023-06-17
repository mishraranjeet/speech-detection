

class SpeechProcessService(object):
    def __init__(self, audio_chunks):
        self.audio_chunks = audio_chunks

    def process_chunks(self):
        silence_indices = {}
        for i, chunk in enumerate(self.audio_chunks):
            # Check if the chunk is silent (below the threshold)
            if chunk.dBFS < -40:  # Adjust this threshold according to your audio
                message = f" {False}, Speech not present in chunk {i}"
            else:
                print(True, "Speech detected in chunk")
                message = f" {False}, Speech not present in chunk {i}"
            silence_indices["chunk"] = chunk
            silence_indices["message"] = message
        return silence_indices

