# speech-detection


## Technologies:

- Python3
- Flask
- pydub for audio processing

## Installation

This project requires [Python](https://www.python.org/) v3.11 to run.

Steps to run the project.

```sh
1. Clone the repositiory and open in your favourite terminal
2. run this commnad to start rabbitmq server locally : docker-compose up -d
3. Open the given link in browser: http://localhost:4000/send-chunk
    - This link read the audio file convert to chunks in chunk micro service 
      and send the chunks to another micro service speech process that process the chunk 
      and return true or false message based on the speech present in the chunk