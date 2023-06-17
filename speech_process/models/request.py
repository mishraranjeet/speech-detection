import json

import requests
import os


class RequestSession:
    session = requests.Session()

    @classmethod
    def get_session(cls, service_name="SPEECH_PROCESSING"):
        return cls.session


def get_chunk_service(chunk):
    URL = os.getenv("CHUNK_SERVICE_URL")
    payload = json.dumps({
        "chunk": chunk,
    })
    headers = {
        'Authorization': os.getenv("AUTH_KEY"),
        'Content-Type': 'application/json'
    }
    response = RequestSession.get_session().post(URL, data=payload, headers=headers)
    return response.json()

