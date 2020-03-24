import re

def verifier(address):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', address)
    if match == None:
        print('Bad Syntax')
        return 'NOT OK'
    else:
        return 'OK'
