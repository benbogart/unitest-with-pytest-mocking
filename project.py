from time import sleep


def fetch_goggles():
    # make an api call to goggles.com
    # ...
    sleep(4)

    response =  {'status':200,
                 "foo": True}

    # return a 408 (timeout) status code 
    response =  {"status": 408}

    return response

import helpers
def count_goggles():
    
    result = helpers.fetch_goggles()
    return result['count']