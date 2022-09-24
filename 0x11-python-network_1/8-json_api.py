#!/usr/bin/python3
'''task 8 script'''

if __name__ == '__main__':
    import requests
    import sys

    data = {'q': sys.argv[1] if len(sys.argv) >= 2 else ""}
    res = requests.post('http://0.0.0.0:5000/search_user', data=data)
    text = res.text

    try:
        json = res.json()
        if json.get('id', None) is None:
            print('No result')
        else:
            print('[{}] {}'.format(json['id'], json['name']))
    except Exception:
        print('Not a valid JSON')
