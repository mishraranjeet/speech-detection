import json

import requests
import os


class RequestSession:
    session = requests.Session()

    @classmethod
    def get_session(cls, service_name="SPEECH_PROCESSING"):
        return cls.session


def get_chunk_service(chunk):
    URL = os.getenv("SPEECH_SERVICE_URL")+"/process-chunk"
    headers = {
        'Authorization': os.getenv("AUTH_KEY"),
        'Content-Type': 'application/octet-stream'
    }
    response = RequestSession.get_session().post(URL, data=chunk, headers=headers)
    return response.json()

