def createResponse(template, parameters):
  for param in template['params']:
    # Handle each type of response
    for response in template['response']:
      template['response'][response] = template['response']['speech'].replace('_' + param + '_', str(parameters[param]))
  return template['response']
