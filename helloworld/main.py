def hello_world(request):
    request_args = request.args   #takes all the passed arguments (after the '?' sign in the URL)

    ###Pass arguments with JSON###
    request_json = request.get_json(silent = True) #silent  = True means if we don't pass any json params then it puts Non

    if request_args and 'name' in request_args and 'lastname' in request_args:
        name = request_args['name']
        lastname = request_args['lastname']
    elif request_json and 'name' in request_json and 'lastname' in request_json:
        name = request_json['name']
        lastname = request_json['lastname']
    else:
        name = 'world'
        lastname = ''
    return f'Hello {name} {lastname}'