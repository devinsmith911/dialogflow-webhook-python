# A simple webhook for DialogFlow using Python/Ngrok

## How to Configure Intent:
1. Configure the action in actionsConfig.py
2. Name the `action` on the DialogFlow UI to correspond with the one created in (1)

## How to Run:
1.  Download Ngrok from: https://ngrok.com/download
2.  Start ngrok with `./ngrok http 8080` or your relevant systems command
3.  Run `python pythonResponder.py` 
4.  Use the ngrok endpoint and input that in Dialogflow's webhook url
