available_actions = {
    'make.name': {
        'params': ['color', 'number'],
        'response': {
          'speech': 'Alright, your silly name is _color_ _number_! I hope you like it! See you next time.',
          'displayText': 'Alright, your silly name is _color_ _number_! I hope you like it! See you next time.'
        }
    }
}




# example of a response
# {
#     'id': '3751851b-021f-4285-9697-2c79890201be',
#     'lang': 'en',
#     'result': {'action': 'make.name',
#                 'actionIncomplete': 'false',
#                 'contexts': [],
#                 'fulfillment': {'messages': [{'speech': 'hello developer',
#                                             'type': 0}],
#                                 'speech': 'hello developer'},
#                 'metadata': {'intentId': '0d1a57cb-b1b6-49db-b4fb-85d6c07f49e9',
#                             'intentName': 'make_name',
#                             'webhookForSlotFillingUsed': 'false',
#                             'webhookUsed': 'true'},
#                 'parameters': {'color': 'red', 'given-name': '', 'number': 99},
#                 'resolvedQuery': 'my colour is red and my number is 99',
#                 'score': 1.0,
#                 'source': 'agent',
#                 'speech': ''},
#     'sessionId': '2ab1f01f-9b59-4cfe-8be9-07fcb4dc689a',
#     'status': {'code': 200, 'errorType': 'success', 'webhookTimedOut': 'false'},
#     'timestamp': '2018-03-31T13:10:18.528Z'
#  }