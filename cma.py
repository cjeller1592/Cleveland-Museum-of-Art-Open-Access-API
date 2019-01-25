import requests
import json

class openAccess(object):
    
    def search(self, q, limit):

        try:
            data = {'q': q,
                'limit': limit
                }

            r = requests.get('https://openaccess-api.clevelandart.org/api/artworks/',
                    headers={'Content-Type':'application/json'}, params=data)

        except Exception as e:
            print('Exception raised on search: %s' % e)
            return e

        result = r.json()['data']
        
        return result

    
    def find(self, id):

        try:
            r = requests.get('https://openaccess-api.clevelandart.org/api/artworks/' + id,
                    headers={'Content-Type':'application/json'})

        except Exception as e:
            print('Exception raised on find: %s' % e)
            return e

        result = r.json()['data']

        return result
