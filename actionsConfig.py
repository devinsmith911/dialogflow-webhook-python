# Action templates are called by setting first key equal to the action name in the intent
# Use _underscores_ to declare variables

available_actions = {
    'make.name': {
        'params': ['color', 'number'],
        'response': {
          'speech': 'Alright, your silly name is _color_ _number_! I hope you like it! See you next time.',
          'displayText': 'Alright, your silly name is _color_ _number_! I hope you like it! See you next time.'
        }
    }
}
