def createResponse(template, parameters):

  # template looks like:
  # {'params': ['color', 'number'],
  #   'response': {
  #     'speech': 'Alright, your silly name is _color_ _number_! I hope you like it! See you next time.',
  #     'displayText': 'Alright, your silly name is _color_ _number_! I hope you like it! See you next time.'
  #   }
  # }
  # parameters looks like:
  # 'parameters': {'color': 'red', 'given-name': '', 'number': 99},

  # how to gsub in python
  # replace('_' + x + '_', 'variable')

  #  
  print 'INSIDE CREATE RESPONSE'
  print 'INSIDE CREATE RESPONSE'
  print 'INSIDE CREATE RESPONSE'

  for param in template['params']:
    # template[param] = template[param].replace('_' + param + '_',)
    # do replace

    print 'param:'
    print param
    print 'template[resp][speech]'
    print template['response']['speech']
    print 'String replacement:'
    # print template['response']['speech'].replace('_' + param + '_', parameters[param])

    template['response']['speech'] = template['response']['speech'].replace('_' + param + '_', str(parameters[param]))

  return template